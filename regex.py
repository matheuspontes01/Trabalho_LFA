# Trabalho feito por: Matheus Silva Pontes & Lucas Monteiro de Carvalho

import re

# nome
nome_er = re.compile(r'^[a-zA-Z ]{1,50}$')
nome = input("Digite seu nome: ")
print(nome_er.fullmatch(nome))

# CPF
cpf_er = re.compile(r'^(\d{11}|\d{3}\.\d{3}\.\d{3}-\d{2})$')
cpf = input("Digite seu CPF: ")
print(cpf_er.fullmatch(cpf))

# E-mail
email_padrao = r'(?=[\w.\-]{2,}@)[\w\-]([\w.\-]*[\w\-])?@(?=[\w.\-]{2,}\.)[\w\-]([\w.\-]*[\w\-])?\.[a-z]{3}(?:\.(?:br|ao|pt|es|de|uk))?'
email_er = re.compile(r'^' + email_padrao + r'$')
email = input("Digite seu e-mail: ")
print(email_er.fullmatch(email))

# Telefone
telefone_er = re.compile(r'^(\d{11}|\(\d{2}\)\d{5}-\d{4})$')
telefone = input("Digite seu telefone: ") 
print(telefone_er.fullmatch(telefone))

# Extraindo e-mails validos de um texto
texto = """
Prezado usuário,

Aqui estão os contatos do nosso time de suporte:

- alice.souza@gmail.com

- suporte_23@empresa-tech.com

- joao99@dominio123.org

- erro.email@gmail..com

Por favor, envie suas dúvidas para qualquer um dos e-mails válidos acima.

Atenciosamente,

Equipe de Atendimento
"""

emails_validos = [m.group() for m in re.finditer(email_padrao, texto)]
print("E-mails válidos encontrados:")
print(emails_validos)