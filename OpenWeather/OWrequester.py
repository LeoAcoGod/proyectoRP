import requests

def obtener_clima(ciudad):
    api_key = "959a7f456379d6dad4ee635600d591fc"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units=metric"
    respuesta = requests.get(url)
    datos = respuesta.json()

    if respuesta.status_code == 200:
        temperatura = datos['main']['temp']
        humedad = datos['main']['humidity']
        descripcion = datos['weather'][0]['description']
        tipoLogo=logoTipe(descripcion) 
       
        resultados =[ciudad,descripcion,temperatura,humedad,tipoLogo]
        
        return resultados
    else:
        print("Error al obtener los datos del clima.")

def logoTipe(descripcionL):
    switch = {
        "clear sky": "01d",
        "few clouds": "02d",
        "scattered clouds": "03d",
        "broken clouds": "04d",
        "shower rain": "09d",
        "rain": "10d",
        "thunderstorm": "11d",
        "snow": "13d",
        "mist": "50d",
        
    }
    return switch.get(descripcionL, "01n")

#consola
#ciudad = "Tezontepec de Aldama"
#print('',obtener_clima(ciudad))