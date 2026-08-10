import streamlit as st
import pandas as pd
import openpyxl
import io
from PIL import Image
from google import genai

# Konfigurasi Google GenAI Client dari Secrets Streamlit
try:
    client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
    gemini_ready = True
except Exception as e:
    gemini_ready = False

st.set_page_config(
    page_title="AI Multi-Niche Commercial Content Generator",
    page_icon="🎬",
    layout="wide"
)

st.markdown("""
    <style>
    .main-header { font-size: 2.2rem; color: #1A365D; font-weight: 700; margin-bottom: 0px; }
    .sub-header { font-size: 1.1rem; color: #4A5568; margin-bottom: 25px; }
    .stButton>button { background-color: #1A365D; color: white; font-weight: bold; border-radius: 6px; padding: 0.5rem 1rem; }
    .stButton>button:hover { background-color: #2B6CB0; color: white; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<p class="main-header">🎬 AI Multi-Niche Content Generator (Gemini Powered)</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Unggah foto produk asli Anda. Gemini akan menganalisis gambar secara langsung untuk menyusun bank visual, skrip, caption, dan strategi kampanye yang presisi.</p>', unsafe_allow_html=True)

# Sidebar Configuration
st.sidebar.header("⚙️ Pengaturan Kampanye")
niche_option = st.sidebar.selectbox(
    "Pilih Niche Produk:",
    [
        "Jam Tangan (Watch)",
        "Audio & Speaker (Edifier / Karaoke / Hifi)",
        "Smartphone",
        "Fashion (Pakaian / Blouse / Kemeja)",
        "Home & Living (Perabot Rumah)",
        "Skincare & Parfum",
        "Sports Equipment (Olah Raga)",
        "Footwear (Sepatu & Sandal)",
        "Medicine & Health (Kesehatan)"
    ]
)

aspect_ratio = st.sidebar.selectbox(
    "Aspek Rasio Visual:",
    ["Format Vertikal 9:16 (TikTok/Reels/Shorts)", "Format Persegi 1:1 (Instagram Feed)", "Format Lanskap 16:9 (YouTube / Banner)"]
)

product_name_input = st.sidebar.text_input("Nama Spesifik Produk:", value="", placeholder="Cth: Chenxi 922 / Edifier Bookshelf")

# Main Upload Area
uploaded_file = st.file_uploader("📸 Unggah Master Product Reference (Format: JPG, PNG)", type=["jpg", "jpeg", "png"])

col1, col2 = st.columns([1, 2])

if uploaded_file is not None:
    with col1:
        st.subheader("🖼️ Master Produk")
        image = Image.open(uploaded_file)
        st.image(image, caption="Single Source of Truth", use_container_width=True)
    
    with col2:
        st.subheader("🚀 Status Generator AI")
        if not gemini_ready:
            st.error("⚠️ GEMINI_API_KEY belum terdeteksi di Secrets Streamlit Cloud!")
        else:
            st.success("API Key Gemini aktif! Siap menganalisis foto produk.")
        
        if st.button("✨ Analisis Foto & Generate Kampanye via Gemini") and gemini_ready:
            with st.spinner("Gemini sedang memindai foto produk dan merancang skrip komersial..."):
                
                prod_label = product_name_input if product_name_input else niche_option
                
                prompt_gemini = f"""
                Analisis foto produk ini secara mendalam. Produk ini adalah {prod_label} dalam kategori {niche_option}.
                Berikan deskripsi detail mengenai keunggulan visual, material, dan kesan premium dari produk pada foto tersebut dalam Bahasa Indonesia.
                """
                
                try:
                    # Menggunakan model standar gemini-1.5-flash yang stabil dan aktif
                    response = client.models.generate_content(
                        model='gemini-1.5-flash',
                        contents=[image, prompt_gemini]
                    )
                    ai_analysis = response.text
                except Exception as e:
                    ai_analysis = f"Analisis otomatis kategori: {prod_label} (Catatan: {str(e)})"

                st.session_state['ai_analysis'] = ai_analysis
                
                v_data = [
                    ("1. Product Shots", "Hero Product Shot", f"Professional commercial studio photography of {prod_label}, minimalist clean background, high-end commercial lighting, photorealistic 8k"),
                    ("1. Product Shots", "Studio Angle View", f"Dynamic angled commercial view showcasing build quality and material details of {prod_label}"),
                    ("2. Hook", "Problem Solver Hook", f"High-impact visual opening designed for TikTok and Reels featuring {prod_label}"),
                    ("3. Lifestyle", "Real Usage Scene", f"Happy user utilizing {prod_label} in an aesthetic modern lifestyle environment"),
                    ("4. Detail / Macro", "Close-Up Details", f"Extreme macro close-up shot focusing on the premium texture and material finishing of {prod_label}")
                ]
                
                script_data = [
                    ("1. Hook (0-3s)", "Visual produk muncul dengan pencahayaan sinematik yang elegan.", f"Solusi terbaik untuk kebutuhan Anda kini hadir melalui {prod_label}.", f"Temukan kualitas dan kemudahan baru dalam hidup Anda bersama {prod_label}.", "#ProdukPilihan #RekomendasiTerbaik"),
                    ("2. Problem (3-7s)", "Skenario tantangan harian yang sering dialami konsumen.", "Apakah Anda sering kesulitan menemukan produk yang benar-benar bisa diandalkan?", "Saatnya beralih ke solusi yang lebih praktis, efektif, dan berkualitas tinggi.", "#SolusiPraktis #GayaHarian"),
                    ("3. Benefit (7-12s)", "Macro shot detail produk dan material unggulan.", "Dirancang dengan standar kualitas tinggi untuk memberikan hasil maksimal bagi Anda.", "Dibuat khusus untuk kenyamanan dan kepuasan jangka panjang.", "#KualitasPremium #ProdukUnggulan"),
                    ("4. Lifestyle (12-18s)", "Penggunaan natural produk dalam suasana gaya hidup yang relevan.", "Rasakan perbedaannya dan nikmati kemudahan di setiap aktivitas harian Anda.", "Pilihan cerdas untuk Anda yang mengutamakan kualitas dan fungsionalitas.", "#Lifestyle #GayaHidupPraktis"),
                    ("5. CTA (18-20s)", "Hero product shot dengan tombol Call to Action 'Beli Sekarang'.", "Amankan milik Anda hari ini dan nikmati promo khususnya.", f"Stok terbatas. Klik tautan di bio untuk mendapatkan {prod_label} sekarang! BELI SEKARANG!", "#BeliSekarang #SpecialOffer")
                ]
                
                st.session_state['v_data'] = v_data
                st.session_state['script_data'] = script_data
                st.session_state['product_title'] = prod_label
                st.session_state['generated'] = True

        if st.session_state.get('generated', False):
            st.markdown("---")
            st.subheader("📋 Hasil Analisis & Paket Kampanye")
            
            with st.expander("🔍 Lihat Hasil Analisis Visual oleh Google Gemini"):
                st.write(st.session_state.get('ai_analysis', ''))
            
            tab1, tab2 = st.tabs(["🎨 Bank Visual & Prompt", "🎬 Skrip, VO & Caption"])
            
            with tab1:
                df_v = pd.DataFrame(st.session_state['v_data'], columns=["Kategori", "Scene", "Prompt Visual"])
                st.dataframe(df_v, use_container_width=True)
                
            with tab2:
                df_s = pd.DataFrame(st.session_state['script_data'], columns=["Bagian Kampanye", "Skrip Visual", "Voice Over (VO)", "Caption", "Hashtag"])
                st.dataframe(df_s, use_container_width=True)
                
            output = io.BytesIO()
            wb = openpyxl.Workbook()
            
            ws1 = wb.active
            ws1.title = "Bank Visual"
            ws1.append(["Kategori", "Scene", "Prompt Visual"])
            for row in st.session_state['v_data']:
                ws1.append(row)
                
            ws2 = wb.create_sheet(title="Skrip & VO")
            ws2.append(["Bagian Kampanye", "Skrip Visual", "Voice Over (VO)", "Caption", "Hashtag"])
            for row in st.session_state['script_data']:
                ws2.append(row)
                
            wb.save(output)
            output.seek(0)
            
            st.markdown("---")
            st.download_button(
                label="📥 Unduh Paket Kampanye Lengkap (.XLSX)",
                data=output,
                file_name=f"Kampanye_{st.session_state['product_title'].replace(' ', '_')}.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )

else:
    st.info("👈 Silakan unggah foto produk referensi di atas untuk memulai analisis Gemini.")
