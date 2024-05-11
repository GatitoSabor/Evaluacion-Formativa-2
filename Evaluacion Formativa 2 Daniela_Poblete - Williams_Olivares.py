#Variables
roll_1 = 0
roll_2 = 0
roll_3 = 0
roll_4 = 0
total = 0
desc = 0
Pikachu = 4500
Otaku = 5000
Pulpo = 5200
Anguila = 4800
orden_completa = "no"
reingreso = "no"
otro_pedido = "si"


#Programa principal
while otro_pedido != "no":

    while orden_completa != "si":

        print('''
        Tienda de Sushi
        ----------------------------------
        1. Pikachu Roll             $4.500
        2. Otaku Roll               $5.000
        3. Pulpo Venenoso Roll      $5.200
        4. Anguila Electrica Roll   $4.800
        ''')

        while True:
            try:
                opc=int(input('Seleccione una opcion\n'))
                if opc == 1 or opc == 2 or opc == 3 or opc == 4:
                    break
                else:
                    print('Ingrese una opcion valida')
            except:
                print('Ingrese una opcion valida')
            

        if opc==1:
            roll_1=roll_1+1
        elif opc==2:
            roll_2=roll_2+1
        elif opc==3:
            roll_3=roll_3+1
        elif opc==4:
            roll_4=roll_4+1    

        print(f'''
        ----------------------------------
        {roll_1} Pikachu Roll             ${roll_1 * Pikachu}
        {roll_2} Otaku Roll               ${roll_2 * Otaku}
        {roll_3} Pulpo Venenoso Roll      ${roll_3 * Pulpo}
        {roll_4} Anguila Electrica Roll   ${roll_4 * Anguila}
        ----------------------------------
        ''')

        while True:
            orden_completa = input('¿Su orden esta completa? (si / no)\n')
            if orden_completa=="no":
                break
            elif orden_completa=="si":
                break
            else:
                print('Ingrese una opcion valida')


    total = (roll_1*Pikachu) + (roll_2 * Otaku) + (roll_3 * Pulpo) + (roll_4 * Anguila)

    while True:

        descuento = input('¿Tiene codigo de descuento? (si / no)\n')

        if descuento == 'si':
            while reingreso != "X":
                codigo = input('Ingrese el codigo')
                if codigo == "soyotaku":
                    print('Codigo valido, 10% de descuento')
                    desc = total * 0.1
                    break
                else:
                    print('Codigo no valido')
                    while True:
                        reingreso = input('¿Desea volver a intentarlo? (Y = Si / X = No)')
                        if reingreso == "Y":
                            break
                        elif reingreso == "X":
                            break
                        else:
                            print('Ingrese una opcion valida')
            break
        elif descuento == 'no':
            break
        else:
            print('Ingrese una opcion valida')

    print(f'''
    *************************************
    Total productos: {roll_1 + roll_2 + roll_3 + roll_4}
    *************************************
    Pikachu Roll: {roll_1}
    Otaku Roll: {roll_2}
    Pulpo Venenoso Roll: {roll_3}
    Anguila Electrica Roll: {roll_4}
    *************************************
    Subtotal por pagar: ${total}
    Descuento por codigo: ${desc}
    TOTAL: {total - desc}
    ''')

    while True:
        otro_pedido = input('¿Desea hacer otro pedido? (si / no)\n')
        if otro_pedido == "si":
            break
        elif otro_pedido == "no":
            break
        else:
            print('Ingrese una opcion valida')

    roll_1 = 0
    roll_2 = 0
    roll_3 = 0
    roll_4 = 0
    total = 0
    desc = 0
    reingreso = "no"
