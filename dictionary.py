class Dictionary:
    def __init__(self):
        self.dizionario = None

    def aggiorna(self, dizionario):
        self.dizionario = dizionario

    def aggiungiParola(self, chiave, lista):
        for i in lista:
            self.dizionario[chiave].append(i)

    def addWord(self, chiave, lista):
        self.dizionario[chiave] = lista

    def stampa(self):
        out =""
        for chiave, valore in self.dizionario.items():
            out += chiave+" "
            for i in valore:
                out += i
                out += " "
            out+="\n"
        return out

    def translate(self, parola):
        out = ""
        for i in self.dizionario[parola]:
            out += i+" "

        return out

    def translateWordWildCard(self, query):
        out=""
        lista1 = []
        for lettera in query:
            lista1.append(lettera)
        for i in self.dizionario:
            listap = []
            for lettera in i:
                listap.append(lettera)

            if len(lista1)==len(listap):
                flag = True
                for c in range(0,len(lista1)):
                    if lista1[c]!=listap[c] and lista1[c]!="?":
                        flag = False

                if flag:
                    for t in self.dizionario[i]:
                        out += t+" "

        return out

    def scrivi(self):
        infile = open("dictionary.txt", "w")
        for chiave, valori in self.dizionario.items():
            out = chiave + " "
            for i in valori:
                out += i+" "

            infile.writelines(out+"\n")
        infile.close()