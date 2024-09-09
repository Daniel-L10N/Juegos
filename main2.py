from random import randint

def entrada():
	Abrev = {
		"cantEj": "Cantidad de ejercicios",
		"valMin" : "Valor mínimo",
		"valMax" : "Valor máximo",
	}
	datos = {
			"cantEj":1,
			"valMin":
			0,
		  "valMax":0
	}
	for key in datos.keys():
		while True:
			text = input(f"\t{Abrev[key]}: ")
			if not text.isdigit():
				print ("Error: Solo se admiten números.\n")
				continue
			num = int(text)
			if num <= datos[key]:
				print (f"Error: El valor debe ser mayor a {datos[key]}\n")
				continue
			if key =="valMax" and num <= datos["valMin"]:
				print ("Error: El valor máximo debe ser mayor al valor mínimo\n")
				continue
				
			datos [key]= num
			break
	if datos["valMin"] >= datos["valMax"]:
		print(datos["valMin"], datos["valMax"])
	return datos 
def output(op, dato):
	print(f"{op} : {dato}")
	

def calcResult(datos):
	res =0
	print("\n¡Comencemos!")
	print("¿Cuánto da el resultado de las siguientes operaciones?\n")
	for i in range(datos["cantEj"]):
		if i == 0:
			randOp = 0
		else:
			randOp = randint(0,4)
			
		min = datos["valMin"]
		max = datos["valMax"]
		operaciones =["Suma", "Resta", "Multiplica", "Divide"]
		randNum = randint(min,max)
		if res <= 0: 
			randOp=0
		if randOp == 1 and (res -min) <0:
			randOp=0
			
		def operar(tipo, fn):
			nonlocal res
			if randOp == tipo:
			  res = fn(res, randNum)
			  output(
					operaciones[tipo],
					randNum
				)
		
		operar(0, lambda rs,num : rs+num)
		operar(1, lambda rs,num : rs-num)
		operar(2, lambda rs,num : rs*num)
		operar(3, lambda rs,num : rs/num)
		
	return res
def calcPorcAciert(usRes, res):
	res+=1
	usRes+=1
	if usRes > res:
		return res/usRes
	else:
		return usRes/res
			


print('"Ejercita tu mente sumando y restando números"\nConfiguración:')
datos = entrada()
res = calcResult(datos)
usRes=0
while True:
	usResStr = input("\nResultado: ")
	try:
	  usRes = float(usResStr)
	except:
		print("Error: Solo se admiten números.\n")
		continue
	if usRes<0:
		print("Error: El resultado no puede ser negativo.\n")
		continue
	break
porcAciert = calcPorcAciert(usRes, res)
print(f"Respuesta correcta: {res}")
print(f"Su porcentaje de acierto es del: {(porcAciert*100):.2f}%")

	
