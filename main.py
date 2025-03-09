import translator as tr

t = tr.Translator()
t.loadDictionary("dictionary.txt")

while(True):

    t.printMenu()



    txtIn = input("Inserire il numero della funzione che si vuole azionare")

    if txtIn.isdigit():

        if int(txtIn) == 1:
            t.stampaDizio()

        if int(txtIn) == 2:
            newWord = input("Inserisci prima la parola Aliena e poi le traduzioni:")
            parola = newWord.split(" ")
            tupla = (parola[0], parola[1:])
            t.handleAdd(tupla)

        if int(txtIn) == 3:
            daTradurre = input("Inserisci una nuova parola aliena per la traduzione:")
            if daTradurre.isalpha():
                t.handleTranslate(daTradurre)
            else: print("Errore nella parola")

        if int(txtIn) == 4:
            cercare = input("Inserire una parola aliena:")
            cnt = 0
            for lettera in cercare:
                if lettera == "?":
                    cnt += 1

            if cercare.isascii() and cnt == 1:
                cercare.split()
                t.handleWildCard(cercare)

            else: print("Errore nella parola")

        if int(txtIn) == 5:
            t.copiaDizionario("dictionary.txt")
            break