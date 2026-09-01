import json
import re
import anthropic
import pandas as pd
import os

from dotenv import load_dotenv
load_dotenv()
_anthropic_key = os.getenv("ANTHROPIC_API_KEY")
try:
    import streamlit as st
    if st.secrets.get("ANTHROPIC_API_KEY"):
        _anthropic_key = st.secrets["ANTHROPIC_API_KEY"]
except Exception:
    pass

client = anthropic.Anthropic(api_key=_anthropic_key)

MODEL = "claude-sonnet-4-5"

SYSTEM_PROMPT = """You are a senior product strategist at a top e-commerce consulting firm \
with 10 years of experience turning Amazon customer feedback into high-impact product and \
marketing decisions. You have deep expertise in voice-of-customer analysis, competitive \
positioning, and Amazon listing optimization.

Your analyses are precise, commercially grounded, and directly actionable. You never pad \
with generic advice — every recommendation is specific to the product and evidence from \
the reviews. You always respond with valid JSON and nothing else."""


def _build_user_prompt(product_info: dict, reviews_df: pd.DataFrame) -> str:
    title = product_info.get("title", "Unknown Product")
    rating = product_info.get("overall_rating", "N/A")
    total = product_info.get("total_reviews", "N/A")
    asin = product_info.get("asin", "N/A")

    review_lines = []
    for i, row in reviews_df.iterrows():
        stars = row.get("rating", "?")
        body = row.get("body", "")
        date = row.get("date", "")
        verified = row.get("verified_purchase", False)
        review_lines.append(
            f"[Review {i+1}] ★{stars} | Verified: {verified} | {date}\n{body}"
        )

    reviews_block = "\n\n---\n\n".join(review_lines)

    return f"""Analyze the following Amazon product reviews and return ONLY a valid JSON object \
matching the exact schema below. No markdown, no explanation, no code fences — raw JSON only.

PRODUCT DETAILS:
- Title: {title}
- ASIN: {asin}
- Overall Rating: {rating}/5
- Total Reviews on Amazon: {total}
- Reviews in this analysis: {len(reviews_df)} (pre-filtered for authenticity)

TRUSTED REVIEWS:
{reviews_block}

REQUIRED JSON SCHEMA:
{{
  "executive_summary": "2-3 sentence overview of product health",
  "overall_health_score": <integer 0-100>,
  "complaint_themes": [
    {{
      "theme": "theme name",
      "frequency_pct": <number: percentage of reviews mentioning this>,
      "emotional_intensity": "low|medium|high|critical",
      "example_quotes": ["quote1", "quote2"],
      "improvement_recommendation": "specific actionable fix",
      "estimated_rating_impact": "e.g. +0.3 stars if fixed"
    }}
  ],
  "praise_themes": [
    {{
      "theme": "theme name",
      "frequency_pct": <number>,
      "example_quotes": ["quote1", "quote2"],
      "marketing_angle": "how to use this in marketing copy"
    }}
  ],
  "listing_bullets": ["bullet1", "bullet2", "bullet3", "bullet4", "bullet5"],
  "listing_title_suggestion": "optimized title using customer language",
  "buyer_personas": [
    {{
      "persona_name": "e.g. The Gift Buyer",
      "percentage": <number: estimated pct of reviewers>,
      "description": "who they are",
      "what_they_love": "main appeal",
      "what_frustrates_them": "main complaint",
      "marketing_message": "how to speak to them"
    }}
  ],
  "risk_alerts": [
    {{
      "alert_type": "e.g. Quality Decline / Competitor Threat / Return Risk",
      "severity": "low|medium|high|critical",
      "description": "what the alert is about",
      "recommended_action": "what to do about it"
    }}
  ],
  "keyword_opportunities": ["keyword1", "keyword2", "keyword3"],
  "pricing_sentiment": "are complaints price-related? summary",
  "seasonal_patterns": "any patterns noticed in review dates or buying occasions"
}}

Return ONLY the JSON object. No other text."""


def _call_claude(user_prompt: str, strict: bool = False) -> str:
    prefix = "CRITICAL: Return raw JSON only. No markdown. No explanation. Start with {.\n\n" if strict else ""
    response = client.messages.create(
        model=MODEL,
        max_tokens=4096,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": prefix + user_prompt}],
    )
    return response.content[0].text.strip()


def _parse_json(raw: str) -> dict:
    # Strip accidental markdown fences if present
    if raw.startswith("```"):
        raw = re.sub(r"^```(?:json)?\s*", "", raw, flags=re.MULTILINE)
        raw = re.sub(r"\s*```$", "", raw, flags=re.MULTILINE)
    return json.loads(raw.strip())


def _format_reviews_block(reviews_df: pd.DataFrame, label: str) -> str:
    lines = []
    for i, row in reviews_df.iterrows():
        stars = row.get("rating", "?")
        body = row.get("body", "")
        verified = row.get("verified_purchase", False)
        date = row.get("date", "")
        lines.append(f"[{label} Review {i+1}] ★{stars} | Verified: {verified} | {date}\n{body}")
    return "\n\n---\n\n".join(lines)


