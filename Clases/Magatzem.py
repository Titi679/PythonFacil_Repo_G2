from functools import reduce

class Quiosc:
    def _init_(self, magatzem):
        self.magatzem = magatzem
        self.usuaris = {}
        self.encarrecs = []
        self.ventes = []

    # def registrar_usuari(self, usuari_id):
    #     self.usuaris[usuari_id] = []

    # def consultar_categories(self, es_fred):
    #     categories = set()
    #     prestatges = self.magatzem.prestatges_fred if es_fred else self.magatzem.prestatges_despensa
    #     for prestatge in prestatges:
    #         for nivell in prestatge.nivells:
    #             if nivell.categoria:
    #                 categories.add(nivell.categoria)
    #     return list(categories)

    def realitzar_encarrec(self, usuari_id, productes):
        if usuari_id in self.usuaris:
            self.encarrecs.append((usuari_id, productes))
            self.usuaris[usuari_id].append(productes)
        else:
            print("Error: Usuari no registrat.")


class Magatzem:
  def __init__(self):
    self.espai = []
  
  def get_p(self, pos):
    for prestatge in self.espai:
      if prestatge.get_pos() == pos:
        return prestatge

  #def organitzar(self, Producte):
    # Codi
  
  def add(self, Contenidor):
    pos = self.organitzar(Contenidor.get_pr(Producte))
    Contenidor.set(pos)
    for prestatge in self.espai:
      if prestatge.get_pos() == pos:
        prestatge.add(Contenidor)
  
  def delete(self, Contenidor):
    pos = Contenidor.get_pos
    i = 0
    while i < len(self.espai) and not end:
      if self.espai(i).get_pos() == pos:
        end = True
    self.espai(i).eliminar()

class Despensa(Magatzem):
  def __init__(self):
    x = 0
    while x < 4:
      y = 0
      while y < 12:
        prestatge = Prestatge((x,y))
        self.espai.append(prestatge)

class Frigo(Magatzem):
  def __init__(self):
    x = 0
    while x < 4:
      y = 0
      while y < 4:
        prestatge = Prestatge((x,y))
        self.espai.append(prestatge)

class Prestatge:
  def __init__(self, pos):
    self.pos = (pos[0], pos[1])
    self.quantitat = 0
    self.continguts = []
  
  def getq(self):
    return reduce(lambda acc, contingut: acc + contingut.get_q(), self.continguts, 0)
  
  def get_pos(self):
    return self.pos

  def add(self, Contenidor):
    self.quantitat = self.quatitat + Contenidor.get_q()
    i = len(self.continguts)
    self.continguts.append(Contenidor)
    while i > 0:
      self.continguts[i] = self.continguts[i-1]
    self.continguts[0] = Contenidor

class Contenidor:
  def __init__(self, quantitat, producte):
    self.quantitat = quantitat
    self.producte = producte
  
  def get_pr(self):
    return self.producte

  def get_q(self):
    return self.quantitat
  
  def set(self, pos):
    self.pos = pos

class Producte:
  def __init__(self, id, nom, preu, categoria, vendas, fred):
    self.id = id
    self.nom = nom
    self.preu = preu
    self.categoria = categoria
    self.vendas = vendas
    self.fred = fred

    def afegir_venda(self):
      self.vendas += 1

  def __str__(self):
    return f"id: {self.id} nom: {self.nom} preu: {self.preu} categoria: {self.categoria}"

def add_pr_m(producte):
  pos = org(producte)




despensa = Despensa()
frigo = Frigo()
magatzem = [despensa, frigo]

Producte1 = Producte("oli5", "oli verge extra", 32, "olis", 0, False)
Producte2 = Producte("wine1", "Blanc Pescador",  10, "begudes", 0, False)
Producte3 = Producte("wine2", "Albariño", 14, "begudes", 0, False)

Contenidor11 = Contenidor(50, Producte1)
Contenidor12 = Contenidor(25, Producte1)
Contenidor2 = Contenidor(50, Producte1)
Contenidor3 = Contenidor(50, Producte1)
