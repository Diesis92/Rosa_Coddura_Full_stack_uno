// classe base: forma
//proprieta colore (default nero)
//metodo area()lancia un errore da implementare
//metodo descrivi() ${colore} con area ${area}

//classe rettangolo extends forma
//constructor (larghezza, altezza,colore)
//area() larghezza * altezza

//classe cerchio extends forma
//costructor(raggio, colore)
//area() math.PI * raggio ** 2(arrotonda a 2 decimali)


class Forma {
    constructor(colore = 'nero') {
        this.colore = colore
    }

    area(){
       throw new console.error('classe astratta:implementare in classe reale');
        
    }

    descrivi(){
        return `il mio colore è : ${colore} e questa è la mia ${area}`
    }
}

 class Rettangolo extends Forma(){
        constructor(larghezza, altezza, colore){
            super(colore);
            this.larghezza=larghezza;
            this.altezza = altezza
        }


        //override
        areaRettangolo(area){
            return (this.larghezza * this.altezza).toFixed(2);
        }
    }

class Cercchio extends Forma(){
        constructor(raggio, colore){
            super(colore);
            this.raggio=raggio
        }


        //override
        areaCerchio(area){
            return (Math.PI * (this.raggio**2)).toFixed(2);
        }
    }

const r = new Rettangolo(5,3,'blu');
const c = new Cerchio(4,'rosso')
console.log(r.descrivi());
console.log(c.descrivi());


//1-destruttura questo oggetto in variabili separate
//Estrai:id,nomeCliente,primoProdotto,totale

const ordine = {
    id:'ORD-001',
    cliente:{nome:'Lucia',email:'lucia@mail.it'},
    prodotti:['laptop','mouse','tastiera'],
    totale: 1050
};


//destrutturazione
const { id, cliente: { nome: nomeCliente }, prodotti: [primoProdotto], totale } = ordine;
console.log(id,nomeCliente,primoProdotto,totale)




//2 crea una funzione che unisce due array senza duplicati
//usa spread e Set:new Set([...arr1,...arr2]) rimuove duplicati

// const arr1 = [1,2,3];
// const arr2 = [2,3,4,5]
// function unisciSenzaDuplicati(arr1,arr2) {
//     ///
// }

/**
 * Unisce due array rimuovendo i duplicati.
 
 */
function unisciSenzaDuplicati(arr1, arr2) {
    // Validazione input: devono essere array
    if (!Array.isArray(arr1) || !Array.isArray(arr2)) {
        throw new TypeError("Entrambi i parametri devono essere array.");
    }

    // Unione con spread e rimozione duplicati con Set
    return [...new Set([...arr1, ...arr2])];
}

// Esempio d'uso
const arr1 = [1, 2, 3];
const arr2 = [2, 3, 4, 5];

try {
    const risultato = unisciSenzaDuplicati(arr1, arr2);
    console.log(risultato); // [1, 2, 3, 4, 5]
} catch (err) {
    console.error("Errore:", err.message);
}


//3crea una funzione che fa il merge di due oggetti con le proprietà del secondo che sovrascrivono il primo



function merge(obj1, obj2) {
    // Validazione input
    if (obj1 === null || typeof obj1 !== 'object') {
        throw new TypeError("Il primo parametro deve essere un oggetto valido");
    }
    if (obj2 === null || typeof obj2 !== 'object') {
        throw new TypeError("Il secondo parametro deve essere un oggetto valido");
    }

    // Crea un nuovo oggetto senza modificare gli originali
    return { ...obj1, ...obj2 };
}

// Esempio di utilizzo
const a = { nome: "Mario", eta: 30, città: "Roma" };
const b = { eta: 35, lavoro: "Ingegnere" };

const risultato = merge(a, b);
console.log(risultato);
// Output: { nome: 'Mario', eta: 35, città: 'Roma', lavoro: 'Ingegnere' }
