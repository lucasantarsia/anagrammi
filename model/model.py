import copy
from time import time
from functools import lru_cache


class Model:
    def __init__(self):
        self._anagrammi = set()
        self._anagrammi_list = []

    def calcola_anagrammi(self, parola):
        self._anagrammi = set()  # potrei anche usare una lista, ma uso un set nel caso in cui ci siano anagrammi ripetuti
        self.ricorsione("", "".join(sorted(parola)))  # ordino la parola in modo tale da migliorare l'efficienza
                                                              # in questo modo potrei avere la sequenza delle lettere rimanenti in più branch diversi
        return self._anagrammi

    @lru_cache(maxsize=None)
    def ricorsione(self, parziale, lettere_rimanenti):
        """
        :param parziale: stringa inizialmente vuota a cui man mano aggiungeremo le lettere rimanenti, fino a
                         formare un anagramma
        :param lettere_rimanenti: stringa che inizialmente corrisponde alla parola iniziale, che si svuoterà man mano
                                  che le lettere della parola vanno in parziale
        """
        # Caso terminale: non ci sono lettere rimanenti perchè le ho messe tutte in parziale
        if len(lettere_rimanenti) == 0:
            self._anagrammi.add(parziale)
            return
        else:
            # Caso non terminale: dobbiamo provare ad aggiungere una lettera per volta,
            # e andare avanti nella ricorsione
            for i in range(len(lettere_rimanenti)):
                parziale += lettere_rimanenti[i]
                nuove_lettere_rimanenti = lettere_rimanenti[:i] + lettere_rimanenti[i+1:]  # devo saltare l'i-esima lettera perchè l'ho già messa in parziale
                self.ricorsione(parziale, nuove_lettere_rimanenti)
                parziale = parziale[:-1]  # back trakking: mi serve per risalire di livello

    def calcola_anagrammi_list(self, parola):
        self._anagrammi_list = []
        self.ricorsione_list([], parola)
        return self._anagrammi

    @lru_cache(maxsize=None)
    def ricorsione_list(self, parziale, lettere_rimanenti):
        """
        Questa volta parziale è una lista e non più una stringa
        """
        # caso terminale: non ci sono lettere rimanenti
        if len(lettere_rimanenti) == 0:
            self._anagrammi_list.append(copy.deepcopy(parziale))  # vogliamo passare una copia di parziale e non il suo riferimento
            return
        else:
            # caso non terminale: dobbiamo provare ad aggiungere una lettera per volta,
            # e andare avanti nella ricorsione
            for i in range(len(lettere_rimanenti)):
                parziale.append(lettere_rimanenti[i])
                nuove_lettere_rimanenti = lettere_rimanenti[:i] + lettere_rimanenti[i+1:]
                self.ricorsione_list(parziale, nuove_lettere_rimanenti)
                parziale.pop()


if __name__ == "__main__":
    model = Model()

    start_time = time()
    print(model.calcola_anagrammi("casasasa"))
    end_time = time()
    print(end_time - start_time)

    #print(model.calcola_anagrammi_list("Dog"))
