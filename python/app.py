#le variabili non hanno bisogno di essere dichiarate, basta assegnare un valore e non hanno
#un tipo specifico, possono essere di qualsiasi tipo e cambiare tipo durante l'esecuzione del programma

citta = "Milano" #i doppi apici indicano che si tratta di una stringa, se usassi gli apici singoli sarebbe lo stesso, ma è buona pratica usare i doppi apici per le stringhe.
print(citta)
# = operatore di assegnazione, assegna il valore a sinistra alla variabile a destra.
# i nomi delle variabili devono essere parlanti, cioè devono descrivere il contenuto della variabile, devono essere scritti in minuscolo e separati da underscore se sono composti da più parole.
# non possono iniziare con un numero, non possono contenere spazi, non possono essere
# parole chiave riservate del linguaggio, non possono essere uguali a nomi di funzioni o classi già esistenti.
# le variabili sono case sensitive, cioè citta e Citta sono due variabili diverse.
# le variabili possono essere usate per memorizzare qualsiasi tipo di dato, come numeri, stringhe, liste, dizionari, ecc.
# le variabili possono essere usate per fare operazioni, come concatenare stringhe, fare operazioni matematiche, ecc.
# le variabili possono essere usate per passare valori a funzioni, per restituire valori da funzioni, per memorizzare risultati di operazioni, ecc.
# le variabili possono essere usate per creare oggetti, come classi, istanze, ecc.
# le variabili possono essere usate per creare moduli, pacchetti, ecc.
#print è una funzione built-in di Python che stampa a video il valore passato come argomento, in questo caso la variabile citta.
# non è un linguaggio fortemente tipizzato
numero = "42" # è comunque una stringa a meno che non si faccia un cast esplicito a int(numero) o float(numero)
print(numero)

età = 15 # è un numero intero, ma se si vuole rappresentare l'età in anni e mesi, si potrebbe usare una stringa del tipo "15 anni e 6 mesi" o una tupla del tipo (15, 6) o un dizionario del tipo {"anni": 15, "mesi": 6}
prezzo = 19.99 # è un numero decimale, chiamato float in Python. 
sono_ricco = False # è un valore booleano, che può essere True o False. In questo caso è False, ma se si vuole rappresentare la ricchezza in modo più dettagliato, si potrebbe usare una stringa del tipo "ricco" o "povero" o una tupla del tipo (True, "ricco") o un dizionario del tipo {"ricco": True, "stato": "ricco"}
print(sono_ricco)

#Operazioni con le variabili
#somma, sottrazione, moltiplicazione, divisione, resto, potenza

a = 5
b = 3
somma = a + b
sottrazione = a - b
moltiplicazione = a * b
divisione = a / b
resto = a % b
potenza = a ** b
#litteral 
#somma = a + b + 2 # è una somma di tre numeri, a, b e 2, che restituisce un numero intero. Se invece si scrivesse somma = a + b + "2" si otterrebbe un errore di tipo, perché non si possono sommare un numero intero e una stringa.
a = 6
print (somma) # la variabile somma non cambia, perché è stata assegnata prima del cambiamento di a, quindi somma è ancora 8, mentre se si scrivesse somma = a + b dopo il cambiamento di a, allora somma sarebbe 9.
division = 10 / 5 #2.0, perché la divisione in Python restituisce sempre un numero decimale, anche se il risultato è un numero intero. Se si vuole ottenere un numero intero come risultato della divisione, si può usare l'operatore di divisione intera //, che restituisce solo la parte intera del risultato, quindi 10 // 5 restituirebbe 2.
print(division)
#concatenazione di stringhe
nome = "Giovanni"
cognome = "Vacanti"
nominativo = nome + " " + cognome # la concatenazione di stringhe avviene con l'operatore +, che unisce le due stringhe e restituisce una nuova stringa. In questo caso nominativo sarà "Giovanni Vacanti", con uno spazio tra nome e cognome.
print(nominativo)

#funzione print 
print("ciao")
print(28)
nome = "pino"
print (nome)
print(10+5)

#E se volessi stampare, "Marco ha 28 anni"?
nome = "Marco"
eta = 28
print(nome + " ha " + str(eta) + " anni") 
#scanf input per far scrivere un input all'utente
nome = input("Inserisci il tuo nome: ") # la funzione input() permette di leggere
print("Ciao " + nome + "!")
#se volessi chiedere all'utente la sua età e stamparla?
eta = input("Inserisci la tua età: ") # la funzione input() restituisce sempre una stringa, quindi se si vuole ottenere un numero intero o decimale, è necessario fare un cast esplicito a int(eta) o float(eta)
print("Hai " + eta + " anni!")
cast = int(eta) # cast esplicito a int, che converte la stringa eta in un numero intero. Se la stringa non è un numero valido, si otterrà un errore di tipo.
print("Hai " + str(cast) + " anni!") # cast esplicito a str, che converte il numero intero cast in una stringa, in modo da poterlo concatenare con le altre stringhe. Se si omettesse il cast a str, si otterrebbe un errore di tipo, perché non si possono concatenare un numero intero e una stringa.
#retrivial di variabili

