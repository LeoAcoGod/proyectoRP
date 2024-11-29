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
        tipoLogo = logoTipe(descripcion) 
        comentarioE = obtenerResClima(descripcion)
        resultados = [ciudad,descripcion,temperatura,humedad,tipoLogo,comentarioE]
        
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

def obtenerResClima(clima):
    switch = {
        "clear sky": "Es recomendable regar despues de la puesta de sol",
        "few clouds": "Es recomendable regar despues de la puesta de sol",
        "scattered clouds": "Puede regar normalmente o esperar a que nubla mas",
        "broken clouds": "Riegue en pequeñas cantidades o espere a que llueva",
        "shower rain": "No es recomendable regar",
        "rain": "La lluvia es importante para el crecimiento natural",
        "thunderstorm": "Resguarde plantas pequeñas en interiores",
        "snow": "Resguarde plantas pequeñas en interiores",
        "mist": "Resguarde plantas pequeñas en interiores",
        
    }
    return switch.get(clima, "01n")

#consola
#ciudad = "Tezontepec de Aldama"
#print('',obtener_clima(ciudad))