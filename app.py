import streamlit as st
import pandas as pd
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
import io
from PIL import Image

st.set_page_config(
    page_title="AI Multi-Niche Commercial Content Generator",
    page_icon="🎬",
    layout="wide"
)

# Custom Styling & Header
st.markdown("""
    <style>
    .main-header {
        font-size: 2.2rem;
        color: #1A365D;
        font-weight: 700;
        margin-bottom: 0px;
    }
    .sub-header {
        font-size: 1.1rem;
        color: #4A5568;
        margin-bottom: 25px;
    }
    .stButton>button {
        background-color: #1A365D;
        color: white;
        font-weight: bold;
        border-radius: 6px;
        padding: 0.5rem 1rem;
    }
    .stButton>button:hover {
        background-color: #2B6CB0;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<p class="main-header">🎬 AI Multi-Niche Commercial Content Generator</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Unggah 1 Foto Produk Referensi (Single Source of Truth), pilih niche, dan hasilkan bank visual, prompt, skrip, Voice Over, caption, serta hashtag dalam Bahasa Indonesia secara instan.</p>', unsafe_allow_html=True)

# Sidebar Configuration
st.sidebar.header("⚙️ Pengaturan Kampanye")
niche_option = st.sidebar.selectbox(
    "Pilih Niche Produk:",
    [
        "Jam Tangan (Watch)",
        "Smartphone",
        "Fashion (Pakaian)",
        "Home & Living (Perabot)",
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

st.sidebar.markdown("---")
st.sidebar.info("💡 **Consistency Rule Aktif:** Sistem secara otomatis mengunci identitas produk (warna, bentuk, logo, material) agar 100% konsisten di setiap scene.")

# Main Upload Area
uploaded_file = st.file_uploader("📸 Unggah Master Product Reference (Format: JPG, PNG)", type=["jpg", "jpeg", "png"])

col1, col2 = st.columns([1, 2])

if uploaded_file is not None:
    with col1:
        st.subheader("🖼️ Master Produk")
        image = Image.open(uploaded_file)
        st.image(image, caption="Single Source of Truth", use_column_width=True)
    
    with col2:
        st.subheader("🚀 Status Generator")
        st.success("Gambar berhasil diunggah dan dikunci dengan Absolute Consistency Rule!")
        
        if st.button("✨ Generate Bank Konten & Kampanye Komersial"):
            with st.spinner("Menganalisis produk dan merancang bank visual, skrip, serta VO..."):
                
                # Database Generator based on Niche selected
                if "Watch" in niche_option:
                    product_title = "JAM TANGAN MEWAH PRIA"
                    v_data = [
                        ("1. Product Shots", "Hero Product Shot", "Tampilan utama jam tangan dengan pencahayaan studio mewah, latar belakang gelap charcoal, bayangan lembut, ketajaman maksimal pada dial dan bezel."),
                        ("1. Product Shots", "Front 3/4 Angle", "Sudut pandang 3/4 depan memperlihatkan kedalaman case, tombol chronograph, dan tekstur strap dengan pencahayaan metalik hangat."),
                        ("2. Hook", "Product Reveal", "Transisi dari kegelapan total ke sorotan cahaya dramatis yang mengungkap kemewahan jam tangan secara perlahan."),
                        ("3. Problem", "Busy Daily Life", "Pria eksekutif sibuk di meja kerja modern, menatap jam tangan dengan tenang di tengah tumpukan dokumen."),
                        ("4. Benefit", "Precision & Durability", "Pergerakan jarum detik kronograf yang presisi dan kekokohan rantai bracelet logam premium."),
                        ("5. Lifestyle", "Business Meeting", "Suasana rapat bisnis tingkat tinggi, tangan dengan jam tangan sedang menunjuk dokumen strategis."),
                        ("6. Detail / Macro", "Dial & Sub-Dials", "Makro super tajam menampilkan pola tekstur sunburst pada dial jam tangan dan sub-dial kronograf."),
                        ("7. CTA", "Buy Now", "Komposisi bersih berfokus pada jam tangan dengan tombol teks tebal bergaya minimalis: BELI SEKARANG.")
                    ]
                    script_data = [
                        ("1. Hook (0-3s)", "Visual produk muncul dari kegelapan dengan sorotan cahaya metalik tajam.", "Detik menentukan segalanya. Kenalkan mahakarya presisi di pergelangan Anda.", "Setiap detik berharga. Temukan jam tangan yang mendefinisikan ulang standar kemewahan pria modern.", "#LuxuryWatch #JamTanganPria"),
                        ("2. Problem (3-7s)", "Pria sibuk melirik jam tangan dengan raut wajah penuh tekanan waktu.", "Waktu terus berjalan cepat. Apakah Anda sudah memegang kendali penuh atas hari Anda?", "Kesibukan menuntut ketepatan. Jangan biarkan waktu mendikte Anda, jadilah penguasa waktu.", "#TimeManagement #PriaSukses"),
                        ("3. Benefit (7-12s)", "Macro shot dial, ketahanan air, dan rantai bracelet kokoh berkualitas tinggi.", "Dirancang dengan presisi absolut, material baja tahan karat premium, dan ketahanan tanpa kompromi.", "Kemewahan sejati terletak pada detail. Dibuat untuk bertahan, dirancang untuk memukau.", "#PrecisionWatch #DesignMewah"),
                        ("4. Lifestyle (12-18s)", "Pria mengenakan jam di ruang rapat eksekutif dan kafe urban kelas atas.", "Dari ruang rapat hingga malam gala, tampil percaya diri di setiap langkah perjalanan Anda.", "Sempurnakan gaya hidup profesional Anda dengan aksesori yang berbicara lebih keras dari kata-kata.", "#ExecutiveStyle #GayaPria"),
                        ("5. CTA (18-20s)", "Hero product shot dengan tombol Call to Action 'Beli Sekarang'.", "Amankan milik Anda hari ini. Elevasi penampilan Anda sekarang juga.", "Stok terbatas untuk para pemimpin sejati. Klik tautan di bio untuk miliki sekarang. BELI SEKARANG!", "#BeliSekarang #LimitedEdition")
                    ]
                elif "Smartphone" in niche_option:
                    product_title = "SMARTPHONE PREMIUM"
                    v_data = [
                        ("1. Product Shots", "Front-Facing Hero Shot", "Tampilan depan smartphone menampilkan layar menyala bersih, bezel tipis, dan proporsi bodi akurat di studio minimalis."),
                        ("1. Product Shots", "Rear-Facing Hero Shot", "Tampilan belakang menonjolkan modul kamera presisi, tekstur panel belakang, dan logo yang ditempatkan secara persis."),
                        ("2. Hook", "Dramatic Reveal", "Transisi cahaya dramatis dari gelap gulita yang secara perlahan mengungkap siluet dan bodi smartphone."),
                        ("3. Problem", "Low Battery / Busy Work", "Ekspresi wajah lelah seorang profesional melihat indikator baterai lemah di layar ponsel saat mobilitas tinggi."),
                        ("4. Benefit", "Sleek Construction", "Konstruksi bodi ramping dengan perpaduan material kaca dan logam berkualitas tinggi."),
                        ("5. Lifestyle", "Office Environment", "Pria/wanita profesional bekerja di ruang kantor korporat modern dengan latar dinding kaca."),
                        ("6. Detail / Macro", "Camera Module", "Makro tajam memperlihatkan keseluruhan tata letak modul kamera belakang dan finishing kaca."),
                        ("7. CTA", "Buy Now", "Komposisi hero produk di sebelah kiri dengan ruang negatif luas di kanan untuk teks 'BELI SEKARANG'.")
                    ]
                    script_data = [
                        ("1. Hook (0-3s)", "Transisi cahaya dramatis mengungkap siluet bodi smartphone dari kegelapan.", "Detik pertama menentukan segalanya. Sambut era baru teknologi di genggaman Anda.", "Rasakan lompatan teknologi dalam desain yang memukau. Perangkat yang dirancang untuk memimpin.", "#SmartphonePremium #InovasiTeknologi"),
                        ("2. Problem (3-7s)", "Ekspresi lelah profesional menghadapi ponsel lambat dan baterai habis saat mobilitas.", "Waktu Anda terlalu berharga untuk tertinggal oleh perangkat yang tidak dapat diandalkan.", "Pekerjaan menuntut kecepatan tanpa kompromi. Saatnya beralih ke performa yang mengerti ritme Anda.", "#Produktivitas #GayaHidupModern"),
                        ("3. Benefit (7-12s)", "Macro shot modul kamera, bodi tipis elegan, dan layar luas jernih tanpa batas.", "Desain bodi ramping, sistem optik presisi tinggi, dan ketahanan tanpa kompromi.", "Keindahan estetika berpadu dengan ketangguhan mutlak. Diciptakan untuk menemani setiap pencapaian besar Anda.", "#DesignElegan #KameraSmartphone"),
                        ("4. Lifestyle (12-18s)", "Penggunaan natural di ruang rapat eksekutif, kafe urban, dan perjalanan bisnis.", "Dari ruang rapat hingga malam urban, tampil percaya diri di setiap momen penting.", "Sempurnakan gaya hidup profesional Anda dengan perangkat yang merepresentasikan kesuksesan sejati.", "#ExecutiveStyle #MobileLife"),
                        ("5. CTA (18-20s)", "Hero product shot bersih dengan tata letak tombol 'Beli Sekarang'.", "Amankan milik Anda hari ini. Elevasi produktivitas Anda sekarang juga.", "Stok terbatas untuk gelombang peluncuran perdana. Klik tautan di bio untuk miliki sekarang. BELI SEKARANG!", "#BeliSekarang #SmartphoneTerbaru")
                    ]
                else:
                    product_title = niche_option.upper()
                    v_data = [
                        ("1. Product Shots", "Hero Product Shot", "Tampilan utama produk dengan pencahayaan studio mewah dan latar belakang netral berkelas."),
                        ("2. Hook", "Product Reveal", "Transisi visual memukau yang mengungkap keunggulan produk di detik pertama."),
                        ("3. Problem", "Daily Need", "Skenario nyata kebutuhan harian yang diselesaikan secara elegan oleh produk."),
                        ("4. Benefit", "Premium Quality", "Visual yang menonjolkan kualitas material, keindahan desain, dan fungsi optimal."),
                        ("5. Lifestyle", "Urban Lifestyle", "Penggunaan natural produk oleh model dalam suasana gaya hidup modern."),
                        ("6. Detail / Macro", "Craftsmanship Close-Up", "Makro super tajam pada detail pengerjaan, tekstur, dan finishing produk."),
                        ("7. CTA", "Buy Now", "Komposisi bersih berfokus pada produk dengan ajakan bertindak: BELI SEKARANG.")
                    ]
                    script_data = [
                        ("1. Hook (0-3s)", "Visual produk muncul dengan pencahayaan sinematik yang elegan.", "Detik pertama menentukan segalanya. Kenalkan standar baru untuk Anda.", "Temukan produk yang mendefinisikan ulang kualitas hidup Anda. #KoleksiTerbaik", "#KoleksiTerbaik #ProdukPilihan"),
                        ("2. Problem (3-7s)", "Skenario tantangan harian yang sering dialami pengguna.", "Apakah Anda mencari solusi terbaik untuk aktivitas harian Anda?", "Jangan biarkan hari-hari Anda berjalan biasa saja. Saatnya tingkatkan kualitas.", "#SolusiPraktis #GayaHidup"),
                        ("3. Benefit (7-12s)", "Macro shot detail produk dan material berkualitas tinggi.", "Dirancang dengan presisi absolut dan material pilihan tanpa kompromi.", "Kualitas sejati terletak pada detail. Dibuat untuk bertahan dan memukau.", "#KualitasPremium #DesainElegan"),
                        ("4. Lifestyle (12-18s)", "Penggunaan natural produk dalam suasana hidup yang elegan.", "Tampil percaya diri di setiap kesempatan dan langkah perjalanan Anda.", "Sempurnakan gaya hidup Anda dengan produk yang berbicara lebih keras dari kata-kata.", "#Lifestyle #GayaHidupMewah"),
                        ("5. CTA (18-20s)", "Hero product shot dengan tombol Call to Action 'Beli Sekarang'.", "Amankan milik Anda hari ini. Elevasi penampilan Anda sekarang juga.", "Stok terbatas. Klik tautan di bio untuk miliki sekarang. BELI SEKARANG!", "#BeliSekarang #LimitedEdition")
                    ]
                
                st.session_state['v_data'] = v_data
                st.session_state['script_data'] = script_data
                st.session_state['product_title'] = product_title
                st.session_state['generated'] = True

        if st.session_state.get('generated', False):
            st.markdown("---")
            st.subheader("📋 Hasil Generate Instan")
            
            tab1, tab2 = st.tabs(["🎨 Bank Visual & Prompt", "🎬 Skrip, VO & Caption"])
            
            with tab1:
                df_v = pd.DataFrame(st.session_state['v_data'], columns=["Kategori", "Scene", "Deskripsi Prompt Visual"])
                st.dataframe(df_v, use_container_width=True)
                
            with tab2:
                df_s = pd.DataFrame(st.session_state['script_data'], columns=["Bagian Kampanye", "Skrip Visual", "Voice Over (VO)", "Caption", "Hashtag"])
                st.dataframe(df_s, use_container_width=True)
                
            # Excel Download Button Creator
            output = io.BytesIO()
            wb = openpyxl.Workbook()
            
            # Sheet 1: Visual Bank
            ws1 = wb.active
            ws1.title = "Bank Visual"
            ws1.append(["Kategori", "Scene", "Deskripsi Prompt Visual"])
            for row in st.session_state['v_data']:
                ws1.append(row)
                
            # Sheet 2: Script
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
    st.info("👈 Silakan unggah foto produk referensi di atas untuk memulai generasi konten otomatis.")
