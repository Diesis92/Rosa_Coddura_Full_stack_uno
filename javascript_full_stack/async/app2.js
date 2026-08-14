const numeri = [5, 8, 2, 10, 7];
//stampa tutti i numeri dell'array
// for( let numero of numeri) {
//     console.log(numero);
// }

//somma tutti i numeri dell'array

let somma = 0;
for( let numero of numeri) {
    somma += numero;
    
}
console.log(somma);


const numeri = [3, 8, 5, 10, 1, 4];

let somma = 0;

// for (let numero of numeri) {
// 	if (numero % 2 === 0){
// 	somma += numero
// 	}
// 	console.log("somma": somma);
// }
// prima interazione: 3 è divisivile per 2?no
// seconda interazione: 8 è divisibile per 2?si
// 0 + 8 = 8
// terza interazione: 5 è divisibile per 2 no
// quarta interazione 10 è divisibile per 2 si
// somma 8 + 10 = 18
// quinta interazione: 1 è divisibile per 2? no
// sesta interazione: 4 è divisibile per 2?
// si
// somma 18+4=22
// outup 22


const parola = "javascript";

let contatore = 0;

for (let lettera of parola) {
	if (lettera == "a" ||
 	    lettera == "e" ||
            lettera == "i" || 
            lettera == "o" || 
            lettera == "u") {
	    contatore ++;
}
}
console.log("contatore" ,contatore)

// 1 interazione: j è uguale ad a, oppure e, oppure i, oppure o, oppure u?
// no
// 2 interazione: a è uguale ad a?
// si
// contatore 1
// 3 interazione: v è uguale ad a, oppure e, oppure i, oppure o, oppure u?
// no
// 4 interazione: a è uguale ad a?
// sì
// contatore 1 + 1 = 2
// 5 interazione: s è uguale ad a, oppure e, oppure i, oppure o, oppure u?
// no
// 6 interazione: c è uguale ad a, oppure e, oppure i, oppure o, oppure u?
// no
// 7 interazione: r è uguale ad a, oppure e, oppure i, oppure o, oppure u?
// no
// 8 interazione: i è uguale ad a, oppure e, oppure i?
// si
// contatore 2 + 1 = 3
// 9 interazione: p è uguale ad a, oppure e, oppure i, oppure o, oppure u?
// no
// 10 interazione: t è uguale ad a, oppure e, oppure i, oppure o, oppure u?
// no
//output contatore: 3


const numeri = [12, 4, 25, 8, 17];

let massimo = numeri[0];

for (let numero of numeri) {
    if (numero > massimo) {
        massimo = numero;
    }
}

console.log(massimo);

// somma totale → totale += numero
// trova massimo → massimo = numero
// trova minimo → minimo = numero

// let massimo = 0 → "creo un valore inventato"
// let massimo = numeri[0] → "parto da un valore reale dei miei dati"