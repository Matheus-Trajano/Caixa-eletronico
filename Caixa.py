print("cédulas diponíveis para saque:\n"
      " R$200,00 \n R$100,00 \n R$50,00\n R$20,00\n R$10,00\n R$5,00\n R$2,00\n R$1,00 ")

saque = int(input("Valor que você deseja sacar em reais: "))

print(f"O valor aprovado para saque é: R${saque},00")
duzentos = int(saque / 200)
saque = saque - (duzentos * 200)

cem = int(saque / 100)
saque = saque - (cem * 100)

cinquenta = int(saque / 50)
saque = saque - (cinquenta * 50)

vinte = int(saque / 20)
saque = saque - (vinte * 20)

dez = int(saque / 10)
saque = saque - (dez * 10)

cinco = int(saque / 5)
saque = saque - (cinco * 5)

dois = int(saque / 2)
saque = saque - (dois * 2)

um = int(saque)

print(f"notas de R$200,00: {duzentos}\n"
      f"notas de R$100,00: {cem}\n"
      f"notas de R$50,00: {cinquenta}\n"
      f"notas de R$20,00: {vinte}\n"
      f"notas de R$10,00: {dez}\n"
      f"notas de R$5,00: {cinco}\n"
      f"notas de R$2,00 {dois}\n"
      f"notas de R$1,00: {um}\n"
      f"Obrigado por utilizar nosso serviço de caixa, volte sempre.\n")
