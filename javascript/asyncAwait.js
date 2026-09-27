// Esercizio 1 — Fetch con async/await

// Ti do prima il pseudocodice, come abbiamo fatto prima.

// CREA una funzione asincrona

//     PROVA:

//         fai una richiesta GET all'API:
        // https://jsonplaceholder.typicode.com/users/1

//         ASPETTA la risposta

//         trasforma la risposta in JSON

//         ASPETTA i dati

//         stampa:
//             Nome
//             Username
//             Email

//     SE si verifica un errore:

//         stampa "Errore"

// Prova a trasformarlo in JavaScript.

// Non usare .then(): questa volta devi usare async, await e try/catch.

// CREA una funzione asincrona chiamata recuperaUtente

//     ALL'INTERNO della funzione:
//          crea le due variabili risposta con url fetch e dati in json
//         PROVA a eseguire queste operazioni

//             FAI una richiesta GET all'URL dell'API
//                 ↓
//             ASPETTA che la richiesta finisca
//                 ↓
//             SALVA la risposta dentro "risposta"

//             PRENDI la risposta
//                 ↓
//             CONVERTILA in JSON
//                 ↓
//             ASPETTA che la conversione finisca
//                 ↓
//             SALVA i dati dentro "dati"

//             STAMPA i dati

//         SE durante una delle operazioni si verifica un errore:

//             CATTURA l'errore

//             STAMPA "Si è verificato un errore"

// ALLA FINE:

//     ESEGUI la funzione recuperaUtente

// async function recuperaUtente() {
//     try {
//         const risposta = await fetch("https://jsonplaceholder.typicode.com/users/1")
//         const dati = await risposta.json();
//         console.log(dati);
        
//     } catch (error) {
//         console.log("si è verificato un errore");
        
//     }
// }
// recuperaUtente();



// Esercizio 2 — Recuperare più utenti

// Questa volta devi recuperare:

// https://jsonplaceholder.typicode.com/users

// Pseudocodice:

// CREA una funzione asincrona

//     PROVA:

//         fai una richiesta GET all'API

//         ASPETTA la risposta

//         trasforma la risposta in JSON

//         ASPETTA i dati

//         PER OGNI utente:

//             stampa il nome
//             stampa l'email

//     SE c'è un errore:

//         stampa "Errore nel recupero degli utenti"

// Qui dovrai quindi combinare:

// async
// await
// fetch
// json()
// for...of
// try/catch
// const recuperaUtenti = async () => {
//     try {
//         const risposta = await fetch("https://jsonplaceholder.typicode.com/users")
//         const dati = await risposta.json()
//         for (const element of dati) {
//             console.log("Nome:", element.name);
//             console.log("Email:", element.email);
//         }
//     } catch (error) {
//         console.log("si è verificato un errore");
        
//     }
// }

// recuperaUtenti()

// Esercizio 3 — Simuliamo il login

// Questo è quello che ci interessa di più per arrivare al progetto.

// Usiamo ancora JSONPlaceholder per esercitarci.

// Pseudocodice:

// CREA una funzione asincrona chiamata login

//     PROVA:

//         invia una richiesta POST a:
        // https://jsonplaceholder.typicode.com/users

//         nel body invia:

//             username = "admin"
//             password = "1234"

//         aspetta la risposta

//         trasforma la risposta in JSON

//         aspetta i dati

//         SE i dati ricevuti contengono:
//             username = "admin"
//             E password = "1234"

//             stampa "Login effettuato!"

//         ALTRIMENTI

//             stampa "Username o password errati!"

//     SE si verifica un errore:

//         stampa "Errore durante il login"

// CHIAMA la funzione login

// Questa volta devi quindi mettere insieme tutto quello che hai imparato:

// async
//    ↓
// await
//    ↓
// fetch
//    ↓
// POST
//    ↓
// headers
//    ↓
// body
//    ↓
// JSON.stringify()
//    ↓
// await risposta.json()
//    ↓
// if
//    ↓
// try/catch

const login = async () => {
    try {
        const risposta = await fetch("https://jsonplaceholder.typicode.com/users",
            {method: "POST",
             headers:{
              "Content-Type" : "application/json"
            },
            
           body: JSON.stringify(
            {
                "username": "admin",
                "password": "1234"
            }
        )
    })

    const dati = await risposta.json()

    if (dati.username == "admin" && dati.password == "1234") {
        console.log("Login effettuato!");
    }else{
        console.log("Username o password errati!");
        
    }

    } catch (error) {
        console.log("Errore durante il login");
        
    }
}


