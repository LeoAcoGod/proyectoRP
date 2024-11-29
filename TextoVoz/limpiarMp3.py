import os

def eliminar_archivos_mp3(ruta):
  for archivo in os.listdir(ruta):
    if archivo.endswith(".mp3"):
      ruta_completa = os.path.join(ruta, archivo)
      os.remove(ruta_completa)
      print(f"Archivo eliminado: {ruta_completa}")

ruta_carpeta = "/static/"
eliminar_archivos_mp3(ruta_carpeta)