#liste
frutta = ["mela", "banana", "arancia"] # le liste sono collezioni ordinate di elementi, che possono essere di qualsiasi tipo, come stringhe, numeri, altre liste, ecc. Le liste sono mutabili, cioè si possono modificare dopo la loro creazione, aggiungendo, rimuovendo o modificando gli elementi. Le liste sono delimitate da parentesi quadre [] e gli elementi sono separati da virgole.
print(frutta[0]) # la prima posizione della lista è 0, quindi frutta[0] restituisce "mela", frutta[1] restituisce "banana" e frutta[2] restituisce "arancia". Se si prova a accedere a una posizione che non esiste, come frutta[3], si otterrà un errore di indice.
frutta.append("kiwi") # il metodo append() aggiunge un elemento alla fine della lista, quindi frutta diventa ["mela", "banana", "arancia", "kiwi"].
#Diventa LIFO, last in first out, l'ultimo elemento aggiunto è il primo ad essere rimosso, quindi se si usa il metodo pop() senza argomenti, si rimuove l'ultimo elemento della lista, in questo caso "kiwi", e frutta torna ad essere ["mela", "banana", "arancia"].
#quindi diventa uno stack, una struttura dati che segue la regola LIFO, dove si possono aggiungere elementi con append() e rimuovere elementi con pop(), sempre dall'ultimo elemento aggiunto.
print(frutta)

#come prendo gli elementi di una lista?
print(frutta[0]) # restituisce "mela"
seconda_frutta = frutta[1] # assegna "banana" alla variabile seconda_frutta
print(seconda_frutta) # stampa "banana"
#pop lista
ultima_frutta = frutta.pop() # rimuove l'ultimo elemento della lista, in questo caso "arancia", e lo assegna alla variabile ultima_frutta
print(ultima_frutta) # stampa "arancia"
#per sapere quanto è la lenghezza di una lista, si usa la funzione len(), che restituisce il numero di elementi presenti nella lista. In questo caso, dopo aver rimosso "arancia", la lista frutta contiene solo "mela" e "banana", quindi len(frutta) restituisce 2.
print(len(frutta)) # stampa 2


#dizionari sono simili alle mappe di java. E se io volessi accedere ad un elemento della lista che è accoppiato ad una chiave, come ad esempio "nome" o "cognome"?
persona = {"nome": "Giovanni", "cognome": "Vacanti", "età": 30} # i dizionari sono collezioni non ordinate di coppie chiave-valore, dove ogni chiave è univoca e viene usata per accedere al valore corrispondente. I dizionari sono mutabili, cioè si possono modificare dopo la loro creazione, aggiungendo, rimuovendo o modificando le coppie chiave-valore. I dizionari sono delimitati da parentesi graffe {} e le coppie chiave-valore sono separate da virgole, mentre la chiave e il valore sono separati da due punti :.
print(persona["nome"]) # restituisce "Giovanni", perché la chiave "nome" è associata al valore "Giovanni". Se si prova ad accedere a una chiave che non esiste, come persona["indirizzo"], si otterrà un errore di chiave.
#per aggiungere una nuova coppia chiave-valore al dizionario, si può semplicemente assegnare un valore a una nuova chiave, come persona["indirizzo"] = "Via Roma 1", che aggiunge la coppia chiave-valore "indirizzo": "Via Roma 1" al dizionario persona.
persona["indirizzo"] = "Via Roma 1"
# è una specie di tupla, una struttura dati immutabile che contiene un insieme di elementi ordinati, ma a differenza delle liste, le tuple non possono essere modificate dopo la loro creazione. Le tuple sono delimitate da parentesi tonde () e gli elementi sono separati da virgole.
#le tuple sono utili quando si vuole rappresentare un insieme di valori che non devono essere modificati, come ad esempio le coordinate di un punto, le date, ecc. Le tuple possono essere usate anche come chiavi di un dizionario, mentre le liste no, perché le chiavi di un dizionario devono essere immutabili.
coordinate = (10, 20) # è una tupla che rappresenta le coordinate di un punto in un piano cartesiano, dove 10 è la coordinata x e 20 è la coordinata y. Se si prova a modificare una tupla, come coordinate[0] = 15, si otterrà un errore di tipo, perché le tuple sono immutabili.
print(coordinate) # stampa (10, 20)
print (persona["nome"]) # restituisce "Giovanni", perché la chiave "nome" è associata al valore "Giovanni". Se si prova ad accedere a una chiave che non esiste, come persona["indirizzo"], si otterrà un errore di chiave.
#lista di dizionari
persone = [
    {"nome": "Giovanni", "cognome": "Vacanti", "eta": 30, "citta": "Roma"},
    {"nome": "Maria", "cognome": "Rossi", "eta": 25, "citta": "Milano"},
    {"nome": "Luca", "cognome": "Bianchi", "eta": 35, "citta": "Napoli"}
] # è una lista che contiene tre dizionari, ognuno dei quali rappresenta una persona con le chiavi "nome", "cognome" e "età". Per accedere al nome della seconda persona, si può usare persone[1]["nome"], che restituisce "Maria". 
print(persone[1]["nome"]) # stampa "Maria"

