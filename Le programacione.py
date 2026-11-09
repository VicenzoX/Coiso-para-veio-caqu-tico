bro = {"ss": "Sim Sim", "mn": "Mano","vdd": "verdade", "gg": "Significa bom jogo ou em outras palavras: jogo justo", "gnt": "Gente", "Cringe": "Não, somente não use-a PELA AMOR DE DEUS"}

playing = True

while playing:

    text = input("Insira aqui a giria para a traduzir-la")

    if text == bro.keys():
        print(bro[text])
    else:
        print("Não tem essa palavra!")
