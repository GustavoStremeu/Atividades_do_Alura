#1. Armazene uma frase dentro de uma variável e depois exiba a mesma na tela.
frase = str(input("Qual é o seu nome?"))
print (frase)

#2. Exiba uma mensagem de boas vindas para o usuário de acordo com o valor digitado.

nome = str (input("Digite seu nome: "))
print ("Olá, seja bem vindo!!!" , nome )

#3. Crie um script onde exiba o nome da pessoa, e sua data de aniversário formatada.

nome = str(input("Qual é o seu nome?"))
dia = int(input("Qual é o dia do seu aniversário?"))
mes = int(input("Qual é o mes do seu aniversário?"))
ano = int(input("Que ano você nasceu ?"))
print ("Olá", nome,"você nasceu no dia ",dia,"/",mes,"/",ano)

#4. Crie um programa que leia dois números e mostre a soma entre eles.

numero1 = int(input("Digite qualquer número: "))
numero2 = int(input("Digite qualquer número novamente: "))
print ("A soma dos dois números digitados são:",numero1 + numero2 )

#5 Faça um programa que receba um valor, e traga informações sobre esse valor, dizendo se é alfanumérico, numérico e etc.

digite = input('Digite algo para que o item seja verificado:')
print('O tipo primitivo desse dado é:', type(digite))
print('Só tem espaços?', digite.isspace())
print('É um número?', digite.isnumeric())
print('É uma letra?', digite.isalpha())
print('É alfanumérico?', digite.isalnum())
print('É uma letra maiúscula?', digite.isupper())
print('É uma letra minúscula?', digite.islower())
print('É um título?',digite.istitle())

# 6 Faça um programa que mostre a soma de dois valores, e depois mostre o antecessor e o sucessor do mesmo.

numero = int(input("Digite um número:"))
antecessor = numero - 1
sucessor = numero + 1

print ("O número escolhido foi",numero,", seu sucessor é",sucessor,", e o antecessor é",antecessor)

#7 Leia um número, mostre seu dobro, triplo, e raíz quadrada.

numer = int(input("Digite um número e será mostrado o dobro, o triplo, e a raíz quadrada."))
dobro = numer * 2
triplo = numer * 3
raiz =  pow(numer, 1/2)
print ("O dobro do número digitado é",dobro,", o triplo é",triplo,"E a raiz quadrada é",raiz)

#8 Desenvolva um programa que receba duas notas de um aluno e calcule sua média.

nota1 = int(input("Digite sua primeira nota:"))
nota2 = int(input("Digite sua segunda nota:"))
media = nota1 + nota2
print ("A media das notas é",media /2)

#9  Faça um programa que leia um valor em metros, mostre o valor convertido em centímetros, e milímetros.

num = int(input("Digite uma medida em metros:"))
cm = num *100
milimetros = num *1000
print ("Metros convertido para centímetros é igual a:",cm," e convertido para milímetros é:", milimetros)

#10 Faça um programa que leia um valor, e mostre a sua tabuada do 1 ao 10 na tela.

nu = int(input("Digite o número que deseja a tabuada:"))
print ("A tabuada de",nu,"é:")
print (nu * 0)
print (nu * 1)
print (nu * 2)
print (nu * 3)
print (nu * 4)
print (nu * 5)
print (nu * 6)
print (nu * 7)
print (nu * 8)
print (nu * 9)
print (nu * 10)
print ("Fim da atividade :]")