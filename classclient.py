
class Client:
	def __init__(self,id,nom,age,solde):
		self.id=id
		self.nom=nom
		self.age=age
		self.solde=solde
		print("le solde du client  ",nom," est : ",solde)
	def depot(self):
		sum=float(input("entrez le montant à verser :"))
		self.solde=self.solde+sum-self.solde
		print("vous avez ajouté : \n", self.solde)
	def retrait(self):
		sum=float(input("entrez le montant à retirer : "))
		self.solde=self.solde+sum-self.solde
		print("Vous avez retiré :\n ",self.solde)
	def virrement(self):
		sum =float(input("Combien souhaitez-vous transférer? "))
		if sum<=self.solde:
			self.solde=self.solde+sum-self.solde
			print("Vous avez effectuer un virrement de :",self.solde)
		else:
			print("Désolé votre solde est insuffisant")
c= Client(0,"GROUPE15TP",18,50000)
c.depot()
c.retrait()
c.virrement()

