print("\\\\\\\\\\\\\\ Maquina de Conversão version 1.1 ////////////////// ")
print("Bem vindo a fabulosa maquina de Conversão de Temperaturas!")
print("Escolha a escala a ser convertida, Celsius ou Farenheit!")
escala = int(input("Insira:\n1.-Para Celsius.\n2.-Para Farenheit."))
escala_1 = "Celsius"
escala_2 = "Farenheit"
scale_chose = ""
temperatura = 0
if escala == 1:
    numero = int(input("insira uma temperatura em %s:" %(escala_1)))
    temperatura = numero + temperatura
    generic = temperatura * 1.8 + 32
    scale_chose = scale_chose + escala_2
    
if escala == 2:
    numero = int(input("insira uma temperatura em %s:" %(escala_2)))
    temperatura = numero + temperatura
    generic = (temperatura - 32) / 1.8
    scale_chose = scale_chose + escala_1

print("Sua temperatura é %d em %s!" %(generic,scale_chose))
