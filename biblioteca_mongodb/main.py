from app.services.biblioteca_service import *

inserisci_libri()

fantasy = trova_fantasy_disponibili()

print("LIBRI FANTASY DISPONIBILI")

for libro in fantasy:
    print(libro)

registra_prestito("Il Signore degli Anelli")

print("\nAGGREGAZIONE")

for r in aggrega_per_genere():
    print(r)

crea_indici()

soft_delete("Harry Potter")