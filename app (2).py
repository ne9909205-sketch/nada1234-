import streamlit as st
import joblib
import os
import numpy as np

# 1. تحديد مسار الموديل بشكل ديناميكي (عشان يشتغل على السيرفر صح)
base_path = os.path.dirname(__file__)
model_path = os.path.join(base_path, 'diabetes_model.pkl')

# 2. تحميل الموديل مع التأكد من وجوده
if os.path.exists(model_path):
    model = joblib.load(model_path)
else:
    st.error(f"ملف الموديل 'diabetes_model.pkl' مش موجود في الفولدر الرئيسي على GitHub. ارفعه وهتتحل المشكلة!")
    st.stop()

# 3. واجهة المستخدم (تعديل بسيط لشكل الأبلكيشن)
st.title("Diabetes Prediction App")
st.write("أدخل البيانات المطلوبة للتوقع:")

# هنا ضيف المدخلات بتاعتك (مثال)
# glucose = st.number_input("Glucose")
# bmi = st.number_input("BMI")
# age = st.number_input("Age")

# if st.button("Predict"):
#     prediction = model.predict([[glucose, bmi, age]])
#     st.success(f"النتيجة: {prediction[0]}")
