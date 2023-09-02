


print('Bem vindos ao NewWordGues')


palavras_dicas = {
    'roteador': 'Dispositivo responsável por encaminhar pacotes de dados entre diferentes redes.',

    'protocolo': 'Conjunto de regras que define como os dados são transmitidos e recebidos em uma rede.',  
    'switch': 'Dispositivo de rede que opera na camada de enlace do modelo OSI, utilizado principalmente em LANs para interconectar dispositivos. ',
    'ethernet': 'Tecnologia de rede padrão usada para interconectar computadores e outros dispositivos em uma LAN.', 
    'wireless': 'Rede de computadores na qual a conexão entre dispositivos é feita sem o uso de cabos, utilizando principalmente ondas de rádio ou infravermelho. ',
    'repetidor': 'Dispositivo usado para receber e retransmitir sinais, ampliando assim o alcance desses sinais.' ,
    'PAN': 'Redes de curtíssima distância  visam interconectar dispositivos em um mesmo ambiente.',
    'WAN': 'Redes projetadas para cobrir distâncias de até milhares de quilômetros, como um país ou continente.'
 
}


import random 

palavra_selecionada =random.choice(list(palavras_dicas.keys()))
dica=palavras_dicas[palavra_selecionada]

tentativas = 8
palavra_display =['_'] *len(palavra_selecionada)

# Inicia um loop que continuará enquanto o jogador tiver tentativas restantes
# e ainda não tiver adivinhado a palavra correta
while tentativas > 0 and ''.join(palavra_display) != palavra_selecionada:
    
    # Imprime a representação atual da palavra com sublinhados nas posições das letras não adivinhadas
    print(' '.join(palavra_display))
    
    # Exibe a dica para a palavra atual
    print(f"Dica: {dica}")
    
    # Informa ao jogador o número de tentativas que ele ainda tem
    print(f"Tentativas restantes: {tentativas}")
    
    # Solicita ao jogador para inserir (adivinhar) uma letra e a converte para minúscula
    chute = input("Adivinhe uma letra: ").lower()

    # Verifica se a letra adivinhada pelo jogador está na palavra selecionada
    if chute in palavra_selecionada:
        
        # Se estiver, percorre cada letra da palavra selecionada
        for index, letra in enumerate(palavra_selecionada):
            
            # Para cada ocorrência da letra adivinhada, atualiza a lista de display na posição correspondente
            if letra == chute:
                palavra_display[index] = chute
                
    # Se a letra adivinhada não estiver na palavra selecionada, reduz o número de tentativas do jogador
    else:
        print ('Esta palavra não contém essa letra, tente novamente.')
        tentativas -= 1
