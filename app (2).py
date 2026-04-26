import streamlit as st

# إعداد الصفحة
st.set_page_config(page_title="Graduation Project", layout="wide")

# العنوان (الاسم اللي طلبتيه)
st.markdown("<h2 style='text-align: center;'>إعداد المهندسة: ندى محسن</h2>", unsafe_allow_html=True)
st.write("---")

# تقسيم الشاشة لـ 4 أعمدة عشان البيانات تظهر كاملة
col1, col2, col3, col4 = st.columns(4)

with col4: # العمود اليمين (العمر والنشاط وسمكة الجلد)
    age = st.number_input("العمر", value=25)
    activity = st.number_input("النشاط البدني", value=1.00)
    skin = st.number_input("سمكة الجلد", value=20.00)

with col3: # العمود الثاني (BMI والجلوكوز وLDL)
    bmi = st.number_input("BMI مؤشر الكتلة", value=25.00)
    glucose = st.number_input("مستوى الجلوكوز", value=100.00)
    ldl = st.number_input("كوليسترول LDL", value=100.00)

with col2: # العمود الثالث (الضغط الانبساطي والكوليسترول والتدخين)
    diastolic = st.number_input("ضغط الدم الانبساطي", value=80.00)
    cholesterol = st.number_input("نسبة الكوليسترول", value=150.00)
    smoking = st.selectbox("التدخين (0 أو 1)", options=[0, 1])

with col1: # العمود الأخير (الضغط الانقباضي والأنسولين وA1c)
    systolic = st.number_input("ضغط الدم الانقباضي", value=120.00)
    insulin = st.number_input("الأنسولين", value=80.00)
    a1c = st.number_input("A1c الهيموجلوبين", value=5.50)

st.write("---")

# زر التحليل
if st.button("تحليل البيانات"):
    st.success("تم إدخال الـ 12 بيان بنجاح!")
