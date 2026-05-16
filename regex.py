import re

# nome
nome_er = re.compile('^[a-zA-Z ]+$')
nome = input("Digite seu nome: ")
print(nome_er.match(nome))

# CPF
cpf_er = re.compile(r'(\d{3}\.\d{3}\.\d{3}-\d{2})|\d{11}')
cpf = input("Digite seu CPF: ")
print(cpf_er.match(cpf))
 
# E-mail


# Telefone


# Extraindo e-mails validos de um texto
