import streamlit as st
import pandas as pd

# إعدادات الصفحة
st.set_page_config(page_title="مشروع التخرج - المهندسة ندى محسن", layout="wide")

# العنوان العلوي
st.markdown("<h2 style='text-align: center;'>إعداد المهندسة: ندى محسن</h2>", unsafe_allow_config=True)
st.write("---")

# تقسيم المدخلات إلى أعمدة لتفادي تراكمها بشكل رأسي
col1, col2, col3, col4 = st.columns(4)

with col1:
    systolic = st.number_input("ضغط الدم الانقباضي", min_value=0.0, value=120.0, step=1.0)
    insulin = st.number_input("الأنسولين", min_value=0.0, value=80.0, step=1.0)
    a1c = st.number_input("A1c الهيموجلوبين", min_value=0.0, value=5.5, step=0.1)
    skin_thickness = st.number_input("سمكة الجلد", min_value=0.0, value=20.0, step=1.0)

with col2:
    diastolic = st.number_input("ضغط الدم الانبساطي", min_value=0.0, value=80.0, step=1.0)
    cholesterol = st.number_input("نسبة الكوليسترول", min_value=0.0, value=150.0, step=1.0)
    smoking = st.selectbox("التدخين (0 أو 1)", options=[0, 1])
    hdl = st.number_input("HDL كوليسترول", min_value=0.0, value=50.0, step=1.0)

with col3:
    bmi = st.number_input("مؤشر الكتلة BMI", min_value=0.0, value=25.0, step=0.1)
    glucose = st.number_input("مستوى الجلوكوز", min_value=0.0, value=100.0, step=1.0)
    physical_activity = st.number_input("النشاط البدني", min_value=0.0, value=1.0, step=1.0)
    ldl = st.number_input("LDL كوليسترول", min_value=0.0, value=100.0, step=1.0)

with col4:
    age = st.number_input("العمر", min_value=1, max_value=120, value=25)
    pregnancies = st.number_input("عدد مرات الحمل", min_value=0, value=0)
    # أضيفي أي حقول أخرى هنا

st.write("---")

# زر التنبؤ (Prediction)
if st.button("تحليل البيانات وتوقع النتيجة"):
    # هنا يتم ترتيب البيانات بنفس ترتيب أعمدة الموديل الخاص بكِ
    input_data = [[age, systolic, diastolic, bmi, glucose, insulin, a1c, cholesterol]] 
    
    # مثال لعرض النتيجة (قومي بربطها بموديل الـ ML الخاص بكِ هنا)
    st.success("تم استلام البيانات بنجاح. جاري المعالجة...")
    
    # استعراض البيانات المدخلة في جدول للتأكد
    df_show = pd.DataFrame(input_data, columns=['العمر', 'الانقباضي', 'الانبساطي', 'BMI', 'الجلوكوز', 'الأنسولين', 'A1c', 'الكوليسترول'])
    st.table(df_show)
