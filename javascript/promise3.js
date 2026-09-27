// Promise 3 — Numero casuale

// Crea una Promise che genera un numero casuale da 1 a 10.

// Se il numero è maggiore di 5:

// Hai vinto!

// Se è minore o uguale a 5:

// Hai perso!

// Qui voglio che ti eserciti bene con:

// resolve()
// reject()
// .then()
// .catch()

//creo oggetto promise
//funzione math random
// Prendi il numero prodotto da Math.random(), moltiplicalo per il risultato di max - min + 1, poi aggiungi min.
// alla funzione assegno una costante in cui (1,10)
//faccio partire un if

// assococio la costante dell'oggetto creatoi a then e cath

const numeroCasuale = new Promise((resolve, reject) => {
  function generaNumero(min, max) {
    return Math.floor(Math.random() * (max - min + 1) + min)
  }
  const risultato = generaNumero(1, 10)

  if (risultato > 5) {
    resolve("Hai vinto!")
  } else {
    reject("Hai perso!")
  }

})

numeroCasuale.then(risultato => {
    console.log(risultato);
  }).catch(errore => {
    console.log(errore);
  })


