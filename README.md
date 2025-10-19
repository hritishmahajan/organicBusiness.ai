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
