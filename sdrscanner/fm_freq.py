import numpy as np
# valores a ajustar
thr = 0.01    # Nivel de potencia
width_th = 10 # Ancho de senal
sdr_gain = 6

print("Threshold:", thr)
print("Width:", width_th)
print("Gain:", sdr_gain)

authorized = np.arange(88.3, 107.7, 0.1).tolist()