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
    print (f"Su Resultado Fue De [{valor_user}] Y El Resultado Es [{calculo()}]")
    print (f"Tubo un puntage del {valor_user/calculo()*100}%")

if __name__ ==  '__main__':
    main()