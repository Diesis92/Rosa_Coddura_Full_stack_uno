// const nome = "Rosa";
// const ruolo = "studentessa fullstack";
// const scuola = "arces";
// const inizioAnno = 2025;
// const linguaggi = "Python, JavaScript";

// console.log(`Ciao, il mio nome è ${nome}, sono ${ruolo}, frequento il corso presso ${scuola}, inizio ${inizioAnno}, e studio ${linguaggi}`);

// //controllo temperatura

// let temp = 10;

// if (temp <= 0) {
//     console.log("attenzione al ghiaccio");
// } 
// else if (temp > 0 && temp < 15) {
//     console.log("freddo - metti il cappotto");
// } 
// else if ( temp < 16 && temp < 25){
//     console.log("temperatura piacevole");
// }else if ( temp < 26 &&  temp < 35){
//     console.log("caldo-tata acqua")
// }else{
//     console.log("afa-rimani in casa")
// }
    
// const numero=7;

// for (let i = 1; i<=10; i++) {
//     console.log(`${numero} x ${i} = 7 * ${i}`);
// }

// const voti = [45, 72, 88, 55, 91, 63, 39, 78, 50, 95];
// let contatoreSufficienti = 0;

// for (let i = 0; i < voti.length; i++) {
//     if (voti[i] >= 60) {
//         contatoreSufficienti++;
//     }
// }

// console.log(`voti sufficienti: ${contatoreSufficienti}`);

// // const numeroSegreto = 42;
// // let tentativi = 0;
// // let indovinato = false;

// // while (!indovinato) {
// //     const input = prompt("Indovina il numero (1-100):");
// //     const tentativo = parseInt(input);

// //     tentativi++;

// //     if (tentativo < numeroSegreto) {
// //         alert("Troppo basso");
// //     } else if (tentativo > numeroSegreto) {
// //         alert("Troppo alto");
// //     } else {
// //         alert(`Hai indovinato in ${tentativi} tentativi`);
// //         indovinato = true;
// //     }
// // }

// function saluta(nome) {
//     return `Ciao ${nome}`
// }

// console.log(saluta('Anna'));

// //con valori di default

// // function benevenuto(nome, ruolo=studente) {
// //     return `benvenuto ${nome}, ${ruolo}`
// // }

// // console.log(benvenuta('Rosa'));


// //funzione con più valori di ritorno
// function statistiche(numeri) {
//     const somma = numeri.reduce((acc,n) => acc + n,0);
//     const media = somma / numeri.length;
//     const max = Math.max(...numeri);
//     return {somma, media, max};
// }

// const risultato = statistiche([10,20,30,40]);
// console.log(risultato.somma);
// console.log(risultato.media);
// console.log(risultato.max);


// //arrow function

// //scope

// const globale = "Sono ovunque";

// function esempio() {
//     const locale = 'sono qui dentro'
//     console.log(globale)
//     console.log(locale)
// }

// esempio()
// console.log(globale)
// // console.log(locale) errore

// //funzioni come valori higher order functions

// function applicaDueVolte(funzione, valore) {
//     return funzione(funzione(valore));
// }

// const raddoppia = x => x * 2;
// console.log(applicaDueVolte(raddoppia, 3))

// //primo metodo higher order foreach

// const numeri = [1,2,3,4,5]
// numeri.forEach(n => console.log(n * 2))

// //calcolatrice

// // traccia
// // crea queste funzioni:
// // somma(a,b)
// // sottrai(a,b)
// // moltiplica(a,b)
// // dividi(a,b)
// // oppure 'errore:divisione per zero'




// function calcolatrice(a, operazione, b) {
//     let risultato;

//     switch (operazione) {
//         case "+":
//             risultato = a + b;
//             return `risultato: ${risultato}`;

//         case "-":
//             risultato = a - b;
//             return `risultato: ${risultato}`;

//         case "*":
//             risultato = a * b;
//             return `risultato: ${risultato}`;

//         case "/":
//             if (b === 0) {
//                 return "Errore: divisione per zero";
//             }
//             risultato = a / b;
//             return `risultato: ${risultato}`;

//         default:
//             return "Errore: operazione non valida";
//     }
// }

// console.log(calcolatrice(10,'+',5));
// console.log(calcolatrice(10,'/',0));//errore
// console.log(calcolatrice(7,'*',3));
// console.log(calcolatrice(7,'/',1));

// //arrow functions per array

// const studenti = ['Lucia','Marco', 'Sara','Giovanni', 'Mia'];
// const votiStudenti = [88,65,92,71,45];
// let contatore = 0;
// // 1-stampa ogni studente in maiuscolo usando ForEach + arrow function
// // 2-stampa per ogni studente il voto se è promosso (>=60)
// //suggerimento:usa l'indice forEach:
// //array.forEach((elem, indice) => ...)
// //3- conta quanti studenti hanno un nome con + di quattro caratteri
// //usa una variabile contatore e forEach

// // const somma = (a, b) => a + b;

