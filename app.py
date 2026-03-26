import streamlit as st
import qrcode
from io import BytesIO

# Cấu hình trang web
st.set_page_config(page_title="Trình Tạo Mã QR", page_icon="🌐")

st.title("🛠️ Trình Tạo Mã QR Miễn Phí")
st.write("Chào mừng bạn! Hãy nhập nội dung để tạo mã QR ngay lập tức.")

# Ô nhập dữ liệu
url = st.text_input("Nhập liên kết (URL) hoặc văn bản:", "https://google.com")

if url:
    # Tạo mã QR
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(url)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Chuyển đổi ảnh để hiển thị và tải về
    buf = BytesIO()
    img.save(buf, format="PNG")
    byte_im = buf.getvalue()
    
    # Hiển thị trên giao diện web
    st.image(byte_im, caption="Mã QR của bạn đã sẵn sàng!")
    
    # Nút tải về
    st.download_button(
        label="Tải ảnh QR về máy",
        data=byte_im,
        file_name="qrcode_cua_toan.png",
        mime="image/png"
    )