// const calcolo = (a,b) => {
//     return a * b
// };

// const risultato = calcolo(5,3);
// console.log(risultato);

// const animali = ['Cane', 'Gatto'];
// const b = ['Coniglio'];
// const tutti = [...animali,...b];
// console.log(tutti)

// const frutta = ['mela', 'pera'];
// const aggiunta = [...frutta,'banana'];
// console.log(aggiunta)

// const colori = ["rosso", "verde", "blu"];
// colori.push('giallo');
// console.log(colori);
// //l'array originale viene modificato e stampa ["rosso", "verde", "blu", "giallo"];

// const vecchiLibri = ["Dune", "1984"];
// const nuoviLibri = [...vecchiLibri, "Fondazione"];


// nuoviLibri.push("Il Signore degli Anelli");
// console.log(vecchiLibri);
// console.log(nuoviLibri);
// //vecchiLibri rimane invariato, nuoviLibri  è la somma di vecchiLibri più
// //nuoviLibri con l'aggiunta del Signore degli anelli


// const studente = {
//     nome: "Marco",
//     voto: 8
// };

// const altroStudente = studente;
// altroStudente.voto = 10;

// console.log(studente);
// console.log(altroStudente);
// //abbiamo cambiato la proprietà voto al riferimento

// const altroStudente = {
//     ...studente
// };
// altroStudente.voto = 10;

// console.log(altroStudente)
//abbiamo lavorato sull'oggetto altroStudente lasciando
//invariato l'oggetto studente
/*
const b = a; i riferimenti b e a puntano allo stesso oggetto, mentre, const b = {...a}; crea un nuovo oggetto e dentro ci copia tutte le proprietà di a
La parola chiave è questa:

const b = a

➡️ assegnazione del riferimento

"Dammi lo stesso oggetto."

const b = {...a}

➡️ creazione di una copia superficiale (shallow copy)

"Creami un nuovo oggetto con le stesse proprietà."
*/

// =           → stesso riferimento
// ...         → nuovo contenitore con gli stessi dati

// const somma = (...numeri) => {
//     let totale = 0;

//     for (let numero of numeri) {
//         totale = totale + numeri;
//     }

//     return totale;
// };

// const risultato = somma(1,2,3,4,5);
// console.log(risultato)

const somma = (...numeri) => {
    let totale = 0;

    for (let numero of numeri) {
        totale = totale + numero;
    }

    return totale;
};

const risultato = somma(1,2,3,4,5);

console.log(risultato);

const numeri = [10,20,30];
const r =  numeri.reduce ((totale, numero) => {
    return totale + numero;
}, 0);

// 0+10 = 10
//totale adesso è 10
//10+20 = 30
//totale adesso è 30
//30+30=60
//quindi il totale degli elementi dell'array è 60
//la callback viene chiamata ad ogni nuovo giro degli elementi dell'array
//la callback si chiama r in questo caso?