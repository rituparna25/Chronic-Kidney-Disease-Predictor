
# 🧬 Chronic Kidney Disease Prediction App

This is a machine learning project that predicts whether a patient is likely to have **Chronic Kidney Disease (CKD)** based on 24 clinical features. The model is trained on a medical dataset and deployed via a **Streamlit web app** for instant prediction.

## 📌 Project Overview

- **Model**: Random Forest Classifier (tuned for best accuracy)
- **Dataset**: Chronic Kidney Disease dataset from Kaggle
- **Accuracy**: 100% on test set, 98.75% in 5-fold cross-validation
- **Deployment**: Streamlit App

---

## 🩺 Features Used for Prediction

- Age, Blood Pressure, Blood Urea, Serum Creatinine, Sodium, Potassium, Hemoglobin, etc.
- Categorical health conditions: Red blood cells (normal/abnormal), diabetes, anemia, etc.
- All features are user-inputted from the Streamlit form UI

---

## 🛠️ Tech Stack

| Layer     | Technology             |
|-----------|------------------------|
| ML Model  | RandomForestClassifier |
| Backend   | Python (pickle + numpy + pandas) |
| Frontend  | Streamlit              |
| Data      | CSV from Kaggle        |

---

## 📁 Folder Structure

```
├── app.py                # Streamlit frontend
├── kidney_model.pkl      # Trained ML model (Random Forest)
├── kidney_disease.csv    # Dataset used for training
├── kidney_disease_code.ipynb  # Jupyter Notebook (EDA + Model Training)
├── requirements.txt      # Python dependencies
└── README.md             # Project overview and instructions
```

---

## ⚙️ How to Run Locally

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/Chronic-Kidney-Disease-Predictor.git
   cd Chronic-Kidney-Disease-Predictor
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the app:
   ```bash
   streamlit run app.py
   ```

---

## 📊 Model Performance

| Metric        | Score     |
|---------------|-----------|
| Accuracy      | 100%      |
| Precision     | 1.00      |
| Recall        | 1.00      |
| F1 Score      | 1.00      |
| CV Accuracy   | 98.75%    |

---

## 🙌 Acknowledgments

- **Heritage Institute of Technology, Kolkata** – for academic support and mentorship  
- **IALSD (Institute of Advanced Learning and Skill Development)** – for training and project opportunity  
- **Kaggle** – for providing the open-source CKD dataset

---

## 📚 Future Improvements

- Add SHAP explanations for predictions
- Store prediction logs in a database
- Convert to full-stack (Flask + React) for advanced deployment
- Enable file upload of patient records for batch prediction
---
