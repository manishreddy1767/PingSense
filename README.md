# 🔔 PingSense

> AI-Powered WhatsApp Notification Router

PingSense is an explainable AI system that intelligently routes WhatsApp notifications into **Notify**, **Summarize**, or **Mute** by combining hybrid retrieval, rule-based reasoning, and LLM-powered decision making.

---

## 🚀 Features

- 🔍 Hybrid Retrieval (Token + Semantic Search)
- 🤖 LLM-based Message Classification
- ⚙️ Rule-based Decision Engine
- 📈 Confidence Scoring
- 🛡️ Override Engine
- 📊 Analytics Dashboard
- 🖥️ Streamlit Web Interface
- 📥 JSON & CSV Export
- 🔎 Explainable AI Pipeline

---

## 🏗️ System Architecture

```
Incoming WhatsApp Message
          │
          ▼
 Context Builder
          │
          ▼
 Multimodal Normalizer
(Text / Image / Voice)
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
```

---

## 📂 Project Structure

```
PingSense/
│
├── Home.py
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
│   └── rules/
│
├── data/
├── outputs/
├── screenshots/
├── docs/
├── requirements.txt
└── README.md
```

---

## ⚙️ Technologies Used

| Layer | Technology |
|--------|------------|
| Frontend | Streamlit |
| Backend | Python |
| Data Processing | Pandas |
| Semantic Retrieval | Sentence Transformers |
| LLM | Claude |
| Visualization | Matplotlib |
| Output | JSON, CSV |

---

## 📊 Analytics

The analytics dashboard provides:

- Action distribution
- Message type distribution
- Confidence distribution
- Search & filter
- Export results

---

## 🖥️ Streamlit Dashboard

The application provides:

- 📩 Incoming Message
- 🔍 Retrieved Evidence
- ⚙️ Triggered Rules
- 🤖 LLM Decision
- 🎯 Final Decision
- 📊 Analytics
- 🏗️ Architecture

---

## ▶️ Installation

Clone the repository:

```bash
git clone https://github.com/<your-username>/PingSense.git
cd PingSense
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Generate outputs:

```bash
python -m src.main
```

Launch the dashboard:

```bash
streamlit run Home.py
```

---

## 📷 Screenshots

### Home Dashboard

![Home](screenshots/home.png)

### Analytics Dashboard

![Analytics](screenshots/analytics.png)

### Architecture Page

![Architecture](screenshots/architecture.png)

---

## 📈 Sample Output

```
Action      : Notify
Type        : Business
Confidence  : 76.5%

Evidence
- Same business
- Previously opened
- Semantic similarity

Decision
Notify immediately
```

---

## 🔮 Future Work

- Live WhatsApp integration
- Real-time notifications
- User preference learning
- Additional LLM providers
- Mobile application
- RAG-based memory
- Active learning feedback

---

## 👨‍💻 Author

**Manish Reddy**

Computer Science Engineering Student

---

## 📄 License

This project is licensed under the MIT License.