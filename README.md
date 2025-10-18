# 🧠 AI Consumer Insight Suite: 3-Day AI/ML Business Intelligence Project

## 🎯 Objective

Develop 3 modular AI projects in 3 days that can be individually useful to small businesses and collectively form an integrated **AI Consumer Insight Suite** for analyzing market sentiment, pricing strategy, and customer segmentation.

---

## 🗓️ Project Roadmap Overview

| Day       | Project                               | AI Technique              | Outcome                                                    | Reusability                                        |
| --------- | ------------------------------------- | ------------------------- | ---------------------------------------------------------- | -------------------------------------------------- |
| **Day 1** | Sentiment Analysis on Product Reviews | NLP + Text Classification | Analyze what customers say about a product category        | Plug-in for brand monitoring and feedback analysis |
| **Day 2** | Willingness-to-Pay (WTP) Prediction   | Regression + EDA          | Predict how much extra people will pay for premium quality | Module for pricing optimization                    |
| **Day 3** | Customer Segmentation                 | Clustering                | Identify groups of buyers with similar behavior            | Module for marketing & targeting                   |

---

## 📅 DAY 1: Sentiment Analysis Module

### 🎯 Objective

Analyze online product reviews (e.g., cold-pressed mustard oil) to extract customer sentiment and key themes.

### 🧩 Tasks

1. **Scrape Data:** Collect product reviews from e-commerce platforms or use a Kaggle dataset.
2. **Clean Data:** Remove stopwords, punctuation, and perform tokenization.
3. **Perform Sentiment Analysis:** Use pretrained **VADER** sentiment analyzer to compute sentiment polarity.
4. **Extract Keywords:** Use **TF-IDF** or **CountVectorizer** to find top positive/negative words.
5. **Visualize Results:** Generate bar plots for sentiment distribution.
6. **Save Output:** `sentiment_results.csv` and reusable `sentiment_analysis_module.py`.

### 📦 Deliverables

* CSV with sentiment scores per review
* Python module for analyzing sentiment on any product review dataset
* Optional Streamlit visualization for instant results

---

## 📅 DAY 2: Willingness-to-Pay (WTP) Prediction Module

### 🎯 Objective

Predict how likely customers are to pay a premium for better quality using survey data.

### 🧩 Tasks

1. **Collect Data:** Create Google Form or simulate dataset with features like income, frequency of purchase, trust score, etc.
2. **EDA:** Identify key correlations between features and WTP.
3. **Train Model:** Apply **Linear Regression** or **XGBoost Regressor**.
4. **Feature Importance:** Rank which attributes most affect price sensitivity.
5. **Export Model:** Save trained model as `wtp_model.pkl` with prediction API.

### 📦 Deliverables

* `pricing_module.py` with prediction function
* `wtp_model.pkl` (serialized model)
* Feature importance report or plot

### ♻️ Reuse Potential

Use this as a **pricing intelligence module** for any D2C or SME brand.

---

## 📅 DAY 3: Customer Segmentation Module

### 🎯 Objective

Identify and visualize distinct customer groups using clustering techniques.

### 🧩 Tasks

1. **Collect Data:** Use survey or sales dataset.
2. **Normalize Data:** Apply **StandardScaler**.
3. **Cluster Customers:** Run **K-Means** to group customers into segments.
4. **Analyze Results:** Profile each cluster based on average attributes.
5. **Visualize:** Plot clusters using **PCA** for 2D visualization.
6. **Save Output:** `customer_clusters.csv` and `segmentation_module.py`.

### 📦 Deliverables

* Clustered customer data with segment labels
* Python module for applying clustering to any dataset
* Visualization of segment distribution

---

## ⚙️ DAY 4: Integration — AI Consumer Insight Suite

### 🎯 Objective

Combine all modules into one deployable analytics platform.

### 📁 Folder Structure

```bash
ai_consumer_suite/
│
├── sentiment_analysis_module.py
├── pricing_module.py
├── segmentation_module.py
├── app.py  # Streamlit or Flask dashboard
├── data/
│   ├── reviews.csv
│   ├── survey_data.csv
│   └── cluster_output.csv
└── models/
    └── wtp_model.pkl
```

### 💡 Features

* Upload reviews → get sentiment insights
* Upload survey data → get WTP prediction
* Visualize customer segments interactively

### 💰 Monetization Idea

Offer this suite to:

* Local and organic brands for understanding consumer behavior
* D2C startups for feedback analysis and pricing optimization
* Market research agencies for automation

---

## 🧾 Resume Summary

**AI Consumer Insights Platform for Small Businesses**

* Developed an end-to-end AI toolkit performing sentiment analysis, pricing prediction, and customer segmentation.
* Analyzed 5,000+ customer reviews and survey data to identify key purchase drivers and price sensitivity trends.
* Designed modular architecture for reusability across industries (food, skincare, apparel).
* **Tech Stack:** Python, Scikit-Learn, NLTK, XGBoost, Streamlit.

---

## 🚀 Next Step

Start with **Day 1: Sentiment Analysis Module** — setup, code structure, and data preparation.
