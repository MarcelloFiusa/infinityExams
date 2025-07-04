right_answer = 7
tries = 3
answer = 0
while tries > 0:
    try:
        answer = int(input("Qual é o número inteiro sorteado? Digite algum para tentar adivinhar: "))
        if answer == right_answer:
            print("Temos um houdini entre nós?? Parabéns, você acertou!!")
            break
        else:
            tries -= 1
            if tries > 0:
                print(f"PEEEEN! Errou! Restam {tries} tentativas!")
    except ValueError:
        print("Esse não é um valor inteiro! Tente novamente")
if tries == 0:
    print("Infelizmente acabaram as tentativas.. Volte amanhã!")