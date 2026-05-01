# 💳 Credit Card Fraud Detection System

🚀 An end-to-end Machine Learning project that detects fraudulent credit card transactions using advanced classification techniques, real-time API, explainable AI, and an interactive dashboard.

---

## 📌 Overview

Fraudulent transactions are a major problem in banking and fintech industries, leading to huge financial losses.

This project builds a **real-time fraud detection system** that:

* Identifies fraudulent transactions
* Handles highly imbalanced data
* Provides explainability using SHAP
* Deploys predictions via API
* Visualizes results in a dashboard

---

## 🎯 Objective

* Detect fraud transactions with high recall
* Handle imbalanced dataset effectively
* Build an industry-level ML pipeline
* Deploy model using FastAPI
* Create interactive dashboard using Streamlit

---

## 🧠 Tech Stack

**Languages & Libraries**

* Python
* Pandas, NumPy
* Scikit-learn
* XGBoost
* SMOTE (Imbalanced Data Handling)
* SHAP (Explainable AI)

**Deployment & UI**

* FastAPI (Real-time API)
* Streamlit (Dashboard)
* Plotly (Visualization)

---

## ⚙️ Features

* ✅ Fraud detection using XGBoost
* ✅ Handles imbalanced data using SMOTE
* ✅ Real-time API prediction
* ✅ Interactive dashboard
* ✅ SHAP explainability (feature importance)
* ✅ Transaction simulation (Kafka-style)

---

## 📂 Project Structure

```bash
Credit-Card-Fraud-Detection/
│── data/
│── models/
│   └── fraud_model.pkl
│── outputs/
│   ├── confusion_matrix.png
│   ├── shap_summary.png
│── src/
│   ├── api.py
│   ├── simulate.py
│── app/
│   └── dashboard.py
│── images/
│── main.py
│── requirements.txt
│── README.md
```

---

## ▶️ How to Run

### 1️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 2️⃣ Train Model

```bash
python main.py
```

### 3️⃣ Run FastAPI Server

```bash
uvicorn src.api:app --reload
```

👉 Open: http://127.0.0.1:8000/docs

---

### 4️⃣ Run Streamlit Dashboard

```bash
streamlit run app/dashboard.py
```

---

### 5️⃣ Run Simulation

```bash
python src/simulate.py
```

---

## 📊 Results

* Improved fraud detection using XGBoost
* Handled class imbalance with SMOTE
* Achieved strong recall (important for fraud detection)
* Generated explainable insights using SHAP

---

## 📸 Screenshots

### 📊 Confusion Matrix

![Confusion Matrix](outputs/confusion_matrix.png)

### 🧠 SHAP Feature Importance

![SHAP](outputs/shap_summary.png)

### 📊 Dashboard UI

![Dashboard](images/dashboard.png)

### ⚡ API Swagger

![API](images/api.png)

### 🔄 Simulation Output

![Simulation](images/simulation.png)

---

## 💼 Industry Relevance

This project simulates real-world fraud detection systems used in:

* Banking systems
* Payment gateways
* Fintech platforms
* E-commerce transactions

---

## 🎯 Learning Outcomes

* Handling imbalanced datasets
* Building ML pipelines
* Model evaluation (precision, recall)
* Explainable AI using SHAP
* API development with FastAPI
* Dashboard creation with Streamlit

---

## 🚀 Future Improvements

* Real-time Kafka streaming
* Deep Learning models
* Email/SMS fraud alerts
* Deployment on cloud (AWS/GCP)

---

## 👩‍💻 Author

**Sanskritika Awasthi**

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and connect with me!
