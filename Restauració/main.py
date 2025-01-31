# main.py

from magatzem import *
from quiosc import *

end = False
despensa = Despensa()
frigo = Frigo()
magatzem = [despensa, frigo]
quiosc = Quiosc()

print("\n*** UPC Restauració ***")


while not end:
    print("\nMenú Principal:")
    print("1. Registrar usuari")
    print("2. Veure categories")
    print("3. Veure productes per categoria")
    print("4. Fer encàrrec")
    print("5. Consultar top vendes")
    print("6. Sortir")

    opcio = input("Selecciona una opció: ")

    if opcio == "1":
        usuari = input("Introdueix ID d'usuari: ")
        nom = input("Introdueix nom d'usuari: ")
        if quiosc.registrar_usuari(usuari, nom):
            print(f"Usuari {usuari} registrat!")
        else:
            print("[!] Error: L'usuari ja existeix")
    elif opcio == "2":
        print("Categories disponibles:")
        print(quiosc.obtenir_categories())
    elif opcio == "3":
        print(quiosc.obtenir_categories())
        categoria = input("\nIntrodueix el nom de la categoria: ")
        if categoria in quiosc.obtenir_categories():
            productes_categoria = quiosc.obtenir_productes_per_categoria(categoria)
            print(f"Productes de la categoria '{categoria}':")
            for p in productes_categoria:
                print(f"ID: {p['id']} | Nom: {p['nom']} | Preu: {p['preu']}€ | Categoria: {p['categoria']}")
        else:
            print("[i] Categoria no trobada")
    elif opcio == "4":
        usuari = input("Introdueix el teu ID d'usuari: ")
        if usuari not in quiosc.get_usuaris():
            print("[!] Error: Has de registrar-te abans de fer un encàrrec")
            continue
        productes_encarrec = []
        print("Escull productes (escriu 'fi' per acabar):")
        fi = False
        while fi == False:
            producte_id = input("ID del producte: ")
            if producte_id.lower() == "fi":
                fi = True
            producte = next((p for p in productes if p["id"] == producte_id), None) # https://www.w3schools.com/python/ref_func_next.asp
            if producte != None:
                productes_encarrec.append(producte)
                ventes[producte_id] = ventes.get(producte_id, 0) + 1
                print(f"Producte afegit: {producte['nom']}")
            else:
                print("ID no valid")
        if productes_encarrec != None:
            quiosc.realitzar_encarreg(usuari, productes_encarrec)
            print("[i] Encàrrec realitzat amb exit!")
        else:
            print("[i] Encàrrec buit")
    elif opcio == "5":
        ranking = quiosc.top_vendes()
        if ranking != None:
            print("Top productes més venuts:")
            for producte in ranking:
                print(f"ID: {producte.get_id()} | Nom: {producte.get_nom()} | Vendes: {producte.get_vendas()}")
        else:
            print("[i] Encara no hi ha vendes registrades")
    elif opcio == "6":
        print("Fins aviat!")
        end = True
    else:
        print("[i] Opcio no valida")
