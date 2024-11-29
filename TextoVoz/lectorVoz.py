from gtts import gTTS 
from datetime import datetime


def conversorTextoAVoz(textoE):
    language='es'
    tts = gTTS(text=textoE, lang=language, slow=False)
    now = datetime.now()    
    current_time = now.strftime("%H_%M_%S")
    tts.save("static/"+current_time+".mp3") 
    return textoE,current_time


#conversorTextoAVoz('hola mundo')