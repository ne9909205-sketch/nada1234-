import streamlit as st

# 1. إعداد الصفحة لتكون بعرض الشاشة
st.set_page_config(page_title="نظام تنبؤ بمرض السكري", layout="wide")

# 2. الخانة الرئيسية للعنوان
st.markdown("""
    <div style="background-color:#f8f9fa; padding:25px; border-radius:15px; border: 3px solid #2e7d32; margin-bottom: 25px;">
        <h1 style="text-align: center; color: #1b5e20; margin:0;">نظام تنبؤ بمرض السكري</h1>
        <h3 style="text-align: center; color: #388e3c; margin-top:10px;">إعداد المهندسة: ندى محسن</h3>
    </div>
    """, unsafe_allow_html=True)

# 3. توزيع الـ 17 خانة على 4 أعمدة (لتجنب أخطاء السطور)
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
    stress = st.slider("مستوى التوتر", 1, 10, 5)

with col1:
    systolic = st.number_input("ضغط الدم الانقباضي", value=120.0)
    insulin = st.number_input("الأنسولين", value=80.0)
    a1c = st.number_input("A1c الهيموجلوبين", value=5.5)

st.write("---")

# 4. زر التنبؤ النهائي
if st.button("تحليل البيانات والتنبؤ"):
    # جمع البيانات للتأكد من اكتمال الـ 17 بيان
    total_inputs = [age, activity, skin, family_history, alcohol, bmi, glucose, ldl, diet, sleep, diastolic, cholesterol, smoking, stress, systolic, insulin, a1c]
    st.success(f"تم بنجاح استقبال الـ {len(total_inputs)} بيان. النظام جاهز للتنبؤ.")
