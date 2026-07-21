// // Esercizio 1:a<Scrivi una funzione che riceve due numeri e restituisce il maggiore.
// // let a = 5;
// // let b = 8; 
// // function maggiore(a,b) {
// //     if (a > b){
// //         return true
// //     }
// // }

// // const verifica = maggiore (5,8);
// // console.log(verifica)

// function maggiore(a, b) {

//     if (a > b) {
//         return a
//     } else {
//        return b
//     }

// }

// console.log(maggiore(5, 8));


// // Esercizio 2 — Pari o dispari

// // Data una lista:

// // [4, 7, 10, 3, 8]

// // Stampa:

// // 4 pari
// // 7 dispari
// // 10 pari
// // 3 dispari
// // 8 pari

// // Allenamento:

// // ciclo
// // operatore modulo %

// const lista = [4, 7, 10, 3, 8]

// for (const element of lista) {
//    if (element % 2 == 0 ) {
//         console.log(element + " pari");
//    } else {
//         console.log(element + " dispari");
//    }
// }


// // Esercizio 3 — Classificatore di età

// // Scrivi una funzione:

// // classificaEta(25)

// // che restituisce:

// // 0-12 → bambino
// // 13-17 → adolescente
// // 18-64 → adulto
// // 65+ → anziano

// // Allenamento:

// // condizioni multiple

// function classificaEta(eta) {
//     if (eta >= 0 && eta <= 12 ) {
//         return "bambino";
//     } else if  (eta >= 13 && eta <=17){
//         return "adolescente";
//     } else if (eta >= 18 && eta <= 64){
//         return "adulto"
//     } else{
//         return "aziano"
//     }
// }

// console.log(classificaEta(23))










// Livello 2 — Cicli e contatori
// Esercizio 4 — Conta le vocali

// Input:

// "javascript"

// Output:

// 3

// Devi contare:

// a, a, i

// Allenamento:

// ciclo sulle stringhe
// condizioni

//ho bisogno degli indici per individuare le vocali. Le scorro con i
// let parola = "javascript";

// for (let i = 0; i < parola.length; i++) {
//     const lettera = parola[i]; //È uguale al carattere che si trova nell'indice i.
//    if (lettera == "a" ||
//        lettera == "e" ||
//        lettera == "i" ||
//        lettera == "o" ||
//        lettera == "u" 

//    ) {
//     console.log(lettera)
//    }
// }

// let parola = "javascript";

// let i = 4;

// console.log(parola[i]);

const numeri = [5, 10, 15, 20];
let somma = 0;

for (let i = 0; i < numeri.length; i++) {
    somma += numeri[i];    
}
console.log(somma)