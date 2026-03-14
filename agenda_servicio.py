fechas = []
servicios = []
precios = []


while True:     
 print('\nMENU')
 print("1-Ingresar servicio")
 print('2-Ver total ganado:')
 print('3-Ver registros:')
 print('4-Ver ganancias por servicio')
 print('5--Salir')

 opcion = input('Opcion:')
 if opcion == '1':
    fecha_horario = input("Fecha y horario:")
    servicio = input('Servicio:')
    precio = int(input('Precio:'))
    
    fechas.append(fecha_horario)
    servicios.append(servicio)
    precios.append(precio)
    mes = fecha_horario[0:7]
    archivo_nombre = f'agenda_{mes}.txt'
    with open( archivo_nombre, 'a') as archivo:
        archivo.write(f"{fecha_horario},{servicio},{precio}\n")
    
 elif opcion == '2':
    print('El total de diciembre es de',sum(precios))
 elif opcion == '3':
    for i in range(len(servicios)):
        print(fechas[i],servicios[i],precios[i])
 elif opcion =='4':
    ganancias_servicio = {}
    for i in range(len(servicios)):
      servicio = servicios[i]
      precio = precios[i]
      if servicio in ganancias_servicio:
        ganancias_servicio[servicio ]+=precio
      else:
        ganancias_servicio[servicio] = precio
    print("\nGanancias por servicio:")
    for s in  ganancias_servicio:
       print(s, "→", ganancias_servicio[s])
 elif opcion == '5':
     print('Programa terminado')
     break
 else:
     print('Opcion invalida')
     
 



