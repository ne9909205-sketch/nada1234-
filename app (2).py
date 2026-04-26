import streamlit as st
import pandas as pd

# 1. إعدادات الصفحة
st.set_page_config(page_title="مشروع التخرج", layout="wide")

# 2. العنوان العلوي (تم تصحيح الخطأ هنا)
st.markdown("<h2 style='text-align: center;'>إعداد المهندسة: ندى محسن</h2>", unsafe_allow_html=True)
st.write("---")

# 3. تقسيم المدخلات إلى 4 أعمدة
col1, col2, col3, col4 = st.columns(4)

with col1:
    systolic = st.number_input("ضغط الدم الانقباضي", min_value=0.0, value=120.0)
    insulin = st.number_input("الأنسولين", min_value=0.0, value=80.0)
    a1c = st.number_input("A1c الهيموجلوبين", min_value=0.0, value=5.5)

with col2:
    diastolic = st.number_input("ضغط الدم الانبساطي", min_value=0.0, value=80.0)
    cholesterol = st.number_input("نسبة الكوليسترول", min_value=0.0, value=150.0)
    smoking = st.selectbox("التدخين (0 أو 1)", options=[0, 1])

with col3:
    bmi = st.number_input("مؤشر الكتلة BMI", min_value=0.0, value=25.0)
    glucose = st.number_input("مستوى الجلوكوز", min_value=0.0, value=100.0)
    ldl = st.number_input("LDL كوليسترول", min_value=0.0, value=100.0)

with col4:
    age = st.number_input("العمر", min_value=1, max_value=120, value=25)
    physical_activity = st.number_input("النشاط البدني", min_value=0.0, value=1.0)
    skin_thickness = st.number_input("سمكة الجلد", min_value=0.0, value=20.0)

st.write("---")

# 4. زر التنبؤ
if st.button("تحليل البيانات"):
    st.success("تم تشغيل الكود بنجاح!")
