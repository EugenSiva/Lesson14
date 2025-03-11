from abc import ABC, abstractmethod

class Zviera(ABC):
    @abstractmethod
    def zvuk(self):
        pass

class Macka(Zviera):
    def zvuk(self):
        return "Mnau"

moje_zviera = Zviera()

moja_macka = Macka()
print(moja_macka.zvuk())