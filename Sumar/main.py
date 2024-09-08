from random import randrange

def main():
    print('\t\t "Ejercita tu mente sumando numeros"')

    ciclos = int(input('Defina la cantidad de Calculos a realizar: \n\t-> '))
    valor_minimo = int(input('Defina el valor minimo para la suma: \n\t-> '))
    valor_maximo = int(input('Defina el valor maximo para la suma: \n\t-> '))

    list_namber = []
    for i in range(ciclos):
        print(f"Valor {i+1}")
        number_ramdom = randrange(valor_minimo, valor_maximo + 1)
        print (number_ramdom)
        list_namber.append(number_ramdom)
        input('Presiones enter para continuar ...')
    
    valor_user= int(input("Ingrase el valor calculado: "))
    def calculo():
        resul = 0
        for i in list_namber:
            resul += i
        return resul
    def promedio(valueUser, value):
        if valueUser > value:
            return round(value/valueUser*100, 2)
        else:
            return round(valueUser/value*100, 2)

    print (f"Su Resultado Fue De [{valor_user}] Y El Resultado Es [{calculo()}]")
    print(f"Su porcentage de asertacion fue de {promedio(valor_user, calculo())}%")

if __name__ ==  '__main__':
    main()
        
