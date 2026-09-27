// const espress  assegna require
// assegna nome app ad espress
// usa app.use
// fai una post con rotta e callback stampa req body in cui c'è la richiesta json
// e la risposta server

// metti l'applicazione in ascolto

// const express = require("express")
// const app = express()
// app.use(express.json())
// app.post("/utenti", (req,res) =>{
//     console.log(req.body);
//     res.send("Dati inviati")
    
// })
// app.listen(3000)

// ci vuole il metodo json() affiancato a express perché quest'ultimo non sa interpretare da solo le richieste del body

// 39. Esercizio — Login

// Immagina di avere questa richiesta:

// POST /login

// con un body:

// {
//     "username": "mario",
//     "password": "1234"
// }

// Scrivi una semplice rotta Express che:

// riceva il body
// recuperi username
// recuperi password
// stampi entrambi nella console
// restituisca una risposta al client.

const express = require("express")
const login = express()
login.use(express.json())
login.post("/login", (req,res)=>{
   const {username, password} = req.body
   console.log("username", username)
   console.log("password", password)
    res.send("Dati inviati")
    
})
login.listen(3000,()=>{
    console.log("Dati inviati alla porta 3000");
    
})


const express = require("express");

const app = express();

app.get("/utente", (req, res) => {
    res.json({
        nome: "Mario",
        eta: 30
    });
});
app.listen(3000,()=>{
    console.log("Dati ricevuti");
    
})

// 47. Esercizio — Route dinamica

// Vuoi poter visitare:

// /utente/25

// dove 25 rappresenta l'ID dell'utente.

// Scrivi una rotta Express che permetta di recuperare questo valore.

// Poi indica dove viene memorizzato:

// 25

// nell'oggetto req.

const express = require("express");

const app = express();

app.get("/utente/25", (req, res) => {
    const {id, username, password} = res.json()
app.listen(3000,()=>{
    console.log("Dati ricevuti");
    
}))


const express = require("express");

const appCitta = express();

appCitta.use(express.json())
const arrayOggetti {["id",nome]}= res.json()
appCitta.get("/citta/1", (req, res) => {
    console.log("ecco i dati:", arrayOggetti);
    
})

appCitta.post("/citta", (req,res)=>{
   const {id, nome = req.body}
   res.send("Dati inviati"
})

appCitta.listen(3000,()=>{
    console.log("ecco i dati");

