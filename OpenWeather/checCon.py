import requests

def check_internet_connection():
    try:
        response = requests.get('https://www.google.com', timeout=5)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.exceptions.RequestException as e:
        print(f"No se pudo establecer conexión: {e}")
        return False