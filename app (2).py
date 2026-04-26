import streamlit as st

# إعداد الصفحة لتكون بعرض الشاشة
st.set_page_config(page_title="Graduation Project", layout="wide")

# العنوان العلوي
st.markdown("<h2 style='text-align: center;'>إعداد المهندسة: ندى محسن</h2>", unsafe_allow_html=True)
st.write("---")

# تقسيم الصفحة لـ 4 أعمدة لتوزيع الـ 17 بيان
col1, col2, col3, col4 = st.columns(4)

with col4: # العمود الأول (يمين)
    age = st.number_input("العمر", value=25)
    activity = st.number_input("النشاط البدني", value=1.0)
    skin = st.number_input("سمكة الجلد", value=20.0)
    history = st.selectbox("تاريخ العائلة مع المرض", options=["لا يوجد", "يوجد"])
    alcohol = st.selectbox("تناول الكحول", options=["لا", "نعم"])

with col3: # العمود الثاني
    bmi = st.number_input("BMI مؤشر الكتلة", value=25.0)
    glucose = st.number_input("مستوى الجلوكوز", value=100.0)
    ldl = st.number_input("كوليسترول LDL", value=100.0)
    diet = st.selectbox("نظام غذائي صحي", options=["نعم", "لا"])
    sleep = st.number_input("ساعات النوم", value=7.0)

with col2: # العمود الثالث
    diastolic = st.number_input("ضغط الدم الانبساطي", value=80.0)
    cholesterol = st.number_input("نسبة الكوليسترول", value=150.0)
    smoking = st.selectbox("التدخين (0 أو 1)", options=[0, 1])
    stress = st.slider("مستوى التوتر", 1, 10, 5)

with col1: # العمود الرابع (يسار)
    systolic = st.number_input("ضغط الدم الانقباضي", value=120.0)
    insulin = st.number_input("الأنسولين", value=80.0)
    a1c = st.number_input("A1c الهيموجلوبين", value=5.5)

st.write("---")

# زر التحليل
if st.button("تحليل الـ 17 بيان"):
    st.success("تم استقبال كافة البيانات بنجاح!")
