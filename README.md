
# 🧴 Smart Skincare Recommender

An intelligent product ranking system for skincare products — blending rule-based logic, manual overrides, and optional AI reasoning to deliver dynamic top-N recommendations.

---

## 📌 Features

- 🔍 **Product Ranking** by views, sales, stock, or brand tier
- 🧠 **AI Prompt Filtering** using natural language (optional)
- 👨‍💼 **Manual Override System** for marketing teams
- 🕒 **CRON API Support** for daily refresh and auto-tasks
- 🌙 **Dark Mode UI** with modern leaderboard layout
- 📊 Built with **Flask + HTML + JavaScript + Pandas + Smolagents**

---

## 🎥 Frontend Preview

<img src="docs/screenshot-light.png" alt="light mode" width="500"/>
<img src="docs/screenshot-dark.png" alt="dark mode" width="500"/>

---

## 📂 Project Structure

```
├── agent_runner.py         # (Optional) AI code generation logic
├── dat.py                  # Flask app: routes, ranking, API
├── templates/
│   └── index.html          # UI: leaderboard, AI input, dark mode
├── static/                 # Optional CSS/JS folders
├── logs/
│   └── overrides.log       # Manual override log
├── Mock_Skincare_Dataset - Data.csv
└── README.md
```

---

## ⚙️ Setup Instructions

1. **Clone the repo**
   ```bash
   git clone https://github.com/yourusername/skincare-recommender.git
   cd skincare-recommender
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # or .\venv\Scripts\activate on Windows
   ```

3. **Install requirements**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask app**
   ```bash
   python dat.py
   ```

5. Visit: [http://localhost:5000](http://localhost:5000)

---

## 🔁 API Endpoints

| Route | Method | Purpose |
|-------|--------|---------|
| `/` | GET | Frontend homepage |
| `/recommendations` | GET | Top N product recommendations |
| `/ai-recommendations` | POST | Accepts AI prompt and returns filtered products |
| `/override` | POST | Manually promote a product |
| `/overrides` | GET | View current manual overrides |
| `/reset` | POST | Clear all overrides |
| `/cron/daily-refresh` | POST | (Optional) Scheduled task for refresh |
| `/cron/clear-overrides` | POST | (Optional) Reset overrides via CRON |

---

## 🧠 AI Logic (Optional)

You can optionally use:
- 🤖 `OpenAI GPT` (via API)
- 🔧 `SmolAgents` (via HuggingFace)
- 📜 Or plain Python rule logic (recommended for simplicity)

Example prompt:  
> “Show top 5 Tier A products by sales”

---

## 📅 CRON Setup (To Be Implemented)

Use Linux cron, `cron-job.org`, or cloud automation to trigger daily tasks:

```bash
# Run at 3am every day
0 3 * * * curl -X POST http://localhost:5000/cron/daily-refresh
```

---

## 🛠 Technologies

- Python 3.x
- Flask
- Pandas
- HTML5, CSS3
- JavaScript (Vanilla)
- Hugging Face AI Agent Framework(smolagents)

---

## 📜 License

MIT License.  
Feel free to fork and adapt for fashion, electronics, or grocery recommendations.

---

## 💬 Contact

Created by [@yourname](https://github.com/yourusername).  
Got feedback? Open an issue or reach out!
