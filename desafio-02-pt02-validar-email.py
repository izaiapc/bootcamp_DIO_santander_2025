# Explorando Operadores e Manipulação de Strings
# 2 / 2 - Validador de Formato de E-mails

# Entrada do usuário
# Aqui o input é vazio porque o proprio sistema da DIO faz o teste
email = input().strip() 

# TODO: Verifique as regras do e-mail:
def validar_email(email):
  # Deve conter o caractere "@" e um domínio, como gmail.com ou outlook.com.  
  if "@" not in email or "." not in email.split("@")[-1]: return "E-mail inválido"
  
  # Não pode começar ou terminar com "@".
  if email.startswith("@") or email.endswith("@"): return "E-mail inválido"
  
  # Não pode conter espaços.
  if " " in email: return "E-mail inválido"
  
  # E-mail valido caso não passe por dentro dos IFs anteriores
  return "E-mail válido"

# Chama o método validar_email que retornará a string "E-mail inválido" ou "E-mail inválido" conforme os requisitos do desafio
print(validar_email(email))