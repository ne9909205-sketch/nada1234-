import streamlit as st
import joblib
import os
import numpy as np

# 1. تحديد المسار البرمجي للمجلد الحالي
base_path = os.path.dirname(__file__)

# 2. اسم الملف بالظبط كما ظهر في الصورة (بالأقواس والأرقام)
# ملحوظة: لو غيرت اسم الملف على جيت هاب لـ diabetes_model.pkl لازم تغير الاسم هنا كمان
model_name = 'diabetes_model (3) (1).pkl'
model_path = os.path.join(base_path, model_name)

# 3. محاولة تحميل الموديل
try:
    if os.path.exists(model_path):
        model = joblib.load(model_path)
        st.success("✅ تم تحميل الموديل بنجاح!")
    else:
        st.error(f"❌ ملف الموديل غير موجود بالاسم ده: {model_name}")
        st.info("تأكد من رفع الملف بنفس الاسم بالظبط على GitHub")
        st.stop()
except Exception as e:
    st.error(f"حدث خطأ أثناء تحميل الموديل: {e}")
    st.stop()

# 4. واجهة التطبيق
st.title("نظام توقع مرض السكري")
st.write("قم بإدخال البيانات المطلوبة للحصول على التوقع")

# مثال لمدخلات (
