import time

def heavy_calculation():
    total = 0
    for i in range(10**8):  # cálculo pesado
        total += i
    return total

print("Iniciando cálculo...")
start = time.time()

result = heavy_calculation()

end = time.time()
print("Resultado:", result)
print("Tiempo total:", end - start, "segundos")
