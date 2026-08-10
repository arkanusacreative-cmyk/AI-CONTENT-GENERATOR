import streamlit as st
import pandas as pd
import openpyxl
import io
from PIL import Image

st.set_page_config(
    page_title="AI Multi-Niche Commercial Content Generator",
    page_icon="🎬",
    layout="wide"
)

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
st.markdown('<p class="sub-header">Unggah 1 Foto Produk Referensi (Single Source of Truth), pilih niche, dan hasilkan bank visual, prompt, skrip, Voice Over, caption, serta hashtag yang relevan secara instan.</p>', unsafe_allow_html=True)

# Sidebar Configuration
st.sidebar.header("⚙️ Pengaturan Kampanye")
niche_option = st.sidebar.selectbox(
    "Pilih Niche Produk:",
    [
        "Jam Tangan (Watch)",
        "Smartphone",
        "Fashion (Pakaian / Blouse / Kemeja)",
        "Home & Living (Perabot / Speaker)",
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

product_name_input = st.sidebar.text_input("Nama Spesifik Produk (Opsional):", value="", placeholder="Cth: ROBOT RB650 / Kopi PRABU / Vioni Set")

st.sidebar.markdown("---")
st.sidebar.info("💡 **Dinamis & Spesifik:** Konten, skrip, VO, dan hashtag akan disesuaikan otomatis dengan kategori dan produk pilihan Anda.")

# Main Upload Area
uploaded_file = st.file_uploader("📸 Unggah Master Product Reference (Format: JPG, PNG)", type=["jpg", "jpeg", "png"])

col1, col2 = st.columns([1, 2])

if uploaded_file is not None:
    with col1:
        st.subheader("🖼️ Master Produk")
        image = Image.open(uploaded_file)
        st.image(image, caption="Single Source of Truth", use_container_width=True)
    
    with col2:
        st.subheader("🚀 Status Generator")
        st.success("Gambar berhasil diunci untuk menjaga konsistensi visual produk!")
        
        if st.button("✨ Generate Bank Konten & Kampanye Komersial"):
            with st.spinner("Merancang bank visual, skrip spesifik produk, VO, dan hashtag..."):
                
                prod_label = product_name_input if product_name_input else niche_option
                
                # Dynamic Database Generator based on Selected Niche
                if "Watch" in niche_option:
                    v_data = [
                        ("1. Product Shots", "Hero Product Shot", f"Tampilan utama jam tangan {prod_label} dengan pencahayaan studio mewah, latar belakang charcoal, bayangan lembut, fokus tajam pada dial dan bezel."),
                        ("1. Product Shots", "Front 3/4 Angle", "Sudut pandang 3/4 depan memperlihatkan kedalaman case, tombol chronograph, dan tekstur strap logam/kulit."),
                        ("2. Hook", "Product Reveal", "Transisi dari kegelapan total ke sorotan cahaya dramatis yang mengungkap kemewahan jam tangan."),
                        ("3. Problem", "Busy Daily Life", "Pria eksekutif sibuk di meja kerja modern, menatap jam tangan dengan tenang di tengah rutinitas padat."),
                        ("4. Benefit", "Precision & Durability", "Pergerakan jarum detik kronograf yang presisi dan kekokohan rantai bracelet premium."),
                        ("5. Lifestyle", "Business Meeting", "Suasana rapat bisnis tingkat tinggi, memperlihatkan jam tangan di pergelangan tangan secara elegan."),
                        ("6. Detail / Macro", "Dial & Sub-Dials", "Makro super tajam menampilkan tekstur sunburst pada dial dan detail mekanis jam tangan."),
                        ("7. CTA", "Buy Now", "Komposisi bersih berfokus pada produk dengan tombol teks tebal bergaya minimalis: BELI SEKARANG.")
                    ]
                    script_data = [
                        ("1. Hook (0-3s)", "Visual jam tangan muncul dari kegelapan dengan sorotan cahaya metalik tajam.", f"Detik menentukan segalanya. Kenalkan kemewahan presisi dari {prod_label}.", f"Setiap detik berharga. Temukan jam tangan {prod_label} yang mendefinisikan ulang gaya Anda.", "#LuxuryWatch #JamTanganPria"),
                        ("2. Problem (3-7s)", "Ekspresi profesional melirik jam tangan di tengah kesibukan tinggi.", "Waktu berjalan cepat. Apakah Anda sudah memegang kendali penuh atas hari Anda?", "Kesibukan menuntut ketepatan. Jangan biarkan waktu mendikte Anda.", "#TimeManagement #PriaSukses"),
                        ("3. Benefit (7-12s)", "Macro shot dial, ketahanan air, dan rantai bracelet kokoh berkualitas tinggi.", "Dirancang dengan presisi absolut, material baja tahan karat, dan ketahanan tanpa kompromi.", "Kemewahan sejati terletak pada detail. Dibuat untuk bertahan dan memukau.", "#PrecisionWatch #DesignMewah"),
                        ("4. Lifestyle (12-18s)", "Penggunaan jam di ruang rapat eksekutif dan kafe urban kelas atas.", "Dari ruang rapat hingga malam gala, tampil percaya diri di setiap langkah perjalanan Anda.", "Sempurnakan gaya hidup profesional Anda dengan aksesori berkelas.", "#ExecutiveStyle #GayaPria"),
                        ("5. CTA (18-20s)", "Hero product shot dengan tombol Call to Action 'Beli Sekarang'.", "Amankan milik Anda hari ini. Elevasi penampilan Anda sekarang juga.", f"Stok terbatas untuk para pemimpin sejati. Klik tautan untuk miliki {prod_label} sekarang! BELI SEKARANG!", "#BeliSekarang #LimitedEdition")
                    ]
                elif "Smartphone" in niche_option:
                    v_data = [
                        ("1. Product Shots", "Front-Facing Hero Shot", f"Tampilan depan {prod_label} menampilkan layar menyala jernih, bezel tipis, dan proporsi bodi akurat di studio minimalis."),
                        ("1. Product Shots", "Rear-Facing Hero Shot", "Tampilan belakang menonjolkan modul kamera presisi, tekstur panel elegan, dan logo produk."),
                        ("2. Hook", "Dramatic Reveal", "Transisi cahaya dramatis dari gelap gulita yang secara perlahan mengungkap siluet bodi smartphone."),
                        ("3. Problem", "Low Battery / Performance Lag", "Ekspresi wajah profesional melihat ponsel lambat atau baterai habis saat mobilitas tinggi."),
                        ("4. Benefit", "Sleek Construction", "Konstruksi bodi ramping dengan perpaduan material kaca dan logam berkualitas tinggi."),
                        ("5. Lifestyle", "Office / Content Creation", "Penggunaan perangkat di ruang kerja modern atau saat mengambil konten foto/video luar ruangan."),
                        ("6. Detail / Macro", "Camera Module", "Makro tajam memperlihatkan keseluruhan tata letak modul kamera belakang dan finishing bodi."),
                        ("7. CTA", "Buy Now", "Komposisi hero produk di sebelah kiri dengan ruang negatif luas di kanan untuk teks 'BELI SEKARANG'.")
                    ]
                    script_data = [
                        ("1. Hook (0-3s)", "Transisi cahaya dramatis mengungkap siluet bodi smartphone dari kegelapan.", f"Detik pertama menentukan segalanya. Sambut era baru teknologi dari {prod_label}.", f"Rasakan lompatan performa dalam genggaman Anda bersama {prod_label}.", "#Smartphone #InovasiTeknologi"),
                        ("2. Problem (3-7s)", "Ekspresi lelah menghadapi ponsel lambat dan baterai habis saat mobilitas.", "Waktu Anda terlalu berharga untuk tertinggal oleh perangkat yang tidak dapat diandalkan.", "Pekerjaan menuntut kecepatan tanpa kompromi. Saatnya beralih ke performa maksimal.", "#Produktivitas #GayaHidupModern"),
                        ("3. Benefit (7-12s)", "Macro shot modul kamera, bodi tipis elegan, dan layar luas jernih tanpa batas.", "Desain bodi ramping, sistem optik presisi tinggi, dan ketahanan baterai optimal.", "Keindahan estetika berpadu dengan ketangguhan mutlak untuk aktivitas harian Anda.", "#DesignElegan #KameraSmartphone"),
                        ("4. Lifestyle (12-18s)", "Penggunaan natural di ruang rapat eksekutif, kafe urban, dan perjalanan luar ruang.", "Dari produktivitas kantor hingga hiburan maksimal, jalani hari dengan percaya diri.", "Sempurnakan gaya hidup digital Anda dengan perangkat berteknologi tinggi.", "#MobileLife #GadgetTerbaru"),
                        ("5. CTA (18-20s)", "Hero product shot bersih dengan tata letak tombol 'Beli Sekarang'.", "Amankan milik Anda hari ini. Elevasi produktivitas Anda sekarang juga.", f"Dapatkan penawaran spesial peluncuran {prod_label} hari ini. BELI SEKARANG!", "#BeliSekarang #PromoSmartphone")
                    ]
                elif "Fashion" in niche_option:
                    v_data = [
                        ("1. Product Shots", "Studio Flatlay / Hanging", f"Tampilan utama pakaian {prod_label} dengan pencahayaan lembut, menonjolkan tekstur kain, jahitan rapi, dan warna asli."),
                        ("1. Product Shots", "Model Lookbook Shot", "Model profesional mengenakan pakaian dengan latar belakang studio minimalis yang bersih."),
                        ("2. Hook", "Style Transformation", "Transisi cepat outfit kasual berubah menjadi tampilan modis dan elegan berkat pakaian ini."),
                        ("3. Problem", "Outfit Confusion", "Kebingungan memilih baju yang nyaman, adem, dan tetap stylish untuk dipakai seharian."),
                        ("4. Benefit", "Fabric & Comfort", "Makro tekstur bahan yang lembut, menyerap keringat, tidak mudah kusut, dan jatuh sempurna di badan."),
                        ("5. Lifestyle", "Urban Hangout / Office", "Model berjalan percaya diri di area perkotaan atau kafe estetik dengan gaya OOTD harian."),
                        ("6. Detail / Macro", "Stitching & Details", "Makro pada detail kancing, kerah, pola motif, atau jahitan presisi tinggi."),
                        ("7. CTA", "Shop The Look", "Tampilan model dengan teks tebal ajakan membeli: MILIKI SEKARANG.")
                    ]
                    script_data = [
                        ("1. Hook (0-3s)", "Model tampil memukau dengan balutan busana tren terbaru.", f"Tampil stylish dan percaya diri setiap hari dengan koleksi eksklusif dari {prod_label}.", f"Ubah gaya harian Anda menjadi pusat perhatian bersama {prod_label}.", "#OOTD #FashionIndonesia"),
                        ("2. Problem (3-7s)", "Ekspresi ragu di depan lemari pakaian karena bingung memilih baju yang pas.", "Pernah merasa tidak punya baju yang tepat untuk acara penting hari ini?", "Jangan biarkan salah kostum merusak hari Anda. Temukan kenyamanan dan gaya sekaligus.", "#FashionTips #GayaHarian"),
                        ("3. Benefit (7-12s)", "Close-up tekstur bahan premium yang lembut, adem, dan potongan pola pas di badan.", "Dibuat dari bahan pilihan berkualitas tinggi, adem dipakai seharian, dan potongan jahitan presisi.", "Kenyamanan tanpa kompromi dengan sentuhan desain elegan yang menawan.", "#BahanPremium #FashionTrendy"),
                        ("4. Lifestyle (12-18s)", "Aksi model berjalan santai di kafe atau area urban dengan gaya kasual chic.", "Cocok untuk berbagai suasana, dari santai, hangout, hingga acara semi formal.", "Pancarkan aura elegan di setiap langkah aktivitas harian Anda.", "#UrbanStyle #FashionOOTD"),
                        ("5. CTA (18-20s)", "Tampilan produk dengan tombol ajakan 'Beli Sekarang / Cek Keranjang'.", "Jangan sampai kehabisan warna favorit Anda. Dapatkan penawaran spesial hari ini.", f"Klik keranjang kuning atau tautan di bio untuk miliki {prod_label}. BELI SEKARANG!", "#BeliSekarang #PromoFashion")
                    ]
                else:
                    v_data = [
                        ("1. Product Shots", "Hero Product Shot", f"Tampilan utama produk {prod_label} dengan pencahayaan studio komersial yang bersih dan berkelas."),
                        ("2. Hook", "Problem Solver Hook", f"Visual cepat yang memperlihatkan bagaimana {prod_label} langsung menarik perhatian penonton di detik pertama."),
                        ("3. Problem", "Daily Challenge", "Skenario tantangan atau kebutuhan harian yang sering dialami target konsumen."),
                        ("4. Benefit", "Key Features & Quality", "Sorotan pada keunggulan utama, material berkualitas, dan fungsi optimal produk."),
                        ("5. Lifestyle", "Real Usage Scene", "Penggunaan produk secara nyata oleh pengguna dalam suasana gaya hidup modern."),
                        ("6. Detail / Macro", "Close-Up Details", "Makro tajam pada detail pengerjaan, tekstur, atau kemasan produk."),
                        ("7. CTA", "Buy Now", "Komposisi bersih berfokus pada produk dengan ajakan bertindak: BELI SEKARANG.")
                    ]
                    script_data = [
                        ("1. Hook (0-3s)", "Visual produk muncul dengan pencahayaan sinematik yang elegan.", f"Solusi terbaik untuk kebutuhan Anda kini hadir melalui {prod_label}.", f"Temukan kualitas dan kemudahan baru dalam hidup Anda bersama {prod_label}.", "#ProdukPilihan #RekomendasiTerbaik"),
                        ("2. Problem (3-7s)", "Skenario tantangan harian yang sering dialami konsumen.", "Apakah Anda sering kesulitan menemukan produk yang benar-benar bisa diandalkan?", "Saatnya beralih ke solusi yang lebih praktis, efektif, dan berkualitas tinggi.", "#SolusiPraktis #KebutuhanHarian"),
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
            st.subheader("📋 Hasil Generate Instan")
            
            tab1, tab2 = st.tabs(["🎨 Bank Visual & Prompt", "🎬 Skrip, VO & Caption"])
            
            with tab1:
                df_v = pd.DataFrame(st.session_state['v_data'], columns=["Kategori", "Scene", "Deskripsi Prompt Visual"])
                st.dataframe(df_v, use_container_width=True)
                
            with tab2:
                df_s = pd.DataFrame(st.session_state['script_data'], columns=["Bagian Kampanye", "Skrip Visual", "Voice Over (VO)", "Caption", "Hashtag"])
                st.dataframe(df_s, use_container_width=True if 'use_container_width' in dir(pd) else True, use_container_width=True)
                
            # Excel Download Button Creator
            output = io.BytesIO()
            wb = openpyxl.Workbook()
            
            ws1 = wb.active
            ws1.title = "Bank Visual"
            ws1.append(["Kategori", "Scene", "Deskripsi Prompt Visual"])
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
    st.info("👈 Silakan unggah foto produk referensi di atas untuk memulai generasi konten otomatis.")
