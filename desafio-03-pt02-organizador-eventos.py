# Dicionário para agrupar participantes por tema
eventos = {}

# Entrada do número de participantes
n = int(input('numero: ').strip())

for _ in range(n):
    linha = input('Digite participante e hobby no formato participate,hobby: ').strip()
    participantes,tema = linha.split(",")
    if tema not in eventos:
        eventos[tema] = []
    eventos[tema].append(participantes)
# Exibe os grupos organizados
for tema, participantes in eventos.items():
    print(f"{tema}: {', '.join(participantes)}")

print(eventos)