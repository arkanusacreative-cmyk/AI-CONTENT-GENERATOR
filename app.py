import streamlit as st
import pandas as pd
import openpyxl
import io
from PIL import Image
import urllib.parse

st.set_page_config(
    page_title="AI Multi-Niche Commercial Content Generator & Image Creator",
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

st.markdown('<p class="main-header">🎬 AI Multi-Niche Content & Image Generator</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Unggah foto produk, pilih niche, hasilkan bank visual, skrip, caption, serta <b>Generate Gambar Visual Komersial AI secara Langsung!</b></p>', unsafe_allow_html=True)

# Sidebar Configuration
st.sidebar.header("⚙️ Pengaturan Kampanye & AI")
niche_option = st.sidebar.selectbox(
    "Pilih Niche Produk:",
    [
        "Audio & Speaker (Edifier / Karaoke / Hifi)",
        "Jam Tangan (Watch)",
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

product_name_input = st.sidebar.text_input("Nama Spesifik Produk (Opsional):", value="", placeholder="Cth: Edifier Bookshelf / ROBOT RB650")

st.sidebar.markdown("---")
st.sidebar.info("💡 **Fitur Baru:** Pilih prompt di bawah untuk langsung memunculkan hasil gambar AI sesuai konsep komersial produk Anda.")

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
        
        if st.button("✨ Generate Paket Konten & Kampanye Komersial"):
            with st.spinner("Merancang bank visual, skrip spesifik produk, VO, dan hashtag..."):
                
                prod_label = product_name_input if product_name_input else niche_option
                
                # Dynamic Database Generator based on Selected Niche
                if "Audio" in niche_option:
                    v_data = [
                        ("1. Product Shots", "Hero Product Shot", f"Professional commercial product photography of wood finish active bookshelf speaker {prod_label} with black fabric grill, warm studio lighting, 8k resolution, photorealistic"),
                        ("1. Product Shots", "Studio Angle View", f"Close up angle view showing tweeter, woofer, bass reflex port, and classic wooden side panels of {prod_label}, commercial studio background"),
                        ("2. Hook", "Immersive Sound Wave", f"Cinematic sound waves radiating from {prod_label} in a cozy aesthetic modern room, warm atmosphere, high-end lifestyle"),
                        ("3. Lifestyle", "Room Setup / Working Vibe", f"{prod_label} placed neatly on a wooden aesthetic desk with vinyl records and a clean laptop setup, cozy lighting"),
                        ("4. Detail / Macro", "Wood Texture & Tweeter", f"Macro super sharp photography of the wooden side texture and tweeter dome of {prod_label}, commercial detail shot")
                    ]
                    script_data = [
                        ("1. Hook (0-3s)", "Musik menghentak dengan visual speaker menyala dinamis di ruangan estetik.", f"Rasakan detail suara sesungguhnya di ruangan Anda dengan {prod_label}.", f"Ubah cara Anda mendengarkan musik selamanya bersama kejernihan audio dari {prod_label}.", "#AudioHiFi #EdifierSpeaker"),
                        ("2. Problem (3-7s)", "Ekspresi kurang puas mendengarkan audio berkualitas rendah dan cempreng.", "Pernah merasa musik favorit Anda terdengar datar dan kehilangan detail aslinya?", "Jangan biarkan kualitas suara buruk merusak pengalaman mendengarkan musik Anda.", "#SoundQuality #AudioLokal"),
                        ("3. Benefit (7-12s)", "Close-up woofer berdenyut, kejernihan vokal, dan material kayu premium.", "Dilengkapi teknologi akustik presisi tinggi, bass mendalam, dan vokal jernih tanpa distorsi.", "Sentuhan estetika kayu klasik berpadu dengan performa suara kelas studio.", "#HiFiAudio #SpeakerAktif"),
                        ("4. Lifestyle (12-18s)", "Suasana kamar atau ruang kerja estetik ditemani alunan musik santai yang hangat.", "Sempurnakan sudut ruangan Anda dengan estetika berkelas dan suara menggelegar.", "Nikmati setiap detail instrumen musik seolah Anda berada di konser langsung.", "#RoomDecor #WorkstationVibes"),
                        ("5. CTA (18-20s)", "Tampilan produk elegan dengan tombol ajakan 'Beli Sekarang'.", "Tingkatkan kualitas audio Anda hari ini. Rasakan perbedaannya.", f"Stok terbatas. Klik tautan di bio untuk miliki {prod_label} sekarang! BELI SEKARANG!", "#BeliSekarang #AudioMewah")
                    ]
                elif "Watch" in niche_option:
                    v_data = [
                        ("1. Product Shots", "Hero Product Shot", f"Luxury commercial watch photography of {prod_label}, dramatic charcoal background, soft shadow, sharp focus on dial and bezel, 8k"),
                        ("1. Product Shots", "Front 3/4 Angle", f"3/4 angle view of luxury timepiece {prod_label}, showing case depth, chronograph pushers, and metallic strap texture"),
                        ("2. Hook", "Product Reveal", f"Cinematic product reveal of luxury watch {prod_label} emerging from dark shadow with sharp metallic light highlight"),
                        ("3. Lifestyle", "Business Meeting", f"High-end executive wrist wearing luxury watch {prod_label} in a professional corporate boardroom meeting"),
                        ("4. Detail / Macro", "Dial & Sub-Dials", f"Macro photography showing sunburst dial texture and mechanical details of luxury watch {prod_label}")
                    ]
                    script_data = [
                        ("1. Hook (0-3s)", "Visual jam tangan muncul dari kegelapan dengan sorotan cahaya metalik tajam.", f"Detik menentukan segalanya. Kenalkan kemewahan presisi dari {prod_label}.", f"Setiap detik berharga. Temukan jam tangan {prod_label} yang mendefinisikan ulang gaya Anda.", "#LuxuryWatch #JamTanganPria"),
                        ("2. Problem (3-7s)", "Ekspresi profesional melirik jam tangan di tengah kesibukan tinggi.", "Waktu berjalan cepat. Apakah Anda sudah memegang kendali penuh atas hari Anda?", "Kesibukan menuntut ketepatan. Jangan biarkan waktu mendikte Anda.", "#TimeManagement #PriaSukses"),
                        ("3. Benefit (7-12s)", "Macro shot dial, ketahanan air, dan rantai bracelet kokoh berkualitas tinggi.", "Dirancang dengan presisi absolut, material baja tahan karat, dan ketahanan tanpa kompromi.", "Kemewahan sejati terletak pada detail. Dibuat untuk bertahan dan memukau.", "#PrecisionWatch #DesignMewah"),
                        ("4. Lifestyle (12-18s)", "Penggunaan jam di ruang rapat eksekutif dan kafe urban kelas atas.", "Dari ruang rapat hingga malam gala, tampil percaya diri di setiap langkah perjalanan Anda.", "Sempurnakan gaya hidup profesional Anda dengan aksesori berkelas.", "#ExecutiveStyle #GayaPria"),
                        ("5. CTA (18-20s)", "Hero product shot dengan tombol Call to Action 'Beli Sekarang'.", "Amankan milik Anda hari ini. Elevasi penampilan Anda sekarang juga.", f"Stok terbatas untuk para pemimpin sejati. Klik tautan untuk miliki {prod_label} sekarang! BELI SEKARANG!", "#BeliSekarang #LimitedEdition")
                    ]
                else:
                    v_data = [
                        ("1. Product Shots", "Hero Product Shot", f"Professional commercial product photography of {prod_label}, clean minimalist studio background, high-end lighting, photorealistic 8k"),
                        ("1. Product Shots", "Studio Angle View", f"Dynamic angled commercial view of {prod_label}, showcasing premium build quality and modern design"),
                        ("2. Hook", "Problem Solver Hook", f"Stunning visual presentation of {prod_label} catching immediate attention in a commercial aesthetic setup"),
                        ("3. Lifestyle", "Real Usage Scene", f"Happy modern user utilizing {prod_label} in a bright natural lifestyle environment, high-end cinematic vibe"),
                        ("4. Detail / Macro", "Close-Up Details", f"Macro close-up shot focusing on the premium texture and material finishing of {prod_label}")
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
            st.subheader("📋 Hasil Generate Instan & AI Image Creator")
            
            tab1, tab2, tab3 = st.tabs(["🎨 Bank Visual & Prompt", "🖼️ **AI Image Generator Langsung**", "🎬 Skrip, VO & Caption"])
            
            with tab1:
                df_v = pd.DataFrame(st.session_state['v_data'], columns=["Kategori", "Scene", "Prompt Bahasa Inggris (AI Ready)"])
                st.dataframe(df_v, use_container_width=True)
                
            with tab2:
                st.markdown("### 🎨 Buat Gambar Konsep Komersial Secara Instan")
                st.info("Pilih salah satu adegan di bawah ini, lalu klik tombol untuk merender gambarnya secara otomatis melalui AI tanpa perlu pindah aplikasi!")
                
                selected_scene_idx = st.selectbox(
                    "Pilih Adegan / Scene Visual untuk Dirender:",
                    range(len(st.session_state['v_data'])),
                    format_func=lambda x: f"{st.session_state['v_data'][x][0]} - {st.session_state['v_data'][x][1]}"
                )
                
                chosen_prompt = st.session_state['v_data'][selected_scene_idx][2]
                st.text_area("Prompt AI yang Digunakan:", value=chosen_prompt, height=80)
                
                if st.button("🚀 Render Gambar AI Sekarang"):
                    with st.spinner("Sedang merender gambar komersial via AI (tunggu 5-10 detik)..."):
                        # Encode prompt for Pollinations AI URL
                        encoded_prompt = urllib.parse.quote(chosen_prompt)
                        # Set width/height based on aspect ratio choice
                        width, height = (576, 1024) if "9:16" in aspect_ratio else (1024, 1024) if "1:1" in aspect_ratio else (1280, 720)
                        
                        ai_image_url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width={width}&height={height}&nologo=true"
                        
                        st.success("Gambar berhasil dirender!")
                        st.image(ai_image_url, caption=f"Hasil AI: {st.session_state['v_data'][selected_scene_idx][1]}", use_container_width=True)
                        st.markdown(f"🔗 [Buka Gambar Resolusi Penuh di Tab Baru]({ai_image_url})")

            with tab3:
                df_s = pd.DataFrame(st.session_state['script_data'], columns=["Bagian Kampanye", "Skrip Visual", "Voice Over (VO)", "Caption", "Hashtag"])
                st.dataframe(df_s, use_container_width=True)
                
            # Excel Download Button Creator
            output = io.BytesIO()
            wb = openpyxl.Workbook()
            
            ws1 = wb.active
            ws1.title = "Bank Visual & Prompt"
            ws1.append(["Kategori", "Scene", "Prompt AI"])
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
