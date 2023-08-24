print("\\\\\\\\\\\\\\ Maquina de Conversão version 1.2 ////////////////// ")
print("Bem vindo a fabulosa maquina de Conversão de Temperaturas!")
print("Escolha a escala a ser convertida, Celsius ou Farenheit!")
escala = int(input("Insira:\n1.-Para Celsius.\n2.-Para Farenheit: "))
escala_1 = "Celsius"
escala_2 = "Farenheit"
scale_chose = ""

while escala == 1:
    numero = int(input("Insira uma temperatura em celsius:"))
    generic = numero * 1.8 + 32
    scale_chose = scale_chose + escala_2
    
    
while escala == 2:
    numero = int(input("Insira sua temperatura em Farenheit:"))
    generic = (numero - 32) / 1.8
    scale_chose = scale_chose + escala_1
    print("Sua temperatura convertida para %s é: %d" %(scale_chose,generic))
    break
    
if escala != 1 and escala != 2:
     escala = int(input("Input invalido insira um input valido 1 ou 2!"))
     
