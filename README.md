
# 🏡 House Price Prediction

A regression project to predict house prices using various machine learning models like Linear Regression, Random Forest, and XGBoost based on the [Kaggle House Prices dataset](https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques).

---

## 📂 Project Structure

```
house-price-prediction/
│
├── data/           # contains train.csv, test.csv
├── notebooks/      # Jupyter notebook for training and EDA
├── models/         # saved model (.pkl), train_columns
├── images/         # visualizations
├── main.py         # script to load model and predict
├── requirements.txt
└── README.md
```

---

## 🚀 Models Used

| Model              | MAE      | RMSE     | R²    |
|-------------------|----------|----------|-------|
| Linear Regression | 24,351   | 34,012   | 0.81  |
| Random Forest     | 18,921   | 28,345   | 0.89  |


✅ **Best performing model:**  Random Forest

---

## 🛠️ How to Run

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Run prediction script

```bash
python main.py
```

> Make sure you have `best_model.pkl` and `train_columns.pkl` inside the `models/` folder.

---

## 📦 Requirements

- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn

---

## 🧠 Future Work

- Feature engineering
- Model tuning (GridSearchCV)
- Streamlit web app for user input

---
