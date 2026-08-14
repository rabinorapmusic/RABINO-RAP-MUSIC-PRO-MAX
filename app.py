import gradio as gr
import random
from gtts import gTTS
import os

def generar_cancion(tema):
    if tema.strip() == "":
        return "⚠️ Escribe un tema bro 😈 Ej: Dembow de Los Alcarrizos", None, ""
    
    # BASE DE DATOS DE ARTISTAS
    artistas = [
        ["Romeo Santos", "Karol G"],
        ["Bad Bunny", "Rosalia"],
        ["Aventura", "Shakira"],
        ["El Alfa", "Becky G"],
        ["Juan Luis Guerra", "Natti Natasha"],
        ["Anuel AA", "Karol G"],
        ["Daddy Yankee", "Selena Gomez"],
        ["Ozuna", "Becky G"]
    ]
    estilos = ["Dembow", "Reggaeton", "Bachata", "Trap", "Merengue"]

    duo = random.choice(artistas)
    estilo = random.choice(estilos)

    # LETRA GENERADA
    letra = f"""🔥 NUEVO DÚO: {duo[0]} x {duo[1]} 🔥
GÉNERO: {estilo}
TEMA: {tema}

[Intro - Cerebro]
Rabino Rap en el beat, Cerebro activado

[Verso 1 - {duo[0]}]
Desde Los Alcarrizos pa'l mundo entero
Con flow de Rabino Rap, soy el primero
{tema}, eso es lo que quiero baby
Dime si te atreves a bailar conmigo

[Verso 2 - {duo[1]}]
Tú me tienes mal, no puedo negarlo
Tu flow me tiene en el suelo
Dale que esto se va a prender
Que esta noche la vamos a romper

[Coro - Los 2]
Cerebro en el beat, Rabino en la casa
Esto está caliente, que nadie se pasa
{tema} conmigo hasta que amanezca
Dale que el dembow no se regresa

[Outro]
Producido por Cerebro IA
"""
    # CREAR AUDIO CON VOZ
    archivo = "cerebro.mp3"
    tts = gTTS(letra, lang='es', slow=False)
    tts.save(archivo)
    
    # ACORDES PARA PRODUCIR
    acordes = f"""TONO: D menor 
ACORDES: Dm - Gm - C - F 
BPM: 95 
GÉNERO: {estilo}
KIT: Usa 808 + Tambora si es {estilo}"""
    
    return letra, archivo, acordes

# INTERFAZ DE GRADIO
with gr.Blocks(title="CEREBRO - Rabino Rap", theme=gr.themes.Soft()) as demo:
    gr.Markdown("# 🧠 CEREBRO - RABINO RAP")
    gr.Markdown("**Escribe un tema y Cerebro te crea un dúo completo con voz + acordes**")
    
    with gr.Row():
        tema = gr.Textbox(
            label="Escribe el tema", 
            placeholder="Ej: Amor en Los Alcarrizos, Desamor, Party", 
            scale=4
        )
        btn = gr.Button("DESPERTAR A CEREBRO 🔥", variant="primary", scale=1)
    
    with gr.Row():
        letra_out = gr.Textbox(label="📝 Letra Generada", lines=12)
        audio_out = gr.Audio(label="🔊 Voz de Cerebro")
    
    acordes_out = gr.Textbox(label="🎸 Acordes para Producir")
    
    btn.click(fn=generar_cancion, inputs=tema, outputs=[letra_out, audio_out, acordes_out])
    
    gr.Markdown("### Hecho por Rabino Rap 🇩🇴 | Powered by IA")

demo.launch()
