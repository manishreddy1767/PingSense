# 🔔 PingSense

> AI-Powered WhatsApp Notification Router

PingSense is an intelligent notification routing system that analyzes incoming WhatsApp messages and decides whether they deserve an **immediate notification**, should be **summarized**, or can be **muted**.

The system combines **Hybrid Retrieval**, **Rule-Based Reasoning**, **Semantic Search**, **LLM Decision Making**, and **Confidence Scoring** to make explainable notification decisions.

---

# 📌 Problem Statement

Modern messaging platforms generate an overwhelming number of notifications every day. Important alerts such as OTPs, payment requests, emergency messages, and scams are often mixed with promotional messages and routine group chats.

PingSense intelligently filters these notifications and ensures users receive only the messages that truly deserve immediate attention.

---

# ✨ Features

- 🔍 Hybrid Retrieval (Token + Semantic Search)
- 🧠 Rule-Based Decision Engine
- 🤖 Claude LLM Integration
- 📊 Confidence Scoring
- 🛡 Override Engine
- 📩 Explainable Notification Decisions
- 📈 Analytics Dashboard
- 📂 Batch Message Processing
- 📥 JSON & CSV Export
- 🖥 Interactive Streamlit Dashboard

---

# 🏗 System Architecture

```
Incoming WhatsApp Message
            │
            ▼
      Context Builder
            │
            ▼
 Multimodal Normalizer
            │
            ▼
 Hybrid Retrieval
(Token + Semantic Search)
            │
            ▼
      Rule Engine
            │
            ▼
      Claude LLM
            │
            ▼
    Override Engine
            │
            ▼
  Confidence Engine
            │
            ▼
 Final Decision

 Notify
 Summarize
 Mute
```

---

# 🚀 Technologies Used

| Category | Technology |
|----------|------------|
| Language | Python |
| Frontend | Streamlit |
| Data | Pandas, NumPy |
| Machine Learning | Sentence Transformers |
| Semantic Search | all-MiniLM-L6-v2 |
| LLM | Claude API |
| Visualization | Matplotlib |
| Similarity | Scikit-learn |
| Output | JSON, CSV |

---

# 📂 Project Structure

```
PingSense/
│
├── Home.py
│
├── pages/
│   ├── 1_Analytics.py
│   └── 2_Architecture.py
│
├── src/
│   ├── analytics/
│   ├── confidence/
│   ├── context/
│   ├── data/
│   ├── llm/
│   ├── multimodal/
│   ├── output/
│   ├── overrides/
│   ├── pipeline/
│   ├── retrieval/
│   ├── rules/
│   └── main.py
│
├── outputs/
│   ├── results.csv
│   └── results.json
│
├── screenshots/
│
├── docs/
│
├── requirements.txt
├── README.md
└── LICENSE
```

---

# ⚙ Installation

Clone the repository

```bash
git clone <repository-url>
```

Move into the project

```bash
cd PingSense
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶ Running the Project

Generate predictions

```bash
python -m src.main
```

Launch Streamlit Dashboard

```bash
streamlit run Home.py
```

---

# 📊 Analytics

The analytics dashboard provides

- Total Messages
- Notify Count
- Summarize Count
- Mute Count
- Message Type Distribution
- Confidence Distribution
- Search & Filter
- CSV Export
- JSON Export

---

# 🧠 AI Decision Pipeline

1. Load incoming message
2. Build contextual information
3. Normalize multimodal content
4. Retrieve similar historical messages
5. Apply rule engine
6. Generate LLM reasoning
7. Apply override rules
8. Compute confidence score
9. Produce final notification decision

---

# 📷 Screenshots

## Home Dashboard

![Home](screenshots/home.png)

---

## Analytics Dashboard

![Analytics](screenshots/analytics.png)

---

## Architecture

![Architecture](screenshots/architecture.png)

---

## Decision View

![Decision](screenshots/decision.png)

---

## Evidence View

![Evidence](screenshots/evidence.png)

---

# 📈 Sample Output

```json
{
    "message_id": "msg_023",
    "action": "notify",
    "message_type": "business",
    "confidence": 0.765,
    "reason": "Payment related message."
}
```

---

# 🔮 Future Improvements

- Voice message transcription
- Image OCR
- Multilingual support
- Personalized learning
- Real-time WhatsApp integration
- Vector database retrieval
- Mobile application
- User feedback learning

---

# 👨‍💻 Author

**Manish Reddy**

Computer Science and Engineering

---

# 📄 License

This project is released under the MIT License.