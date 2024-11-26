import numpy as np
from keras.api.models import Sequential
from keras.api.layers import Dense

# Suponiendo que tienes tus datos en dos arreglos: X (clima) e y (acciones recomendadas)
X={'25','30'}
Y={'No regar',' regar'}

# Crear el modelo
model = Sequential()
model.add(Dense(64, activation='relu', input_dim=X.shape[1]))
model.add(Dense(32, activation='relu'))
model.add(Dense(1, activation='linear'))

# Compilar el modelo
model.compile(loss='mean_squared_error', optimizer='adam')

# Entrenar el modelo
model.fit(X, Y, epochs=100, batch_size=32)

# Hacer una predicción
nueva_condicion_climatica = np.array([[25, 70, 10]])  # Ejemplo de entrada
prediccion = model.predict(nueva_condicion_climatica)
print("Recomendación:", prediccion)