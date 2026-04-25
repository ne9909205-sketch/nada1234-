import streamlit as st
import joblib
import os
import numpy as np

# إعدادات الصفحة واسمك
st.set_page_config(page_title="مشروع التخرج - ندى محسن", layout="wide")

# 1. تحميل الموديل
base_path = os.path.dirname(__file__)
model_name = 'diabetes_model (3) (1).pkl'
model_path = os.path.join(base_path, model_name)

try:
    model = joblib.load(model_path)
    st.success("✅ تم تحميل الموديل بنجاح | إعداد: ندى محسن")
except Exception as e:
    st.error(f"خطأ في التحميل: {e}")
    st.stop()

# 2. العنوان واسمك في الواجهة
st.title("🩺 نظام توقع مرض السكري")
st.markdown(f"### إعداد الطالبة: **ندى محسن**")
st.write("---")

st.subheader("الرجاء إدخال الـ 17 بيان المطلوبة:")

# 3. تقسيم المدخلات لـ 17 عمود (مقسمة على صفوف عشان الشكل يكون منظم)
col1, col2, col3, col4 = st.columns(4)

with col1:
    v1 = st.number_input("العمر", value=0)
    v2 = st.number_input("الجلوكوز", value=0)
    v3 = st.number_input("ضغط الدم", value=0)
    v4 = st.number_input("سمك الجلد", value=0)
    v5 = st.number_input("الأنسولين", value=0)

with col2:
    v6 = st.number_input("مؤشر الكتلة BMI", value=0.0)
    v7 = st.number_input("تاريخ العائلة", value=0.0)
    v8 = st.number_input("عدد مرات الحمل", value=0)
    v9 = st.number_input("الطول (سم)", value=0)
    v10 = st.number_input("الوزن (كجم)", value=0)

with col3:
    v11 = st.number_input("نسبة الكوليسترول", value=0)
    v12 = st.number_input("النشاط البدني", value=0)
    v13 = st.number_input("التدخين (0 أو 1)", value=0)
    v14 = st.number_input("نظام الأكل", value=0)
    v15 = st.number_input("مستوى التعليم", value=0)

with col4:
    v16 = st.number_input("الدخل السنوي", value=0)
    v17 = st.number_input("الحالة الصحية العامة", value=0)

st.write("---")

# 4. زر التوقع
if st.button("تحليل النتائج الآن"):
    # تجميع الـ 17 مدخل في مصفوفة واحدة
    features = np.array([[v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, v15, v16, v17]])
    
    prediction = model.predict(features)
    
    st.subheader("النتيجة النهائية:")
    if prediction[0] == 1:
        st.error("⚠️ النتيجة: تشير البيانات إلى احتمالية عالية للإصابة بالسكر.")
    else:
        st.success("✅ النتيجة: تشير البيانات إلى أن الشخص سليم، حافظ على صحتك!")

# تذييل الصفحة
st.markdown("---")
st.caption("تم تطوير هذا النظام كجزء من مشروع تخرج الطالبة ندى محسن © 2026")
