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

email_er = re.compile(r'^[\w._-]{2,}@[\w._-]+\.[a-z]{3}(\.(br|ao|pt|es|de|uk))?$')
email = input("Digite seu e-mail: ")
print(email_er.match(email))

# Telefone
telefone_er = re.compile(r'^(\d{11}|\(\d{2}\)\d{5}-\d{4})$')
telefone = input("Digite seu telefone: ")
print(telefone_er.match(telefone))

# Extraindo e-mails validos de um texto
