// function somma(a, b) {
//     // cosa deve fare?
//     console.log(a+b);
    
// }

// function sottrazione(a, b) {
//     // cosa deve fare?
//     console.log(a-b);
    
// }

// function moltiplicazione(a, b) {
//     // cosa deve fare?
//     console.log(a*b);
    
// }

// function calcola(a, b, operazione) {
//     operazione(a,b)
// }

// calcola(5,3, somma)
// calcola(5,3, sottrazione)
// calcola(5,3, moltiplicazione)

// funzione da eseguire
//        ↓
// attendi(funzione)
//        ↓
// la funzione viene conservata nel parametro callback
//        ↓
// setTimeout(callback, 2000)
//        ↓
// dopo 2 secondi → callback()

function  daFare() {
    console.log("finito");
    
}

function aspetta (callback) {
    setTimeout(callback, 5000)
    console.log("aspetto che tu abbia finito");
    
}

aspetta(daFare)

function compitoEseguito(params) {
    
}