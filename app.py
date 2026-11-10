import streamlit as st
import urllib.parse


st.title('🍯 مناحل الخليفة')
st.write('عسل طبيعي نقي 100% - اطلب كميتك مباشرة عبر الموقع')

st.divider()

# 1. قائمة أنواع العسل والأسعار
h_type = {
    'حبة بركة': 150_000,
    'حمضيات': 125_000,
    'جبلي': 150_000,
    'شوكيات': 175_000,
    'جيجان': 175_000
}

# القائمة المنسدلة لاختيار النوع أولاً
h = st.selectbox(
    'نوع العسل:',
    list(h_type.keys()),
    index=None,
    placeholder="اضغط هنا لاختيار نوع العسل..."
)

# 2. إدخال الكمية
n = st.number_input(
    'عدد الكيلوغرامات المطلوبة:',
    value=None,
    min_value=0.5,
    step=0.5,
    placeholder="أدخل الكمية (مثلاً: 1 أو 2.5)..."
)

st.divider()

# 3. التحقق المنطقي، الحساب، وزر الواتساب
if h is None:
    st.info("يرجى اختيار نوع العسل أولا")
elif n is None:
    st.info("يرجى إدخال الكمية المطلوبة.")
elif n > 10.0:
    st.error('''قيمة كبيرة !
يجب إدخال قيمة بين 0.5 و 10.0 كغ''')
else:
    # استخراج السعر وحساب الإجمالي
    mony = h_type[h]
    total = mony * n

    # عرض السعر النهائي بشكل بطاقة رقمية أنيقة
    st.metric(label="السعر النهائي", value=f"{int(total):,} ل.س")

    # رقم الهاتف المستلم
    phone_number = "96394105810"

    # نص الرسالة الجاهزة للطلب
    message = f"""السلام عليكم، أود طلب عسل من مناحل الخليفة:
- النوع: {h}
- الكمية: {n} كغ
- الإجمالي: {int(total):,} ليرة سورية"""

    # تجهيز الرابط المباشر
    encoded_message = urllib.parse.quote(message)
    whatsapp_url = f"https://wa.me/{phone_number}?text={encoded_message}"

    # زر الطلب
    st.link_button("📲 إرسال الطلب عبر واتساب", whatsapp_url)

    st.markdown(
        "ليس لديك واتساب؟ [اضغط هنا للاتصال برقم البائع](tel:+96394105810)"
    )
    import streamlit.components.v1 as components

    copy_box_html = """
    <div style="
        display: inline-flex;
        align-items: center;
        background-color: #FFF3D6;
        border: 1px solid #D4AF37;
        border-radius: 8px;
        padding: 4px 8px;
        font-family: sans-serif;
    ">
        <span style="font-size: 15px; font-weight: bold; color: #2B2118; margin-left: 10px; margin-right: 6px;">
            +96394105810
        </span>
        <button onclick="copyText()" style="
            background-color: #D4AF37;
            color: white;
            border: none;
            border-radius: 6px;
            padding: 5px 10px;
            cursor: pointer;
            font-size: 13px;
            font-weight: bold;
        ">📋 نسخ</button>
        <span id="done" style="display: none; color: green; font-size: 12px; margin-right: 6px;">تم! ✓</span>
    </div>

    <script>
    function copyText() {
        navigator.clipboard.writeText("+96394105810");
        var d = document.getElementById("done");
        d.style.display = "inline";
        setTimeout(function() { d.style.display = "none"; }, 2000);
    }
    </script>
    """

    st.write('رقم التواصل مع البائع:')
    components.html(copy_box_html, height=55)