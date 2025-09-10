def orden_lib():
    x = True
    e = 0
    libros_ordenados_por_año= ["","","","","","","","","",""]
    with open(libros_file, "r", encoding="utf-8") as f:
        lista_libros = f.readlines()
        for i in lista_libros:
            posicion  = 9
            if e > 0:
                separe_1 = i.split(",")
                año1 = separe_1[-2]
                año1 = int(año1)
                for a in range(1,11):
                    separe_2 = lista_libros[a].split(",")
                    año2 = separe_2[-2]
                    año2 = int(año2)
                    if (año1 < año2  and año1 != año2):
                        posicion = posicion - 1
                    if (año1 == año2 and e!= a):
                        if(x):
                            posicion = posicion - 1
                            x = False
                libros_ordenados_por_año[posicion] = i
            e = e + 1
    
    print("--- Libros ordenados por año asc ---")
    print(lista_libros[0])
    for i in libros_ordenados_por_año:
        print(i)
