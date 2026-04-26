import streamlit as st

# 1. إعداد الصفحة لتكون بعرض الشاشة
st.set_page_config(page_title="نظام تنبؤ بمرض السكري", layout="wide")

# 2. العنوان الرئيسي في خانة بارزة (نظام تنبؤ بمرض السكري بإعداد المهندسة ندى محسن)
st.markdown("""
    <div style="background-color:#f0f2f6; padding:20px; border-radius:10px; border: 2px solid #464e5f;">
        <h1 style="text-align: center; color: #1f3044; margin:0;">نظام تنبؤ بمرض السكري</h1>
        <h3 style="text-align: center; color: #464e5f; margin-top:10px;">إعداد المهندسة: ندى محسن</h3>
    </div>
    """, unsafe_allow_html=True)

st.write("---")

# 3. توزيع الـ 17 خانة على 4 أعمدة عشان الشكل يبقى احترافي
col1, col2, col3, col4 = st.columns(4)

with col4: # العمود الأول (يمين)
    f1 = st.number_input("العمر", value=25)
    f2 = st.number_input("النشاط البدني", value=1.0)
    f3 = st.number_input("سمكة الجلد", value=20.0)
    f4 = st.number_input("عدد مرات الحمل", value=0)
    f5 = st.number_input("محيط الخصر", value=80.0)

with col3: # العمود الثاني
    f6 = st.number_input("BMI مؤشر الكتلة", value=25.0)
    f7 = st.number_input("مستوى الجلوكوز", value=100.0)
    f8 = st.number_input("كوليسترول LDL", value=100.0)
    f9 = st.number_input("كوليسترول HDL", value=50.0)
    f10 = st.number_input("الدهون الثلاثية", value=150.0)

with col2: # العمود الثالث
    f11 = st.number_input("ضغط الدم الانبساطي", value=80.0)
    f12 = st.number_input("نسبة الكوليسترول", value=150.0)
    f13 = st.selectbox("التدخين (0 أو 1)", options=[0, 1])
    f14 = st.selectbox("تاريخ العائلة (0 أو 1)", options=[0, 1])

with
