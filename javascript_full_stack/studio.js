console.log(typeof(42));
console.log(typeof("ciao"));
console.log(typeof([1,2,3]));//bug
console.log(typeof(null)) // bug

//Concatenazione classica (con +)

const nome = "Rosa";
const eta = 33

console.log("ciao sono " + nome + "ed ho"+ eta+ "anni")

// Template Literals (backtick)

console.log(`Ciao sono ${nome} ed ho ${eta} anni`)

const linguaggioPreferito = 'Javascript';
let anniDiEsperienza = 0;
const haFattoPython = true;
let progettoAttuale;

// Per ogni variabile, stampa:
// 'Nome: [valore] — Tipo: [tipo]'
// Usa i template literals!

console.log(`Nome:${linguaggioPreferito} - Tipo :${typeof linguaggioPreferito}`)
console.log(`Nome:${anniDiEsperienza} - Tipo :${typeof anniDiEsperienza}`)
console.log(`Nome:${haFattoPython} - Tipo :${typeof haFattoPython}`)
console.log(`Nome:${progettoAttuale} - Tipo :${typeof progettoAttuale}`)

//operatore ternario

// condizione ? seVero : seFalso

eta >= 18 ? 'maggiore' : 'minorenne'

//for

for (let i = 0; i< 5; i++) {
    console.log(`iterazione fino al numero ${i}`);
    
}

const arr1 = [1,2,3,4,5]

for (let i = 0; i < arr1.length; i++) {
    console.log(`l'elemento in posizione ${i} è ${arr1[i]}`)
}