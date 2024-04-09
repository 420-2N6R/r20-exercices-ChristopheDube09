from datetime import datetime

class CompteBancaire :
    def __init__(self, compte_holder, listeTransactions, balance=0) :
            self. compte_holder = compte_holder
            self.balance = balance
            self.transact = listeTransactions
            

    def deposer(self):
          Valeur = 10
          self.balance += Valeur
          print(f"Un montant de {Valeur} $ a été deposé sur votre compte bancaire vers {self.transact}. Voir compte est rendu a {self.balance} $")
          
    def retirer(self):
      Valeur = 10
      if self.balance - Valeur >= 0 :
            self.balance - Valeur
            print(f"Un montant de {Valeur} $ a été retiré sur votre compte bancaire vers {self.transact}.. Voir compte est rendu a {self.balance} $")
      else :
          print(f"Il ny a pas assez de fond dans le compte pour faire ce retrait. Voici les fonds de votre compte : {self.balance}")

    def transac(self) :
         print(f"{self.__temps_maintenant()}")
      

    @staticmethod
    def __temps_maintenant():
          return datetime.now().strftime("%H:%M:%S")
    
compte = CompteBancaire(compte_holder ="Alice", balance=1000)
compte.deposer(500)
compte.retirer(200)


