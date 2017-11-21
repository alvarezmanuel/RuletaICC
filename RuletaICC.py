rollcount = 0
print("¡Bienvenido al juego de Ruleta!")
print("Tu saldo inicial es de 500")
while rollcount < 100:
    import random
    landon = random.randint(0, 36)
    LOB = []
    budget = 500
    valnum = 0
    valin = 0
    input("Presiona Enter para ver las Opciones De Apuesta")
    print("Opciones de apuesta:")
    print("--------------------")
    print("Apuesta a que caiga en un número par escribiendo 'par'")
    print("Apuesta a que caiga en un número impar escribiendo 'impar'")
    print("Apuesta a que caiga en un número entre 0 y 12 escribiendo '1ra 3ra'")
    print("Apuesta a que caiga en un número entre 13 y 25 escribiendo '2da 3ra'")
    print("Apuesta a que caiga en un número entre 25 y 36 escribiendo '3ra 3ra'")
    print("Apuesta a que caiga en un número en específico escribiendo 'num'")
    print("Escribe 'pmitad' para apostar entre 0 y 18, y escribe 'smitad'")
    betin = input("Introduce tu apuesta: ")
    if betin == 'par':
        def apostarpar():
            global valin
            print("Has elegido apostar a los números impares")
            valin = input("¿Cuánto te gustaría apostar?: ")
            print("Si cae en un número par, ganas", int(valin)*2)
            LOB.append('apostarpar')
        apostarpar()
    if betin == 'impar':
        def apostarimpar():
            global valin
            print("Has elegido apostar a los números impares")
            valin = input("¿Cuánto te gustaría apostar?: ")
            print("Si cae en un número par, ganas", int(valin)*2)
            LOB.append('apostarimpar')
        apostarimpar()
    if betin == '1ra 3ra':
        def apostar13():
            global valin
            print("Has elegido apostar en el primer tercio de números")
            valin = input("¿Cuánto te gustaría apostar?: ")
            print("Si cae en el primer tercio de números, ganas", int(valin)*3)
            LOB.append('apostar13')
        apostar13()
    if betin == '2da 3ra':
        def apostar23():
            global valin
            print("Has elegido apostar en el segundo tercio de números")
            valin = input("¿Cuánto te gustaría apostar?: ")
            print("Si cae en el primer tercio de números, ganas", int(valin)*3)
            LOB.append('apostar23')
        apostar23()
    if betin == '3ra 3ra':
        def apostar33():
            global valin
            print("Has elegido apostar en el tercer tercio de números")
            valin = input("¿Cuánto te gustaría apostar?: ")
            print("Si cae en el segundo tercio de números, ganas", int(valin)*3)
            LOB.append('apostar33')
        apostar33()
    if betin == 'num':
        def apostarnum():
            global valin
            global valnum
            print("Has elegido apostar en un número en específico")
            valnum = input("¿En qué número te gustaría apostar?: ")
            if int(valnum) > 36 or int(valnum) < 0:
                print("No puedes apostar en ese número...")
                print("El juego ha encontrado un error, ¿Por qué harías eso?")
                class NotOnRouletteBoard(Exception):
                    pass
                raise NotOnRouletteBoard
            else:
                print("Has elegido apostar en", valnum)
                valin = input("¿Cuánto te gustaría apostar?: ")
                print("Si cae en", valnum,  "ganas", int(valin)*36)
                LOB.append('num')
                LOB.append(valnum)
        apostarnum()
    if betin == 'pmitad':
        def apostarpmitad():
            global valin
            print("Has elegido apostar en la primera mitad")
            valin = input("¿Cuánto te gustaría apostar?: ")
            print("Si cae en la primera mitad de números, ganas", int(valin)*2)
            LOB.append('apostarpmitad')
            apostarpmitad()
    if betin == 'smitad':
        def apostarsmitad():
            global valin
            print("Has elegido apostar en la primera mitad")
            valin = input("¿Cuánto te gustaría apostar?: ")
            print("Si cae en la segunda mitad de números, ganas", int(valin)*2)
            LOB.append('apostarsmitad')
        apostarsmitad()
    def Girar():
        print("Girando...")
        print("Casi pasa a", random.randint(0, 36))
        print("Casi cae en", random.randint(0, 36))
        global landon
        print("Ha caído en", landon)
    Girar()
    def lose():
        global budget
        global valin
        print("¡Oh no! ¡Perdiste!")
        print("Perdiste", valin, "Soles")
        budget -= int(valin)
        print("Tu saldo es ahora", budget, 'soles')
    def evenwin():
        global valin
        global budget
        print("¡Wow! ¡Ganaste! ¡Ha sido un número par!")
        print("¡Recibes", int(valin)*2, "soles!")
        budget += int(valin)*2
        print("Tu saldo es ahora", budget, 'soles')
    def oddwin():
        global valin
        global budget
        print("¡Wow! ¡Ganaste! ¡Ha sido un número impar!")
        print("¡Recibes", int(valin)*2, "soles!")
        budget += int(valin)*2
        print("Tu saldo es ahora", budget, 'soles')
    def win13():
        global valin
        global budget
        print("¡Imcreìble! ¡Ganaste!")
        print("¡Recibes", int(valin)*3, "soles!")
        budget += int(valin)*3
        print("Tu saldo es ahora", budget, 'soles')
    def win23():
        global valin
        global budget
        print("¡Sorprendente! ¡Le atinaste!")
        print("¡Recibes", int(valin)*3, "soles!")
        budget += int(valin)*3
        print("Tu saldo es ahora", budget, 'soles')
    def win33():
        global valin
        global budget
        print("¡Buen trabajo, acertaste con el tercer tercio!")
        print("¡Recibes", int(valin)*3, "soles!")
        budget += int(valin)*3
        print("Tu saldo es ahora", budget, 'soles')
    def numwin():
        global valin
        global budget
        print("¡Ganaste! ¡Ganaste! ¡Ganaste!")
        print("¡Felicitaciones!")
        print("¡Recibes", int(valin)*36, "soles!")
        budget += int(valin)*36
        print("Tu saldo es ahora", budget, 'soles')
    def lowwin():
        global valin
        global budget
        print("¡Enhorabuena, ganaste!")
        print("¡Recibes", int(valin)*2, "soles!")
        budget += int(valin)*2
        print("Tu saldo es ahora", budget, 'soles')
    def highwin():
        global valin
        global budget
        print("¡Ganaste!")
        print("¡Recibes", int(valin)*2, "soles!")
        budget += int(valin)*2
        print("Tu saldo es ahora", budget, 'soles')
    if 'apostarpar' in LOB and landon % 2 == 0:
        evenwin()
    if 'apostarpar' in LOB and landon % 2 != 0:
        lose()
    if 'apostarimpar' in LOB and landon % 2 == 1:
        oddwin()
    if 'apostarimpar' in LOB and landon % 2 != 1:
        lose()
    if 'apostar13' in LOB and landon < 13:
        win13()
    if 'apostar13' in LOB and landon >= 13:
        lose()
    if 'apostar23' in LOB and landon >= 13 and landon <= 25:
        win23()
    if 'apostar23' in LOB and landon < 13 or landon > 25:
        lose()
    if 'apostar33' in LOB and landon > 25:
        win33()
    if 'apostar33' in LOB and landon <= 25:
        lose()
    if 'num' in LOB and valnum == landon:
        numwin()
    if 'num' in LOB and valnum != landon:
        lose()
    if 'apostarpmitad' in LOB and landon < 19:
        lowwin()
    if 'apostarpmitad' in LOB and landon >= 19:
        lose()
    if 'apostarsmitad' in LOB and landon >= 19:
        highwin()
    if 'apostarsmitad' in LOB and landon < 19:
        lose()