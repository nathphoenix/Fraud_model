# 🛡️ Fraud Detection System

## 📘 Project Overview

This project aims to develop a robust, machine learning-based **Fraud Detection System** capable of identifying fraudulent financial transactions using behavioral, contextual, and temporal features. It leverages historical data and intelligent feature engineering to detect anomalies with high accuracy.

---

## 🎯 Objective

To build and deploy a real-time fraud detection model that:
- Detects fraudulent transactions with high recall and low false positive rate.
- Leverages engineered features from transaction data.
- Provides predictions via a RESTful API.
- Supports scalability via Docker and Flask.

---

## 🧠 Problem Statement

Traditional rule-based fraud detection systems struggle to keep up with evolving fraud patterns. This project solves that limitation by applying data-driven machine learning techniques to detect both known and unknown fraud behaviors, offering better adaptability and precision.

---

## 📊 Dataset Description

The dataset consists of transaction records with the following features:

| Feature | Description |
|--------|-------------|
| `transaction_amount` | The monetary value of the transaction. |
| `transaction_type` | Type of transaction (e.g., withdrawal, transfer). |
| `device_type` | The device used for the transaction. |
| `location` | Geographic location of the transaction. |
| `time_of_day` | Part of the day the transaction occurred. |
| `day_of_week` | Day of the week the transaction took place. |
| `is_foreign_transaction` | Flag for international transactions. |
| `is_high_risk_country` | Indicates high-risk origin country. |
| `previous_fraud_flag` | Indicates if the user has prior fraud history. |
| `risk_score` | Precomputed score indicating transaction risk. |
| `hour` | Hour extracted from transaction timestamp. |

**Target Variable:**
- `label_code` – Binary label where `1` indicates fraud and `0` indicates legitimate transaction.

---

## 🔧 Methodology

### 1. Data Preprocessing
- Handle missing values and outliers.
- Encode categorical variables (e.g., `transaction_type`, `device_type`, etc.).
- Normalize continuous features like `transaction_amount` and `risk_score`.
- Feature engineering: convert `time_of_day`, `day_of_week`, and `hour` into model-usable formats.

### Imbalance dataset handling

- We have an imbalanced dataset with only 1000 rows. To address this imbalance, we can use either undersampling or oversampling techniques.
Undersampling reduces the number of samples from the majority class. While it helps balance the data, it also removes potentially valuable information, which can be harmful when working with a small dataset.

Oversampling, on the other hand, increases the number of samples in the minority class by duplicating existing samples or generating synthetic ones (e.g., using SMOTE).

✅ Conclusion:
Considering the small size of our dataset (1000 rows), oversampling is the ideal approach.

### 2. Exploratory Data Analysis (EDA)
- Class imbalance visualization.
- Correlation matrix to examine feature relationships.
- Trend analysis across days, hours, and transaction types.

### 3. Model Development
- Techniques to handle class imbalance (SMOTE, undersampling).
- Train and evaluate multiple models:
  - Logistic Regression (baseline)
  - Random Forest
  - XGBoost
  - LightGBM etc.
- Evaluation metrics:
  - Confusion Matrix
  - Precision, Recall, F1-Score
  - ROC-AUC

### Model Accuracy interpretation
---

**LightGBM:**
With an accuracy of 97.89%, LightGBM demonstrates **top-tier performance**, showing excellent balance between precision and recall for both classes. Its ROC AUC of 0.9969 and PR AUC of 0.9969 suggest it can **confidently separate and rank predictions**, making it the most effective model overall.

---

**Gradient Boosting:**
Scoring 96.69% accuracy and a ROC AUC of 0.9936, Gradient Boosting is nearly on par with LightGBM. Its recall and precision for both classes are consistently high, making it a **robust and reliable option** for classification tasks with balanced class importance.

---

**XGBoost:**
With an accuracy of 96.39%, XGBoost performs very well, especially in ranking predictions (ROC AUC 0.9941, PR AUC 0.9947). It offers slightly lower class 1 recall compared to LightGBM but remains a **strong and stable performer** in most use cases.

---

**CatBoost:**
Matching XGBoost in accuracy (97.29%) and F1-score, CatBoost delivers high-quality classification with minimal preprocessing, especially for datasets with categorical variables. Its ROC AUC of 0.9919 supports its role as a **top-tier, plug-and-play model**.

---

**Random Forest:**
Random Forest reaches 93.07% accuracy with a ROC AUC of 0.9834. It maintains strong class balance and generalization but doesn’t outperform gradient boosting models. It’s a **good balance between performance and interpretability**, especially for quicker training and less tuning.

