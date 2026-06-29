// /*
// raccolta chiave - valore esattamente con un dizionario python
// */
// const studente = {
//     nome: 'Rosa',
//     cognome: 'Coddura',
//     eta: 25,
//     corso: 'Full Stack Development',

//     // metodo saluto
//     saluto: function () {
//         console.log(`Ciao, mi chiamo ${this.nome} ${this.cognome} e ho ${this.eta} anni. Seguo il corso di ${this.corso}.`);
//     }
// };

// // accesso alle proprietà
// console.log(studente.nome);
// console.log(studente.cognome);
// console.log(studente.eta);
// console.log(studente.corso);

// // chiamata del metodo
// studente.saluto();


// // destructuring
// const persona = {
//     nome: 'Rosa',
//     cognome: 'Coddura',
//     eta: 25,
//     corso: 'Full Stack'
// };


// // senza destructuring
// const nome = persona.nome;
// const cognome = persona.cognome;
// const eta = persona.eta;
// const corso = persona.corso;

// console.log(nome, cognome, eta, corso);


// // con destructuring (versione compatta)
// const { nome, cognome, eta, corso } = persona;

// console.log(nome, cognome, eta, corso);


// // destructuring con alias
// const { nome: nomePersona, cognome: cognomePersona } = persona;

// console.log(nomePersona, cognomePersona);


// // destructuring array
// const numeri = [10, 20, 30, 40];

// // senza destructuring
// const primo = numeri[0];
// const secondo = numeri[1];

// console.log(primo, secondo);


// // con destructuring array
// const [a, b, c, d] = numeri;

// console.log(a, b, c, d);


// // destructuring array con salto elementi
// const [x, , z] = numeri;

// console.log(x, z);

// // classi in javascript

// class Studente {
//     constructor(nome, cognome, corso, voti = []) {
//         this.nome = nome;
//         this.cognome = cognome;
//         this.corso = corso;
//         this.voti = voti;
//     }

//     saluta() {
//         console.log(`Ciao, sono ${this.nome} ${this.cognome} e frequento il corso ${this.corso}.`);
//     }

//     aggiungiVoto(voto) {
//         this.voti.push(voto);
//     }

//     get media() {
//         if (this.voti.length === 0) return 0;

//         return this.voti.reduce((acc, val) => acc + val, 0) / this.voti.length;
//     }
// }


// // crea un'istanza
// const studente1 = new Studente('Rosa', 'Coddura', 'Full Stack');

// // uso dei metodi
// studente1.saluta();

// studente1.aggiungiVoto(28);
// studente1.aggiungiVoto(30);
// studente1.aggiungiVoto(27);

// // media voti
// console.log(studente1.media);

// // ereditarietà

// class Persona {
//     constructor(nome, cognome, eta) {
//         this.nome = nome;
//         this.cognome = cognome;
//         this.eta = eta;
//     }

//     presentati() {
//         return `Ciao, sono ${this.nome} ${this.cognome} e ho ${this.eta} anni.`;
//     }
// }

// class Docente extends Persona {
//     constructor(nome, cognome, eta, materia) {
//         super(nome, cognome, eta);
//         this.materia = materia;
//     }

//     // override
//     presentati() {
//         return `Ciao, sono il docente ${this.nome} ${this.cognome}, ho ${this.eta} anni e insegno ${this.materia}.`;
//     }
// }

// // istanza
// const prof = new Docente('Mario', 'Rossi', 45, 'JavaScript');

// console.log(prof.presentati());


// //spread operator e rest parameters

// //spread su array ... espande
// // rest ... raccoglie

// const arr1 = [1,2,3]
// const arr2 = [4,5,6]
// const uniti = [...arr1, ...arr2]

// //copy di un oggetto

// const originale = {a:1,b:2};
// const copia = {...originale,c:3};

// //rest raccoglie argomenti multipli in un array

// function somma(...numeri) {
//     return numeri.reduce((acc, n) => acc + n, 0);
// }

// console.log(somma(1, 2, 3, 4, 5));

// Crea la classe contoBancario con:
//proprieta: titolare(string), saldo(number, default 0),transazioni(array)
//metodo deposita(importo):aggiunge al saldo se importo > 0
//metodo preleva(importo):sottrae dal saldo se importo > 0 e saldo sufficiente
//metodo get estrattoConto():restituisce un riepilogo formattato

// class ContoBancario {
//     constructor(titolare, saldo = 0 ) {
//         this.titolare = titolare;
//         this.saldo = saldo;
//         this.transazioni = [];

//     }

//      deposita(importo) {
//         if (typeof importo !== "number" || isNaN(importo) ){return "si prega di digitare un numero valido"}
//         if (importo <=0) { return "importo non valido"
//             this.saldo += importo;
//         }

//         this.transazioni.push({
//             tipo : "deposita",
//             importo,
//             saldo:this.saldo
//         })
//         return this.saldo;
//     }

//     preleva(importo) {
//         if (typeof importo !== "number" || isNaN(importo) ){return "si prega di digitare un numero valido"}
//         if (importo <= 0){ return "importo non valido"}
//         if (importo > this.saldo){return "Saldo insufficiente"}
        

//         this.saldo -= importo;
        

//         this.transazioni.push({
//             tipo : "prelievo",
//             importo,
//             saldo:this.saldo
//         })

//         return this.saldo;
//     }

//     get estrattoConto() {
//        return `Titolare:$(this.titolare) | Saldo : € $(this.saldo) | Transazioni: $(this.transazioni)` 
//     }
// }

class ContoBancario {
    constructor(titolare, saldo = 0) {
        this.titolare = titolare;
        this.saldo = saldo;
        this.transazioni = [];
    }

    deposita(importo) {
        if (typeof importo !== "number" || isNaN(importo)) {
            return "si prega di digitare un numero valido";
        }

        if (importo <= 0) {
            return "importo non valido";
        }

        this.saldo += importo;

        this.transazioni.push({
            tipo: "deposito",
            importo,
            saldo: this.saldo
        });

        return this.saldo;
    }

    preleva(importo) {
        if (typeof importo !== "number" || isNaN(importo)) {
            return "si prega di digitare un numero valido";
        }

        if (importo <= 0) {
            return "importo non valido";
        }

        if (importo > this.saldo) {
            return "Saldo insufficiente";
        }

        this.saldo -= importo;

        this.transazioni.push({
            tipo: "prelievo",
            importo,
            saldo: this.saldo
        });

        return this.saldo;
    }

    get estrattoConto() {
        return `Titolare: ${this.titolare} | Saldo: € ${this.saldo} | Transazioni: ${this.transazioni.length}`;
    }
}
//test
const conto = new ContoBancario('Mario Rossi', 1000);
conto.deposita(500);//saldo: 1500 euro
conto.preleva(200);//saldo: 1300 euro
conto.preleva(2000);// 'Saldo insufficiente'
console.log(conto.estrattoConto);
// Titolare: Mario Rossi| Saldo: € 1300 | transazioni:2