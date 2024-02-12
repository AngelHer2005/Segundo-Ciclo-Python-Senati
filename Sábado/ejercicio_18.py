valor,cantidad,numero_p = [["auto",3.50],["camión",15.00],["moto",8.0]],[0.0,0.0,0.0],0
automotores_t=int(input("¿Cuántos automóviles pasaron hoy día? "))
print("""Tipos:
    1. auto: S/. 3,50
    2. camiones: S/. 15
    3. Moto: S/. 8""")
while automotores_t != 0:
    tipo=int(input(f"¿Qué tipo de automóvil llevó el cliente N°{numero_p+1} en ingresar?\n"))
    if 0<tipo<=3:
        cantidad[tipo-1]+=1;numero_p+=1;automotores_t-=1
    else:print("Error. Ingresa una número válido..\n")            
        
print(f"""
La cantidad total recaudada en este día fue {((auto:=valor[0][1]*cantidad[0]))+(camion:=valor[1][1]*cantidad[1])+(moto:= valor[2][1]*cantidad[2])}

La cantidad total recaudada por cada tipo fue:
Auto = S/. {auto}
Camión = S/. {camion}
Moto = S/. {moto}

Y el tipo de automotor que más transita es: {valor[int(max(cantidad)-1)][0]}""")