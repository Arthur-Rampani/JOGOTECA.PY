def tabuada_extrema():
    import random
    numero_gerado = random.randint(1, 10)
    numero_gerado2 = random.randint(1, 10)
    total = random.randint(1, 4)
    if total == 1:
        total = numero_gerado - numero_gerado2
        print(f"o {numero_gerado} - {numero_gerado2} = ?")
    if total == 2:
        total = numero_gerado + numero_gerado2
        print(f"o {numero_gerado} + {numero_gerado2} = ?")
    if total == 3:
        total = numero_gerado * numero_gerado2
        print(f"o {numero_gerado} * {numero_gerado2} = ?")
    if total == 4:
        total = numero_gerado / numero_gerado2
        print(f"o {numero_gerado} / {numero_gerado2} = ?")
    while True:
        usuario = float(input("Quais números? "))
        numero_gerado = random.randint(1, 10)
        numero_gerado2 = random.randint(1, 10)
        if usuario == 1:
            total = numero_gerado - numero_gerado2
            print(f"voce irá fazer uma subtração, e o total será {total}")
        if usuario == 2:
            total = numero_gerado + numero_gerado2
            print(f"voce irá fazer uma adição, e o total será {total}")
        if usuario == 3:
            total = numero_gerado * numero_gerado2
            print(f"voce irá fazer uma multiplicação, e o total será {total}")
        if usuario == 4:
            total = numero_gerado / numero_gerado2
            print(f"voce irá fazer uma divisão, e o total será {total}")