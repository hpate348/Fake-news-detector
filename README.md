# 🗞️ Fake News Detector

A machine learning web app that classifies news articles as **real or fake** using TF-IDF vectorization and Logistic Regression, trained on 44,000+ labeled articles.



---

## How It Works

1. **Input** — Paste any news headline or article into the app
2. **Vectorize** — Text is converted into numerical features using TF-IDF
3. **Classify** — Logistic Regression predicts real or fake with a confidence score
4. **Output** — Instant result with percentage confidence

The model learned which words are strongly associated with fake vs. real news across 44,000 articles. Words like *"shocking"* and *"hoax"* skew fake; words like *"confirmed"* and *"reuters"* skew real.

---

## Results

| Metric | Fake | Real |
|--------|------|------|
| Precision | 98% | 99% |
| Recall | 99% | 98% |
| F1 Score | 98% | 98% |

**Overall Accuracy: 98.5%** on held-out test set (8,800+ articles)

---

## Tech Stack

| Tool | Purpose |
|------|---------|
| Python | Core language |
| Pandas | Data loading & cleaning |
| Scikit-learn | TF-IDF vectorizer + Logistic Regression |
| Pickle | Saving & loading the trained model |
| Streamlit | Interactive web UI |
| Hugging Face Spaces | Free cloud deployment |

---

## Run It Locally

```bash
# 1. Clone the repo
git clone https://github.com/YOUR_USERNAME/fake-news-detector.git
cd fake-news-detector

# 2. Install dependencies
pip install -r requirements.txt

# 3. Train the model (only needed once)
python train.py

# 4. Launch the app
streamlit run app.py
```

---

## Project Structure

```
fake-news-detector/
├── data/
│   ├── Fake.csv
│   └── True.csv
├── model/
│   └── model.pkl
├── app.py          ← Streamlit web app
├── train.py        ← Model training script
└── README.md
```

---

## Dataset

**ISOT Fake News Dataset** — 44,898 articles labeled as real or fake, sourced from Reuters and various fake news websites.

→ [View on Kaggle](https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset)

---

## Future Improvements

- [ ] Upgrade to a fine-tuned BERT model for better accuracy
- [ ] Add SHAP explainability to highlight which words influenced the prediction
- [ ] Accept URLs and scrape article text automatically using `newspaper3k`
- [ ] Add a history log of past predictions

---

## Requirements

```
pandas
scikit-learn
streamlit
pickle5
```

---

*Built as part of a beginner ML portfolio project.*
