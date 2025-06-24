import pickle
import pandas as pd

# تحميل النموذج
with open('models/best_model.pkl', 'rb') as f:
    model = pickle.load(f)

# تحميل البيانات
df = pd.read_csv('data/test.csv')

# تنظيف الصف الأول من missing values
sample = df.dropna().iloc[0:1]

# تحويل categorical لـ one-hot
sample_encoded = pd.get_dummies(sample)

# تحميل train columns عشان نطابق الأعمدة
with open('models/train_columns.pkl', 'rb') as f:
    train_columns = pickle.load(f)

# إعادة ترتيب الأعمدة ونملأ أي نقص بـ 0
sample_encoded = sample_encoded.reindex(columns=train_columns, fill_value=0)

# التنبؤ
prediction = model.predict(sample_encoded)
print(f"Predicted Sale Price: ${prediction[0]:,.2f}")
