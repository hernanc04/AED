# Carga de datos
distancia = 3641.3 * 1000
m_recorridos = float(input("Metros recorridos: "))

# Procesos
km = m_recorridos // 1000
mts = m_recorridos % 1000
porcentaje = (m_recorridos * 100) / distancia

# Muestra d datos
print(f'El aventurero recorrió {km} km y {mts} metros.\nUn {porcentaje}% de la distancia total.')




