# -*- coding: utf-8 -*-
# Inizializzo una variabile per la somma
somma = 0

# Continuo a chiedere numeri finché l'utente non inserisce zero
while True:
    # Chiedo un numero all'utente
    numero = int(input("Inserisci un numero intero (0 per terminare): "))
    
    # Se il numero è zero, interrompo il ciclo
    if numero == 0:
        break
    
    # Aggiungo il numero alla somma
    somma += numero

# Stampo la somma totale
print("La somma di tutti i numeri inseriti è:", somma)

