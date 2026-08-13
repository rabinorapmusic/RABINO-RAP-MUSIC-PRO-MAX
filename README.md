import streamlit as st
import time

st.set_page_config(page_title="RABINO RAP MUSIC PRO-MAX", layout="centered", page_icon="🎤")

# MICRÓFONO DEL QUE ME ENVIASTE - ESTILO PRO
st.markdown("""
<style>
.mic {
    font-size: 80px;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="mic">🎤</div>', unsafe_allow_html=True)
st.title("RABINO-RAP-MUSIC-PRO-MAX")
st.subheader("🔥 Tu estudio musical online")
st.caption("Genera letras de reggaeton, bachata, dembow y trap + indicaciones para Suno AI")

st.markdown("---")
st.header("🔥 LA CABINA REMIX")

# 1. NOMBRE
nombre = st.text_input("👤 Nombre del Artista", "Rabino")

# 2. GÉNERO CON BPM AUTOMÁTICO
genero_bpm = {
    "Reggaeton": 100,
    "Dembow": 95,
    "Bachata": 120,
    "Trap": 140,
    "Rap": 85
}
genero = st.selectbox("🎵 Género", list(genero_bpm.keys()))
bpm_auto = genero_bpm[genero]
st.info(f"⚡ BPM Automático: {bpm_auto}")

# 3. MODO
modo = st.radio("🎙️ Modo", ["Solo", "Dúo"])

# 4. TEMA
tema = st.text_area("📖 Tema / Prompt para Suno AI", "Ej: dinero, calle, bendición")

# 5. IDIOMA
idioma = st.selectbox("🌎 Idioma", ["Español", "English", "Bilingüe EN/ES"])

st.markdown("---")

# 6. BOTÓN GENERAR
if st.button("🔥 GENERAR REMIX PARA SUNO AI"):
    if not tema:
        st.error("Escribe un tema broth")
    else:
        with st.spinner("Creando letra + prompt para Suno..."):
            time.sleep(2)

            prompt_suno = f"{genero} song, {bpm_auto} BPM, {idioma}, about {tema}, male vocals, studio quality"

            letra = f"""[INTRO] RABINO PRO-MAX

[HOOK]
Yo estoy en {tema}
{bpm_auto} BPM dándole con fe
{nombre} en el {genero}
Esto es pa' ti y pa' tu gente

[VERSE 1]
De Los Alcarrizos al mundo
Con micrófono en la mano
"""

            st.success("✅ REMIX LISTO")
            st.subheader("1. LETRA")
            st.code(letra)

            st.subheader("2. PROMPT PARA SUNO AI")
            st.code(prompt_suno)
            st.info("Copia ese prompt y pégalo en Suno.com con el beat")

            st.download_button("⬇️ DESCARGAR TODO.ZIP", letra + prompt_suno, f"RABINO_{genero}_{tema}.txt")

st.markdown("---")
st.caption("👑 RABINO RAP MUSIC PRO-MAX | Hecho con Python + Streamlit | Copyright 2026 Rabino rap music")
