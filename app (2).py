import streamlit as st
import pandas as pd
import joblib

# 1. تحميل النموذج والـ Scaler
model = joblib.load('diabetes_model.pkl')
scaler = joblib.load('scaler.pkl')

st.title("نظام الكشف المبكر عن السكري")
st.write("أدخل بيانات المريض للتنبؤ بنسبة الخطورة")

# 2. إنشاء خانات لإدخال البيانات (أمثلة بناءً على ملفك)
age = st.number_input("العمر", min_value=1, max_value=120)
gender = st.selectbox("الجنس", options=[0, 1]) # 0 للأنثى و 1 للذكر مثلاً
hb1ac = st.number_input("مستوى HbA1c")

# 3. زر التوقع
if st.button("تحليل النتيجة"):
    # تجهيز البيانات المدخلة في مصفوفة
    input_data = [[age, gender, hb1ac]] # أضيفي باقي الأعمدة هنا بنفس ترتيب التدريب
    
    # توحيد المقاسات (Scaling)
    input_scaled = scaler.transform(input_data)
    
    # التوقع
    prediction = model.predict(input_scaled)
    
    if prediction[0] == 1:
        st.error("النتيجة: خطورة عالية للإصابة بالسكري")
    else:
        st.success("النتيجة: خطورة منخفضة")