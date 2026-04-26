import streamlit as st

# جعل الصفحة عريضة جداً لتناسب الـ 17 خانة
st.set_page_config(layout="wide", page_title="Diabetes Prediction System")

# تصميم العنوان باسمك الكامل
st.markdown("""
    <style>
    .main-title { font-size:35px !important; text-align: center; color: #1E88E5; font-weight: bold; }
    .sub-title { font-size:20px !important; text-align: center; color: #555; margin-bottom: 30px; }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<p class="main-title">نظام توقع مرض السكري</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">إعداد المهندسة: ندى محسن</p>', unsafe_allow_html=True)

st.divider()

# قائمة بـ 17 مدخلاً احترافياً لمشروع تخرجك
features = [
    "عمر المريض", "BMI مؤشر الكتلة", "ضغط الدم الانقباضي", "ضغط الدم الانبساطي", 
    "عدد مرات الحمل", "مستوى الجلوكوز", "نسبة الكوليسترول", "الأنسولين", 
    "تاريخ العائلة", "النشاط البدني", "التدخين (0 أو 1)", "الهيموجلوبين A1c", 
    "الدهون الثلاثية", "كوليسترول LDL", "كوليسترول HDL", "سماكة الجلد", "معدل ضربات القلب"
]

# تقسيم المدخلات على 4 أعمدة لتنظيم الـ 17 خانة
cols = st.columns(4)
user_inputs = []

for i, feature in enumerate(features):
    with cols[i % 4]:
        val = st.number_input(f"{feature}", value=0.0, step=0.1, key=f"input_{i}")
        user_inputs.append(val)

st.divider()

# زر التحليل النهائي
if st.button("تحليل كافة النتائج"):
    st.balloons()
    st.success(f"تم استقبال كافة النتائج الـ 17 بنجاح. بالتوفيق في مشروع التخرج يا بشمهندسة ندى!")
