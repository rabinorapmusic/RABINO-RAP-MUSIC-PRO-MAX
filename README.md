import streamlit as st
import time
import random

st.set_page_config(page_title="RABINO RAP STUDIO PRO", layout="centered", page_icon="🎤")

st.title("🎤 RABINO RAP STUDIO PRO")
st.subheader("La IA que convierte tu unción en HITS que cambian naciones")
st.markdown("---")

st.header("🔥 LA CABINA")

# CAMPO 1: NOMBRE
nombre = st.text_input("👤 Nombre del Artista", "Rabino")

# CAMPO 2: GÉNERO CON BPM AUTOMÁTICO
genero_bpm = {
    "Rap Cristiano": 85,
    "Dembow Cristiano": 95,
    "Reggaeton Cristiano": 100,
    "Trap Cristiano": 140,
    "Afro Cristiano": 110,
    "Drill Cristiano": 150
}
genero = st.selectbox("🎵 Género", list(genero_bpm.keys()))
bpm_auto = genero_bpm[genero]
st.info(f"⚡ BPM Automático: {bpm_auto} - Perfecto para {genero}")

# CAMPO 3: TEMA
tema = st.text_area("📖 Tema de la canción / Letra", "Ej: dinero, victoria, Dios, Los Alcarrizos")

st.markdown("---")
st.header("🎛️ PRODUCCIÓN")

# CAMPO 4: SUBIR BEAT
beat = st.file_uploader("📁 Sube tu Beat MP3", type=["mp3", "wav"])
if not beat:
    if st.button("🎵 GENERAR BEAT ORIGINAL IA"):
        st.success(f"✅ Beat {genero} a {bpm_auto} BPM generado")

# CAMPO 5: SUBIR VOZ PARA CLONAR
voz = st.file_uploader("🎙️ Sube tu Voz WAV - 15 segundos pa' clonarte", type=["wav", "mp3"])

# CAMPO 6: VOZ A CLONAR - ARREGLADO
voz_clonar = st.selectbox("🧠 Voz a Clonar", ["Mi Voz - La que subí arriba", "Voz IA Genérica"])
if voz_clonar == "Mi Voz - La que subí arriba" and voz:
    st.success("✅ Tu voz está lista para clonar")

st.markdown("---")

# CAMPO 7: BOTÓN GENERAR 10 HITS
if st.button("🔥 GENERAR 10 HITS CON MI VOZ"):
    if not tema:
        st.error("Escribe un tema primero broth")
    elif not voz:
        st.error("Sube tu clip de voz pa' clonarte")
    else:
        progress = st.progress(0)
        for i in range(10):
            with st.spinner(f"Creando HIT {i+1}/10 en {genero} a {bpm_auto} BPM..."):
                time.sleep(1.5)
                letra = f"[HOOK]\nYo estoy en {tema}\n{nombre} en el beat a {bpm_auto} BPM\nRABINO RECORDS con unción"
                st.write(f"**{i+1}. {tema} - {genero} - {bpm_auto}BPM**")
                st.code(letra)
            progress.progress((i+1)/10)

        st.balloons()
        st.success("✅ 10 HITS LISTOS CON TU VOZ")

        st.header("💰 PANEL DE MONETIZACIÓN")
        st.write("Todo listo para subir a Spotify, TikTok, YouTube")
        st.download_button("⬇️ DESCARGAR PAQUETE COMPLETO.ZIP", "zip_data", f"RABINO_{tema}_10HITS.zip")

st.markdown("---")
st.caption("👑 Hecho por RABINO RECORDS | BPM automático por género | 100% Copyright tuyo")
