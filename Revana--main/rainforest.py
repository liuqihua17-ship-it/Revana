import requests
import pandas as pd
import os
import time

try:
    import streamlit as st
    RAINFOREST_API_KEY = st.secrets["RAINFOREST_API_KEY"]
except Exception:
    from dotenv import load_dotenv
    load_dotenv()
    RAINFOREST_API_KEY = os.getenv("RAINFOREST_API_KEY")
BASE_URL = "https://api.rainforestapi.com/request"


def fetch_product_reviews(asin: str) -> dict:
    params = {
        "api_key": RAINFOREST_API_KEY,
        "type": "product",
        "asin": asin,
        "amazon_domain": "amazon.com",
        "include_reviews": "true",
    }

    resp = requests.get(BASE_URL, params=params)

    if resp.status_code != 200:
        print(f"Error {resp.status_code}:")
        print(resp.text)
        resp.raise_for_status()

    time.sleep(3)

    data = resp.json()
    product_data = data.get("product", {})

    main_image = product_data.get("main_image", "")
    product_info = {
        "title": product_data.get("title"),
        "overall_rating": product_data.get("rating"),
        "total_reviews": product_data.get("ratings_total"),
        "asin": asin,
        "image_url": main_image.get("link", "") if isinstance(main_image, dict) else str(main_image or ""),
    }

    raw_reviews = (
    product_data.get("top_reviews") or
    product_data.get("reviews") or
    []
    )

    rows = []
    for r in raw_reviews:
        rows.append({
            "rating": r.get("rating"),
            "title": r.get("title"),
            "body": r.get("body"),
            "date": r.get("date"),
            "verified_purchase": r.get("verified_purchase", False),
            "reviewer_name": r.get("profile", {}).get("name"),
        })

    reviews_df = pd.DataFrame(rows)

    return {"product_info": product_info, "reviews": reviews_df}


if __name__ == "__main__":
    result = fetch_product_reviews("B08N5WRWNW")
    print("Product:", result["product_info"])
    print("\nFirst 5 reviews:")
    print(result["reviews"].head())
