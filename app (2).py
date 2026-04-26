import streamlit as st

# إعداد الصفحة
st.set_page_config(page_title="نظام تنبؤ بمرض السكري", layout="wide")

# الخانة الرئيسية للعنوان
st.markdown("""
    <div style="background-color:#f8f9fa; padding:25px; border-radius:15px; border: 3px solid #2e7d32; margin-bottom: 25px;">
        <h1 style="text-align: center; color: #1b5e20; margin:0;">نظام تنبؤ بمرض السكري</h1>
        <h3 style="text-align: center; color: #388e3c; margin-top:10px;">إعداد المهندسة: ندى محسن</h3>
    </div>
    """, unsafe_allow_html=True)

# تقسيم الصفحة لـ 4 أعمدة
col1, col2, col3, col4 = st.columns(4)

with col4:
    age = st.number_input("العمر", value=25)
    activity = st.number_input("النشاط البدني", value=1.0)
    skin = st.number_input("سمكة الجلد", value=20.0)
    family_history = st.selectbox("تاريخ العائلة مع المرض", options=["لا يوجد", "يوجد"])
    alcohol = st.selectbox("تناول الكحول", options=["لا", "نعم"])

with col3:
    bmi = st.number_input("BMI مؤشر الكتلة", value=25.0)
    glucose = st.number_input("مستوى الجلوكوز", value=100.0)
    ldl = st.number_input("كوليسترول LDL", value=100.0)
    diet = st.selectbox("نظام غذائي صحي", options=["نعم", "لا"])
    sleep = st.number_input("ساعات النوم", value=7.0)

with col2:
    diastolic = st.number_input("ضغط الدم الانبساطي", value=80.0)
    cholesterol = st.number_input("نسبة الكوليسترول", value=150.0)
    smoking = st.selectbox("التدخين (0 أو 1)", options=[0, 1])
    # التعديل هنا: تم تغيير slider إلى number_input ليصبح مثل البقية
    stress = st.number_input("مستوى التوتر", min_value=1, max_value=10, value=5)

with col1:
    systolic = st.number_input("ضغط الدم الانقباضي", value=120.0)
    insulin = st.number_input("الأنسولين", value=80.0)
    a1c = st.number_input("A1c الهيموجلوبين", value=5.5)

st.write("---")

if st.button("تحليل البيانات والتنبؤ"):
    st.success("تم استقبال الـ 17 بيان بنجاح وبشكل متناسق!")