#io voglio stampare tutti i nomi delle persone presenti nella lista persone, come posso fare?
#persona è la varibile dopo in questo caso conserviamo la lista
for persona in persone: 
    print(persona["nome"],"ha",persona["eta"],"anni" + " " + "e vive in",persona["citta"])


#il dizionario è praticamente un oggetto ma è differente dal json perché quest'ultmo è solo testo, infatti, se io volessi convertire
#il dizionario in json...
import json
json_string = json.dumps(persone) #dict to string
print(json_string) # stampa la stringa JSON che rappresenta la lista di dizionari persone. La funzione json.dumps() converte un oggetto Python in una stringa JSON, che è un formato di testo leggero e facile da leggere e scrivere, usato per scambiare dati tra applicazioni web e server. La stringa JSON risultante è simile a una rappresentazione testuale del dizionario, ma con alcune differenze sintattiche, come l'uso di virgolette doppie per le chiavi e i valori, e l'uso di parentesi graffe per delimitare gli oggetti e parentesi quadre per delimitare le liste.
#e se volessi convertire la stringa json in un dizionario?  
json_dict = json.loads(json_string) #string to dict
print(json_dict) # stampa la lista di dizionari che rappresenta le persone, ottenuta convertendo la stringa JSON json_string in un oggetto Python usando la funzione json.loads(). La funzione json.loads() prende una stringa JSON come input e restituisce l'oggetto Python corrispondente, che in questo caso è una lista di dizionari. La struttura dei dati risultante è simile a quella originale, ma è stata ricostruita a partire dalla stringa JSON, quindi è possibile accedere agli elementi della lista e ai valori dei dizionari come si farebbe normalmente in Python.

#stampa tipo variabile

x = "ciao"
print(type(x))

#gestione stringhe
nome = "Marco"
eta = 28
print("Ciao" + nome + "hai " + str(eta) + "anni")
#oppure f che sta per format/formattare
print(f"Ciao {nome} hai {eta} anni")
print(f"Ciaoo { nome} tra 10 anni avrai {eta + 10 } anni")

#una stringa è un oggetto
testo = "Ciao Mondo"
testo_maiuscolo = testo.upper()
print(testo_maiuscolo)

testo.lower()
testo.capitalize()

#split

frase = "Nel mezzo del cammin di nostra vita"
#voglio mettere le singole parole della frase e metterli in una lista
parole = frase.split()
print(parole)

#ma supponiamo di avere dei dati seperati da virgola tipo csv
dati = "Marco, 28, Palermo"
elementi = dati.split(",")
print(elementi)
#e se andassi indietro? Join
nomi = ["Paolo" , "Giovanni", "Maria"]
frase = ",".join(nomi)

#replace
testo = "Mi piace il the"
nuovo = testo.replace("the","caffè")
#tutte queste cose sono a che fare a ETL extrasformer. purificazione dei dati
testo = " Ciao Mondo "
pulito = testo.strip()

testo = "Ciao Nemo"
posnemo = testo.find("Nemo")

nome.startswith()
nome.endswith()

lista = [1, 2, 3]
lista.append[4]

listadue = [1,2,4]
listadue.insert(2,3)

listatre = ["a", "b", "d"]
listatre.insert(2, "c")

listatre.remove("b") #elimina per valore

listatre.pop(2) #elimina per posizione
#ma prima posso prendere l'elemento per memorizzarlo
eliminato = listatre.pop(2)
amici = ["Mario", "Francesco", "Giuseppe"]
pos = amici.index("Francesco")
pos = amici.index("Francesco"-1)

#sort
amici.sort()
amici.reverse()
Mario = amici.count("Mario")
amici.clear()

#dizionari
persona = {"Nome": "Marco", "eta": 28, "citta": "Palermo"}
chiavi = persona.keys()
valori = persona.values()

#foreach

for chiave, valore in persona.items():
    print(f"{chiave}:{valore}")

#come creare le liste in maniera più compatta. Supponiamo di voler stampare dei numeri di una lista ma solo se pari
numeri = [1, 2,3,4,5,6,15,17,18,21,20,21,97]
numeripari =[numero for numero in numeri if numero % 2 == 0]

persone = [{"nome": "Mario", "eta": 28, "Maria": ""#lsta lunga}]
nome_persona = [persona ["nome"]for persona in persona if persone ["eta"] > 28]