// studenti.forEach(studente => {
//     console.log(studente)
// });

// studenti.forEach((studente, i) => {
//     if (votiStudenti[i] >= 60) {
//         console.log(`${studente}: ${votiStudenti[i]} - promosso`);
//     }
// });

// //implementa il metodo upperCase()

// studenti.forEach(studente => {
//     if (studente.length > 4 ){
//         contatore ++;
//     }
// });
// console.log(contatore);

// //function ricorsiva

// //fattoriale(5)= 5*4*3*2*1=120
// //fattoriale(0)=1 caso base

// function fattoriale(n) {
//     if (n === 0) {
//         return 1;
//     } else {
//         return n * fattoriale(n - 1);
//     }
// }

// //poi arrow function

// const fattorialeArrow = n => n === 0 ? 1 : n * fattorialeArrow(n - 1);

// console.log(fattoriale(5));
// console.log(fattorialeArrow(6));

// //palindroma
// //analizzaParola(parola) restituisce un oggetto con:
// //lunghezza:numero di caratteri
// //maiuscola: la parola in maiuscolo
// //miscuola:la parola in minuscolo
// //palindroma: true se la parola è uguale al contrario

// //suggerimento palindroma
// //parola === parola.split('').reverse.().join('')

// //test
function analizzaParola(parola) {
    return {
        lunghezza: parola.length,
        maiuscola: parola.toUpperCase(),
        minuscola: parola.toLowerCase(),
        palindroma: parola === parola.split('').reverse().join('')
    };
}

const p = analizzaParola('radar');
console.log(p);


//array
const numeri =[1,2,3,4,5];
const misto = [42, 'ciao', true, null]
const vuoto= []

console.log(numeri[0]);
console.log(numeri[4]);
console.log(numeri.length);

//push, pop,unshifit, shift metodi base
//metodi funzionali map, filter reduce
//map trasforma ogni elemento

const prezzi = [10,25,8,42,15];
const prezziConIVA=prezzi.map(p => p * 1.22)

const voti = [42,78,60,66,80,75];
const sufficienti = voti.filter(v=>v>= 60);
console.log(sufficienti);

//reduce
const num = [1,2,3,4,5,];
const somma = num.reduce((accumulatore, corrente) => accumulatore + corrente, 0);
console.log(somma)
const prodotto = num.reduce((acc, n) => acc * n,1);
console.log(prodotto);

//metodo chaining concatenazioni di metodi
// const prodotti = [
//     { nome: 'Laptop', prezzo: 900, inStock: true },
//     { nome: 'Mouse', prezzo: 30, inStock: true },
//     { nome: 'Monitor', prezzo: 200, inStock: false },
//     { nome: 'Tastiera', prezzo: 50, inStock: true }
// ];

// const totale = prodotti
//     .filter(p => p.inStock)
//     .map(p => p.prezzo * 0.9)
//     .reduce((acc, prezzo) => acc + prezzo, 0);

// console.log(totale);

//metodi find e findIndex, some e every, includes e sort

const arr= [3,1,4,1,5,9,2,6]
arr.find(n => n > 4);
arr.findIndex(n => n > 4);

arr.some(n => n > 8);
arr.every(n => n > 0);
arr.includes(9)
//attenzione sort modifica l'array originale
const array = [5, 2, 9, 1, 7];

const ordinato = [...array].sort((a, b) => a - b);
//((a, b) => a - b); per ordinare i numeri passa sempre una funzione di comparazione
console.log(ordinato);
console.log(array); // resta invariato

const catalogo = [
  { id: 1, nome: 'Cuffie Bluetooth', prezzo: 79,  categoria: 'audio',      rating: 4.5 },
  { id: 2, nome: 'Webcam HD',        prezzo: 55,  categoria: 'video',      rating: 3.8 },
  { id: 3, nome: 'Microfono USB',    prezzo: 120, categoria: 'audio',      rating: 4.8 },
  { id: 4, nome: 'Hub USB',          prezzo: 30,  categoria: 'accessori',  rating: 4.2 },
  { id: 5, nome: 'Tappetino XL',     prezzo: 25,  categoria: 'accessori',  rating: 4.0 },
  { id: 6, nome: 'Speaker BT',       prezzo: 95,  categoria: 'audio',      rating: 4.6 },
];

//filtra i prodotti audio con rating > 4.5
//usa filter con due ccondizioni combinate con &&

//crea un array con i soli nomi di tutti i prodotti
// usa map per estrarre la proprietà nome da ogni oggetto

//calcola la spesa totale di tutto il catalogo
//usa reduce sommando le proprietà prezzo. valore atteso:€ 404

//trova il prodotto più economico
//usa reduce confrontando i prezzi oppure ordina con sort e prendi il primo

//conta quanti prodotti costano meno di € 50
//usa filter e poi accedi alla proprietà.length del risultato

