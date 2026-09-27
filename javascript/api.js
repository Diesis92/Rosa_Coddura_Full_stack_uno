// API 1 — Capire una GET

// Usa l'API:

//  https://jsonplaceholder.typicode.com/users/1

// e prova a capire quali informazioni restituisce.

// Devi stampare:

// Nome:
// Username:
// Email:
// Città:

// fetch("https://jsonplaceholder.typicode.com/users/1")
//     .then(risposta =>{
//         return risposta.json();
//     })

//     .then(dati=>{
//         console.log("Nome:", dati.name);
//         console.log("Username:", dati.username);
//         console.log("Email:", dati.email);
//         console.log("Città", dati.address.city);

//     })

//     .catch(errore=>{
//         console.log("Errore nella fruizione dei dati!");

//     });


// API 2 — Creare un utente

// Usa una richiesta:

// POST

// verso:

// https://jsonplaceholder.typicode.com/users

// e invia:

// {
//     "name": "Rosa",
//     "username": "rosa92",
//     "email": "rosa@example.com"
// }

// Poi stampa la risposta del server.

// Qui iniziamo a vedere la differenza tra:

// GET → chiedo dati
// POST → invio dati

// fetch("https://jsonplaceholder.typicode.com/users",
//     {
//         method: "POST",
//         headers: {
//             "Content-Type": "Application/json"
//         },

//         body: JSON.stringify(
//             {
//                 "name": "Rosa",
//                 "username": "rosa92",
//                 "email": "rosa@example.com"
//             }
//         )
//     })

//     .then(risposta => {
//         return risposta.json()
//     })

//     .then(dati => {
//         console.log(dati);
//     })

//     .catch(errore => {
//         console.log("Si è verificato un errore");

//     })

// API 3 — Simulare il login

// Questo è il più importante.

// Usa una API di test e costruisci una richiesta che invii:

// {
//     "username": "admin",
//     "password": "1234"
// }

// Dovrai poi gestire la risposta.

// L'obiettivo concettuale è arrivare a:

// FORM
//  ↓
// username + password
//  ↓
// fetch()
//  ↓
// POST /login
//  ↓
// SERVER
//  ↓
// controllo
//  ↓
// risposta
//  ↓
// JavaScript
//  ↓
// "Login effettuato!"

fetch("https://jsonplaceholder.typicode.com/users",
    {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify(
            {
                "username": "admin",
                "password": "1234"
            }
        )
    })

    .then(risposta => {
        return risposta.json()
    })

    .then(dati => {
       if(dati.username === "admin" && dati.password === "1234"){
         console.log("Login effettuato", dati);
       }else{
        console.log("Username o password errati!");
        
       }
    })

    .catch(errore => {
        console.log("Si è verificato un errore");

    })
