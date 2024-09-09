from random import randrange
def main():
    
    operation = ('Suma', 'Resta')
    
    
    def recInfo():
        count_operation= int(input("Defina la cantidad de operaciones a realizar: \n\t-> "))
        valor_minimo= int(input("Ingrse el rango de valor minimo para calcular: "))
        valor_maximo= int(input("Ingrse el rango de valor maximo para calcular: "))
        return [count_operation, valor_minimo, valor_maximo]
    
    def outnumberoperation(data):
        value = 0

        def outputOperation(operation, value):
            print(f"{operation}: {value}")

        
        for i in range(data[0]):

            valueRandom= randrange(data[1], data[2]+1)
            
            operationRandom = operation[randrange(0, 2)]
            
            #Esto lo que indica es que como en todas las cuentas a sacar portimos de cero y se nos asigna un valor
            if value <= 0:
                operationRandom = operation[0]
            
            if operationRandom == operation[0]:
                value += valueRandom
                outputOperation(operationRandom, valueRandom)
            elif operationRandom == operation[1]:
                if (value - valueRandom) < 0:
                    value += valueRandom
                    outputOperation(operation[0], valueRandom)
                else:
                    outputOperation(operationRandom, valueRandom )
                    value -= valueRandom
            input("Presione Enter Para continuar...")
        return value


    def promedio(valueUser, value):
        if valueUser > value:
            return round(value/valueUser*100, 2)
        else:
            return round(valueUser/value*100, 2)


#Inicio del programa..
    print('\t\t "Ejercita tu mente sumando y restando numeros"')
    value =outnumberoperation(recInfo())
    valueUser= int(input("Cual fue su resultado: "))
    print(f"Su resultado fue de {valueUser} y el resultado correcto es {value}") 
    print(f"Su porcentage de asertacion fue de {promedio(valueUser, value)}%")


if __name__ == '__main__':
    main()
