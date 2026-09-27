// FETCH(URL)
//     .THEN(ricevi la risposta)
//         → trasforma la risposta in dati
//     .THEN(ricevi i dati)
//         → usa i dati
//     .CATCH(ricevi l'errore)
//         → gestisci l'errore

// esercizio

// Esercizi Fetch

// Per questi esercizi possiamo usare una API pubblica di test, così non devi ancora costruire il tuo backend.

// Fetch 1 — Recuperare un utente

// Fai una richiesta GET a:

https://jsonplaceholder.typicode.com/users/1

// e stampa nella console:

// Nome:
// Email:

// fetch("https://jsonplaceholder.typicode.com/users/1")
//     .then(risposta =>{
//         return risposta.json();
//     })
//     .then(dati =>{
//         console.log("Nome:", dati.name);
//         console.log("Email:", dati.email);
//     })
//     .catch(errore =>{
//         console.log("Errore!Dati non ricevuti!");

//     })

// Fetch 2 — Recuperare tutti gli utenti

// Fai una richiesta a:

// https://jsonplaceholder.typicode.com/users

// e stampa nella console il nome di ogni utente.

// Dovrai quindi gestire un array.

// fetch("https://jsonplaceholder.typicode.com/users")
//     .then(risposta => {
//         return risposta.json()
//     })
//     .then(dati => {
//         for (const element of dati) {
//             console.log(element);

//         }
//     })

//     .catch(errore => {
//         console.log("Errore!Dati non ricevuti!");

//     })

// FETCH → vai a prendere gli utenti
// THEN → poi prendi la risposta
// THEN → poi prendi/usa i dati JSON
// CATCH → se qualcosa va storto, cattura l'errore

// Fetch 3 — Gestire un errore

// Fai una richiesta a un URL inesistente, per esempio:

// https://jsonplaceholder.typicode.com/abc

// e cerca di gestire il problema mostrando:

// Si è verificato un errore

// Questo esercizio è importante perché nel mondo reale le richieste possono fallire.

fetch("https://jsonplaceholder.typicode.com/abc")
    .then(risposta => {
        return risposta.json()
    })
    .then(dati => {
        console.log(dati);

    })


    .catch(errore => {
        console.log(" Si è verificato un errore");

    })
