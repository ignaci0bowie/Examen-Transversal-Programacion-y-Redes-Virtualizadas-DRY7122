# Script para verificar el rango de VLAN ingresado por el usuario
vlan = int(input("Ingrese el número de VLAN: "))

if 1 <= vlan <= 1005:
    print(f"La VLAN {vlan} pertenece al rango normal.")
elif 1006 <= vlan <= 4094:
    print(f"La VLAN {vlan} pertenece al rango extendido.")
else:
    print("El número de VLAN ingresado no es válido.")