def _build_gap_prompt(
    my_info: dict,
    my_df: pd.DataFrame,
    comp_info: dict,
    comp_df: pd.DataFrame,
) -> str:
    def summary(info, df):
        return (
            f"Title: {info.get('title', 'N/A')}\n"
            f"ASIN: {info.get('asin', 'N/A')}\n"
            f"Overall Rating: {info.get('overall_rating', 'N/A')}/5\n"
            f"Total Reviews on Amazon: {info.get('total_reviews', 'N/A')}\n"
            f"Reviews in this analysis: {len(df)}"
        )

    return f"""You are conducting a competitive intelligence analysis between two Amazon products. \
Compare the two products using ONLY evidence from the reviews provided. \
Return ONLY a valid JSON object matching the exact schema below. No markdown, no explanation, \
no code fences — raw JSON only.

=== MY PRODUCT ===
{summary(my_info, my_df)}

MY PRODUCT REVIEWS:
{_format_reviews_block(my_df, "Mine")}

=== COMPETITOR PRODUCT ===
{summary(comp_info, comp_df)}

COMPETITOR REVIEWS:
{_format_reviews_block(comp_df, "Competitor")}

REQUIRED JSON SCHEMA:
{{
  "my_advantages": [
    {{
      "advantage": "what my product does better than the competitor",
      "evidence": "direct quote or paraphrase from competitor reviews highlighting this gap",
      "marketing_angle": "how to use this advantage in ads or listing copy"
    }}
  ],
  "my_vulnerabilities": [
    {{
      "vulnerability": "where the competitor beats my product",
      "evidence": "direct quote or paraphrase from my reviews revealing this weakness",
      "fix_recommendation": "specific actionable step to close this gap"
    }}
  ],
  "market_opportunity": "2-3 sentence overall strategic recommendation based on the gaps",
  "positioning_statement": "suggested unique value proposition that exploits the competitor's weaknesses",
  "head_to_head_scores": {{
    "quality_perception": {{"mine": <0-10>, "competitor": <0-10>}},
    "value_for_money": {{"mine": <0-10>, "competitor": <0-10>}},
    "customer_service": {{"mine": <0-10>, "competitor": <0-10>}},
    "shipping_packaging": {{"mine": <0-10>, "competitor": <0-10>}},
    "ease_of_use": {{"mine": <0-10>, "competitor": <0-10>}}
  }}
}}

Return ONLY the JSON object. No other text."""


def analyze_reviews(product_info: dict, trusted_reviews_df: pd.DataFrame) -> dict:
    if trusted_reviews_df.empty:
        raise ValueError("No trusted reviews to analyze.")

    user_prompt = _build_user_prompt(product_info, trusted_reviews_df)

    raw = _call_claude(user_prompt)
    try:
        return _parse_json(raw)
    except (json.JSONDecodeError, ValueError):
        print("Warning: first response was invalid JSON — retrying with strict prompt.")
        raw = _call_claude(user_prompt, strict=True)
        return _parse_json(raw)


def competitor_gap_analysis(
    my_product_info: dict,
    my_trusted_reviews: pd.DataFrame,
    competitor_product_info: dict,
    competitor_trusted_reviews: pd.DataFrame,
) -> dict:
    if my_trusted_reviews.empty or competitor_trusted_reviews.empty:
        raise ValueError("Both products need trusted reviews for a gap analysis.")

    user_prompt = _build_gap_prompt(
        my_product_info, my_trusted_reviews,
        competitor_product_info, competitor_trusted_reviews,
    )

    raw = _call_claude(user_prompt)
    try:
        return _parse_json(raw)
    except (json.JSONDecodeError, ValueError):
        print("Warning: first response was invalid JSON — retrying with strict prompt.")
        raw = _call_claude(user_prompt, strict=True)
        return _parse_json(raw)


if __name__ == "__main__":
    import time
    from rainforest import fetch_product_reviews
    from utils import filter_fake_reviews

    # --- My product: AirPods 2nd Gen ---
    print("Fetching my product (AirPods)...")
    my_result = fetch_product_reviews("B07PXGQC1Q")
    my_info = my_result["product_info"]
    my_trusted, _, my_stats = filter_fake_reviews(my_result["reviews"])
    print(f"  {my_info['title'][:60]}...")
    print(f"  Trusted: {my_stats['trusted_count']} | Flagged: {my_stats['flagged_count']}")

    time.sleep(3)

    # --- Competitor: AirPods 3rd Gen ---
    print("\nFetching competitor (AirPods 3rd Gen)...")
    comp_result = fetch_product_reviews("B09JQL3NWT")
    comp_info = comp_result["product_info"]
    comp_trusted, _, comp_stats = filter_fake_reviews(comp_result["reviews"])
    print(f"  {comp_info['title'][:60]}...")
    print(f"  Trusted: {comp_stats['trusted_count']} | Flagged: {comp_stats['flagged_count']}")

    print("\nRunning competitor gap analysis...")
    gap = competitor_gap_analysis(my_info, my_trusted, comp_info, comp_trusted)

    print("\n=== COMPETITIVE GAP ANALYSIS ===\n")
    print(json.dumps(gap, indent=2))
