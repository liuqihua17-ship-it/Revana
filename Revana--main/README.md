# Revana — AI-Powered Review Intelligence

> Stop reading reviews. Start making decisions.

Revana is an AI-powered review intelligence platform for Amazon sellers. Paste an ASIN, get a complete product strategy in under 2 minutes.

## Features

- 🔍 Live Amazon review fetching via Rainforest API
- 🛡️ Fake review detection and filtering (12-signal heuristic scorer)
- 🧠 Claude AI-powered Voice of Customer analysis
- 📊 Competitor gap analysis with head-to-head scoring
- ✍️ AI-generated listing copy optimizer
- 📈 Sentiment trend tracking over time
- 👥 Buyer persona identification
- 📤 Exportable reports (TXT, CSV, JSON)

## Setup

**1. Clone the repo**
```bash
git clone https://github.com/YOUR_USERNAME/revana.git
cd revana
```

**2. Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Add your API keys**

Create a `.env` file in the project root:
```
RAINFOREST_API_KEY=your_key_here
ANTHROPIC_API_KEY=your_key_here
```

- Rainforest API key: [rainforestapi.com](https://www.rainforestapi.com)
- Anthropic API key: [console.anthropic.com](https://console.anthropic.com)

**5. Run the app**
```bash
streamlit run app.py
```

Then open [http://localhost:8501](http://localhost:8501).

> **No API keys?** Enable **Demo Mode** in the app to explore a full example with pre-loaded data — no internet required.

## Project Structure

```
revana/
├── app.py          # Streamlit UI — all tabs and layout
├── analyzer.py     # Claude AI analysis engine
├── rainforest.py   # Rainforest API client
├── utils.py        # Fake review filter + sentiment trends
├── demo_data.py    # Pre-loaded demo data (no API calls needed)
└── .streamlit/
    └── config.toml # Light theme + color config
```

## Tech Stack

| Layer | Technology |
|---|---|
| UI | Python + Streamlit |
| AI Analysis | Anthropic Claude API (`claude-sonnet-4-6`) |
| Amazon Data | Rainforest API |
| Charts | Plotly |
| Data | Pandas |
| Config | python-dotenv |

## Team

- Tamarakare Edwin-Biayeibo
- Gema Zhu
- Qihua Liu
- Wenqi Song

**BANA 274 · UCI Paul Merage School of Business · Spring 2026**
