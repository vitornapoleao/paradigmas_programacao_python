print("Bem vindos a fabulosa maquina de conversão de temperaturas")
print("Com esta ferramenta você consegue converter celsius para farenheit e vice versa!")
T = input("escolha celsios ou farenheit com C ou F:")
if T == "C" or T == "c":
    C = int(input("Insira a temperatura em celsius:"))
    faren = C * 1.8 + 32
    print("A temperatura em Farenheit é %d Farenheit:" %(faren))
if T == "F" or T == "f":
    F = int(input("Insira a temperatura em Farenheit:"))
    celsius = (F - 32) / 1.8
    print("A sua temperatura em Celsius é: %d Celsius! " %(celsius))
else:
    print("Input invalido favor inserir um input correto meu consagrado!")
