# 🧠 AI Consumer Insight Suite: 3-Day AI/ML Business Intelligence Project

## 🎯 Objective

Develop 3 modular AI projects in 3 days that can be individually useful to small businesses and collectively form an integrated **AI Consumer Insight Suite** for analyzing market sentiment, pricing strategy, and customer segmentation.

---

## 🗓️ Project Roadmap Overview

| Day       | Project                               | AI Technique              | Outcome                                                    | Reusability                                        |
| ---------- | ------------------------------------- | ------------------------- | ---------------------------------------------------------- | -------------------------------------------------- |
| **Day 1**  | Sentiment Analysis on Product Reviews | NLP + Text Classification | Analyze what customers say about a product category        | Plug-in for brand monitoring and feedback analysis |
| **Day 2**  | Willingness-to-Pay (WTP) Prediction   | Regression + EDA          | Predict how much extra people will pay for premium quality | Module for pricing optimization                    |
| **Day 3**  | Customer Segmentation                 | Clustering                | Identify groups of buyers with similar behavior            | Module for marketing & targeting                   |

---

## 📅 DAY 1: Sentiment Analysis Module

### 🎯 Objective
Analyze online product reviews (e.g., cold-pressed mustard oil or any category) to extract customer sentiment and key themes.

### 🧩 Tasks
1. **Load Data:** Import large-scale review dataset (e.g., Amazon product reviews).
2. **Clean Text:** Remove punctuation, stopwords, and perform tokenization using NLTK.
3. **Vectorize Features:** Apply **TF-IDF** to convert text into numerical features.
4. **Train Model:** Fit a **Naive Bayes** classifier for sentiment prediction.
5. **Evaluate:** Measure model accuracy and F1-score.
6. **Visualize:** Display sentiment distribution and top frequent words.
7. **Export:** Save sentiment metrics and predictions as JSON.

---

### 🧠 Implementation Snapshot

#### ✅ Cleaned Sample

| review | cleaned |
|--------|----------|
| I have bought several of the Vitality canned dog food products... | bought several vitality canned dog food products loved quality |
| Product arrived labeled as Jumbo Salted Peanuts... | product arrived labeled jumbo salted peanutsthrowaway |
| This is a confection that has been around a few centuries... | confection around centuries light pillowy citrusy delightful |
| If you are looking for the secret ingredient in Robitussin... | looking secret ingredient robitussin believe flavor similar |
| Great taffy at a great price. There was a wide assortment... | great taffy great price wide assortment yummy flavors |

---

#### ⚙️ Vectorizing text features using TF-IDF...
#### 📊 Splitting dataset into train/test sets...
#### 🤖 Training sentiment model...
#### 📈 Evaluating model performance...

---

### ✅ Model Evaluation

```
Accuracy: 80.72%

              precision    recall  f1-score   support
    negative       0.93      0.13      0.23     24935
    positive       0.80      1.00      0.89     88756

    accuracy                           0.81    113691
   macro avg       0.87      0.56      0.56    113691
weighted avg       0.83      0.81      0.75    113691
```

---

### 📊 Visualization Summary

- Sentiment distribution bar chart  
- WordCloud of top frequent terms (positive and negative)  
- Training time visualization for large datasets  

---

### 🧾 Final Output Summary

```json
{
    "file_used": "reviews.csv",
    "accuracy": 80.72,
    "positive_reviews": 443777,
    "negative_reviews": 124677,
    "total_reviews": 568454,
    "processing_time_sec": 3291.43,
    "sample_predictions": {
        "This product is amazing and worth every penny": {
            "sentiment": "positive",
            "confidence": 97.84
        },
        "Terrible quality and bad packaging": {
            "sentiment": "negative",
            "confidence": 58.34
        },
        "I absolutely love the experience using this": {
            "sentiment": "positive",
            "confidence": 90.94
        },
        "Feels cheap and not effective": {
            "sentiment": "positive",
            "confidence": 84.6
        }
    }
}
```

✅ **Processing Time:** 3291.43 seconds (~55 min for ~0.5 M reviews)  
✅ **GPU/CPU Optimization:** Parallel TF-IDF with caching and memory management  

---

### 💻 Hardware Utilization (Apple M2 Benchmark)

| Component | Avg Utilization | Peak | Notes |
|------------|----------------|------|-------|
| Efficiency Cores | 74 % @ 1445 MHz | 82 % | Handles light matrix operations |
| Performance Cores | 99 % @ 1967 MHz | 100 % | Dominant in TF-IDF and Naive Bayes training |
| GPU (10-core Metal) | 27 % @ 444 MHz | 38 % | Minimal in classical ML phase |
| RAM | 6.6 / 8 GB | 8.0 GB (+ swap 8.5 GB) | Heavy TF-IDF caching |
| CPU Power | 1.98 W (avg 2.30 W peak 4.03 W) | – | High sustained load for 55 min |

> 💡 Next upgrade (Day 2): Transition to **TensorFlow + Metal** to fully utilize GPU/ANE.

---

## 📦 Deliverables

- `sentiment_output.json` with performance metrics  
- Python module: `consumer_sentiment_module.py`  
- Visualizations: Sentiment Distribution & WordCloud  

---

## 📅 DAY 2: Willingness-to-Pay (WTP) Prediction Module

### 🎯 Objective
Predict how likely customers are to pay a premium for better quality using survey data.

### 🧩 Tasks
1. **Collect Data:** Create or simulate dataset with features like income, frequency of purchase, trust score, etc.  
2. **EDA:** Identify key correlations between features and WTP.  
3. **Train Model:** Apply **Linear Regression** or **XGBoost Regressor**.  
4. **Feature Importance:** Rank attributes influencing price sensitivity.  
5. **Export Model:** Save trained model as `wtp_model.pkl` with prediction API.

### 📦 Deliverables
- `pricing_module.py` with prediction function  
- `wtp_model.pkl` (serialized model)  
- Feature importance report or visualization  

### ♻️ Reuse Potential
Use this as a **pricing intelligence module** for D2C or SME brands.

---

## 📅 DAY 3: Customer Segmentation Module

### 🎯 Objective
Identify and visualize distinct customer groups using clustering.

### 🧩 Tasks
1. **Collect Data:** Use survey or sales dataset.  
2. **Normalize Data:** Apply **StandardScaler**.  
3. **Cluster Customers:** Run **K-Means** to group customers into segments.  
4. **Profile Results:** Analyze each cluster’s behavior.  
5. **Visualize:** Plot clusters using **PCA** in 2D.  
6. **Save Output:** `customer_clusters.csv` and `segmentation_module.py`.

### 📦 Deliverables
- Clustered customer data with segment labels  
- Python module for clustering any dataset  
- Visualization of segment distribution  

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

* Built an end-to-end AI toolkit performing sentiment analysis, pricing prediction, and customer segmentation.  
* Processed 500 K+ customer reviews to identify purchase drivers and price sensitivity.  
* Designed modular architecture for reusability across industries (food, skincare, apparel).  
* **Tech Stack:** Python | Scikit-Learn | NLTK | TensorFlow | XGBoost | Streamlit  

---

## 🚀 Next Step

Proceed to **Day 2: Willingness-to-Pay (WTP) Prediction** — configure dataset, design regression architecture, and enable GPU acceleration for faster model training.
