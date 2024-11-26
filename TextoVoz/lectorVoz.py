from gtts import gTTS 
    
def conversorTextoAVoz(textoE):
    textos=textoE
    print(''+textos)
    language='es'
    tts = gTTS(text=textos, lang=language, slow=False) 
    tts.save("static/AudioVoz.mp3") 
    return textoE


#conversorTextoAVoz('hola mundo')