---

**SVM (Optimized):**
At 91.57% accuracy, SVM provides good overall results, with **perfect precision for class 1** but lower recall (0.82), indicating it’s conservative in flagging positives. This makes it more suitable in situations where **false positives are more costly** than false negatives.

---

**Logistic Regression (Optimized):**
With 90.36% accuracy and ROC AUC of 0.9612, logistic regression offers solid, interpretable performance but underperforms compared to tree-based models. Class 1 recall (0.83) is relatively low, suggesting it's **best used as a baseline**.

---

**One-Class SVM:**
One-Class SVM achieves only 50.60% accuracy, with a ROC AUC of 0.5102—barely above random. It fails to distinguish between classes effectively and is **not suitable for supervised binary classification**.

---

**Isolation Forest:**
Scoring 49.70% accuracy and a ROC AUC of 0.5117, Isolation Forest is **not effective for this task**. Its poor precision and recall for class 0 further indicate it is **better suited for anomaly detection**, not standard classification.

---



### 4. Temporal Pattern Analysis
- Use `hour`, `day_of_week`, and `time_of_day` to uncover fraud trends over time.
- Detect repetitive fraudulent behavior during specific time windows.

### 5. Model Deployment
- Create a REST API using **flask** to serve the model.
- Accept transaction data in JSON and return:
  - `fraud_prediction` (0 or 1)
  - `confidence_score`
- Dockerize the service for portability.

### 6. Monitoring & Feedback
- Optional Streamlit dashboard for visualization.

---

## ⚙️ Tools & Technologies

| Layer | Tools |
|------|-------|
| Data Processing | Python, Pandas, NumPy |
| Machine Learning | Scikit-learn, XGBoost, LightGBM, Imbalanced-learn |
| API Development | Flask |
| Deployment | Docker |
| Visualization | Matplotlib, Seaborn, Streamlit (optional) |

---

## 📦 Deliverables

- ✅ Preprocessed dataset
- ✅ Trained and validated model
- ✅ Real-time fraud detection API (flask)
- ✅ Dockerfile for containerized deployment
- ✅ Optional Streamlit dashboard replace with jinja2 implementation
- ✅ Complete project documentation

---

## 📈 Success Metrics

| Metric | Target |
|--------|--------|
| **Recall** | ≥ 90% (catch more fraud cases) |
| **Precision** | ≥ 80% (reduce false positives) |
| **AUC-ROC** | ≥ 0.95 |
| **Inference Time** | < 500ms |
| **Explainability** | SHAP or feature importance visualization |

---

---

## 📁 Folder Structure (Suggested)

# 🚀 Getting Started (Local Development)

### 1. Clone the Repository

```bash
git clone https://github.com/nathphoenix/Fraud_model
cd fraud_model

Create a Virtual Environment
python -m venv venv or virtualenv fraud-env --python=python
source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install Dependencies
pip install -r requirements.txt
4. Run the Flask App
python app.py
Access the API at: http://localhost as it runs on port 80

🐳 Production Deployment with Docker + Nginx
📁 Dockerized Architecture
[Client] → [Nginx Reverse Proxy] → [Gunicorn WSGI Server] → [Flask App]
1. Build & Run with Docker Compose

docker-compose up --build

Nginx handles reverse proxy on port 80

App available at: http://localhost develop with html and jinja2 template
you can easily pass parameters from the csv data to the form data on the landing page

Application testing

endpoint = http://localhost/fraud_prediction

API Documentation and usage

https://.postman.co/workspace/My-Workspace~0e7b6522-756e-4404-8e59-18750fbd90d4/request/9827379-c436377c-b0a8-475b-82f9-101dcdd721a9?action=share&creator=9827379&ctx=documentation&active-environment=9827379-f4fcccdf-6d1e-4508-a212-c6da67f411d0

payload = {
  "transaction_amount": 20.54490849240048,
  "transaction_type": "ATM",
  "device_type": "Mobile",
  "location": "Abuja",
  "time_of_day": "Morning",
  "day_of_week": "Tue",
  "is_foreign_transaction": 1,
  "is_high_risk_country": 0,
  "previous_fraud_flag": 0,
  "label_code": 1,
  "transaction_time": "2024-01-29T14:00:00",
  "risk_score": 0.3629753030567228
}


response = {
    "Status": "Successful",
    "explanation": "Fraud detected: this transaction should be flagged and escalated for investigation.",
    "prediction": 1,
    "probability": 0.9996517479079001
}