// Promise 2 — Simulare un caricamento

// Crea una Promise che dopo 3 secondi restituisca:

// Dati caricati!

// Usa:

// setTimeout()

// Poi utilizza .then() per stampare il risultato.

const caricamento = new Promise((resolve,reject) =>{
   setTimeout(() => {
    resolve("Dati caricati")
   }, 3000);
}

caricamento.then(risultato => {
    console.log(risultato);
    
})


// const login = new Promise((resolve, reject) => {
//     let  username = "admin"
//     let password = "1234"

//     if (username == "admin" && password == "1234"){
//         resolve("Login effettuato!");
//     }else{
//         reject("Username o password errati");
//     }
// })

// login
//     .then(risultato => {
//         console.log(risultato);
//     })
//     .catch(errore => {
//         console.log(errore);
//     });