import streamlit as st

# عنوان التطبيق كما في الصورة
st.markdown("<h2 style='text-align: right;'>نظام توقع مرض السكري</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: right;'>إعداد: المهندسة ندى</p>", unsafe_allow_html=True)

# تقسيم الشاشة إلى عمودين لتنظيم الحقول كما في الصورة
col1, col2 = st.columns(2)

with col1:
    # حقل نسبة الكوليسترول (رقم صحيح)
    cholesterol = st.number_input("نسبة الكوليسترول", min_value=0, value=0, step=1)
    
    # حقل النشاط البدني
    physical_activity = st.number_input("النشاط البدني", min_value=0, value=0, step=1)
    
    # حقل التدخين (قائمة اختيار لضمان إدخال 0 أو 1)
    smoking = st.selectbox("التدخين (0 أو 1)", options=[0, 1], help="0 لغير المدخن، 1 للمدخن")

with col2:
    # حقل BMI (يسمح بكسور عشرية)
    bmi = st.number_input("BMI مؤشر الكتلة", min_value=0.0, value=0.0, step=0.1, format="%.2f")
    
    # حقل تاريخ العائلة
    family_history = st.number_input("تاريخ العائلة", min_value=0.0, value=0.0, step=0.1)
    
    # حقل عدد مرات الحمل
    pregnancies = st.number_input("عدد مرات الحمل", min_value=0, value=0, step=1)

# زر التوقع
if st.button("تحليل النتيجة"):
    st.success("تم استقبال البيانات بنجاح جاري التحليل...")