// const prodotti = [
//     { nome: 'Laptop', prezzo: 900, inStock: true },
//     { nome: 'Mouse', prezzo: 30, inStock: true },
//     { nome: 'Monitor', prezzo: 200, inStock: false },
//     { nome: 'Tastiera', prezzo: 50, inStock: true }
// ];

// const totale = prodotti
//     .filter(p => p.inStock)
//     .map(p => p.prezzo * 0.9)
//     .reduce((acc, prezzo) => acc + prezzo, 0);
const risultato = {
  audioTop: catalogo.filter(
    p => p.categoria === 'audio' && p.rating > 4.5
  ),

  nomi: catalogo.map(p => p.nome),

  totale: catalogo.reduce(
    (acc, p) => acc + p.prezzo,
    0
  ),

  piuEconomico: catalogo.reduce((min, p) =>
    p.prezzo < min.prezzo ? p : min
  ),

  sotto50: catalogo.filter(p => p.prezzo < 50).length
};

console.log(risultato);


// const frase = 'il cielo di palermo è sempre azzurro e presente'
// const parole = frase.split('')
// console.log(parole)

//conta le parole della frase 
//usa la proprietà length sull'array parole. Risultato atteso:9

//crea un array delle parole con più di 5 lettere
//usa filter con la ocndizione p.length > 5 risultato atteso: ['palermo', 'sempre','azzurro','bellissimo']

//prima lettera maiuscola per ogni parola
// usa map.suggerimento p[0].toUpperCase()+p.slice(1)per ogni parola

//controlla se 'palermo' è presente
//usa includes('palermo'). risultato atteso: true

//rcrea la frase con le parole ordinate alfabeticamente
//usa [...parole].sort()(per le stringhe non serve funzione di comparazione)poi.join('')

// const risultatoDue = {
//   contaParole: frase.length(),

//   arr: frase.filter(p => p.length > 5),

//   maiuscola: frase.map(p => p[0].toUpperCase()+p.slice(1),p[2].toUpperCase()+p.slice(1), p[0].toUpperCase()+p.slice(1)),

//   incluso: frase.includes('palermo')

//   ordinato: frase.



// }


const frase = 'il cielo di palermo è sempre azzurro e presente';

const parole = frase.split(' ');

const risultatoDue = {
  parole: parole,

  contaParole: parole.length,

  lunghe: parole.filter(p => p.length > 5),

  maiuscole: parole.map(
    p => p[0].toUpperCase() + p.slice(1)
  ),

  inclusoPalermo: parole.includes('palermo'),

  ordinata: [...parole]
    .sort()
    .join(' ')
};

console.log(risultatoDue);


// Esercizio 3 — Chaining Avanzato
// Questo esercizio richiede di concatenare più metodi per risolvere problemi complessi. 
// Lavorerai con un array di studenti, ognuno con un sotto-array di
// voti. L'obiettivo finale è produrre una classifica ordinata dei promossi.
// const studenti = [
// { nome: 'Alice', voti: [85, 92, 78, 88] },
// { nome: 'Bob', voti: [55, 60, 45, 70] },
// { nome: 'Carol', voti: [95, 98, 92, 97] },
// { nome: 'Dave', voti: [72, 68, 75, 80] },
// { nome: 'Eve', voti: [40, 55, 50, 45] },
// ];
// Step 1 — Calcola la Media
// Usa map su studenti. Per ogni studente, usa
// reduce sul sotto-array voti per calcolare la
// somma, poi dividi per voti.length. Aggiungi il
// risultato come nuova proprietà media
// usando lo spread operator ...s.
// Step 2 — Costruisci la Classifica
// In una sola catena: filter gli studenti con
// media >= 60, poi map per tenere solo nome
// e media (con toFixed(1)), poi sort per
// ordinare per media decrescente (b.media -
// a.media).
// Step 3 — Stampa la Classifica
// Usa forEach (con indice i) per stampare ogni
// riga formattata: `${i+1}. ${s.nome} —
// Media: ${s.media}`. Il risultato atteso è:
// Carol 95.5, Alice 85.8, Dave 73.8

const studenti = [
{ nome: 'Alice', voti: [85, 92, 78, 88] },
{ nome: 'Bob', voti: [55, 60, 45, 70] },
{ nome: 'Carol', voti: [95, 98, 92, 97] },
{ nome: 'Dave', voti: [72, 68, 75, 80] },
{ nome: 'Eve', voti: [40, 55, 50, 45] },
];

const risultatoTre = {
  conMedia: studenti.map(s => {
    const media =
      s.voti.reduce((acc, v) => acc + v, 0) / s.voti.length;

    return {
      ...s,
      media
    };
  }),

  classifica: studenti
    .map(s => {
      const media =
        s.voti.reduce((acc, v) => acc + v, 0) / s.voti.length;

      return {
        nome: s.nome,
        media: Number(media.toFixed(1))
      };
    })
    .filter(s => s.media >= 60)
    .sort((a, b) => b.media - a.media)
};

risultatoTre.classifica.forEach((s, i) => {
  console.log(`${i + 1}. ${s.nome} — Media: ${s.media}`);
});

