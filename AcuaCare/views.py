from django.shortcuts import render
from .forms import FormularioChatBot
from .forms import FormularioWeather
from chatbotCarpet import chatbot
from OpenWeather import OWrequester
from TextoVoz import lectorVoz
from django.core.cache import cache
from django.shortcuts import redirect
from .forms import FeedbackForm


def chatbot_view(request):
    
    if request.method == 'POST':
        formulario = FormularioChatBot(request.POST)
        if formulario.is_valid():

            peticion_text = formulario.cleaned_data['texto']
            response_bot = chatbot.respuesta(peticion_text)

            if not ConnectionError:
                voiceResponse=lectorVoz.conversorTextoAVoz(response_bot)            
            else:
                voiceResponse=response_bot
            
            cache.clear()
            audio_src="/static/AudioVoz.mp3"
            return render(request, 'chatbot.html', {'pet': formulario,'res_bot': voiceResponse,'audio_src':audio_src })
    else:
        formulario = FormularioChatBot()
    return render(request, 'chatbot.html', {'pet': formulario})



def weather_view(request):
    
    if request.method == 'POST':
        formularioW = FormularioWeather(request.POST)
        ciudad = "Tezontepec de Aldama"


        if not ConnectionError:
            response_W = OWrequester.obtener_clima(ciudad)
        else:
            response_W = ['No hay conexion a internet','no es posible realizar la peticion','','','']
        
        paisW=response_W[0]
        descripcionW=response_W[1]
        temperaturaW=response_W[2]
        humedadW=response_W[3]
        logoW=response_W[4]
    
        return render(request, 'weather.html', {'paisW': paisW, 'descripcionW':descripcionW, 'temperaturaW':temperaturaW, 'humedadW':humedadW, 'logoW':logoW})
    else:
        formularioW = FormularioWeather()
    return render(request, 'weather.html')

def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)

        if form.is_valid():
            form.save()
            
            return redirect('login')
    else:
        form = FeedbackForm()
    return render(request, 'feedback.html', {'form': form})