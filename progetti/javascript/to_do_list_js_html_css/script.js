const inputBox = document.getElementById('input-box');
const listContainer = document.getElementById('list-container');
function addTask() {
    if (inputBox.value === '') {
        alert('Devi scrivere qualcosa!');
    } else {
        let li = document.createElement('li');
        li.innerHTML = inputBox.value;
        listContainer.appendChild(li);    
        let span = document.createElement('span');
        span.innerHTML = '\u00d7'; //simbolo per icona a croce
        li.appendChild(span);   
    }
    inputBox.value = '';
    saveData();
}


// EVENTO INVIO
// Aggiungiamo un evento "keydown" all'input.
// In questo modo controlliamo se l'utente preme il tasto Invio.
inputBox.addEventListener('keydown', function(e) {

    // Se il tasto premuto è Invio...
    if (e.key === 'Enter') {
        addTask();
    }
});

// Aggiungiamo un evento "click" al contenitore della lista.
// In questo modo controlliamo i click sugli elementi contenuti dentro listContainer.
listContainer.addEventListener('click',  function(e) {

    // Controlliamo quale elemento è stato effettivamente cliccato.
    // e.target rappresenta l'elemento preciso su cui l'utente ha fatto click.
    if (e.target.tagName === 'LI') { //"Se l'elemento che l'utente ha cliccato è un <li>..."

        // Se abbiamo cliccato su un <li>, aggiungiamo o rimuoviamo
        // la classe CSS "checked".
        // toggle() aggiunge la classe se non esiste,
        // oppure la rimuove se esiste già.
        e.target.classList.toggle('checked');
        saveData();

    // Altrimenti, se abbiamo cliccato su uno <span>...
    } else if (e.target.tagName === 'SPAN') {

        // ...risaliamo all'elemento genitore dello <span>,
        // che in questo caso è il <li>,
        // e lo eliminiamo dalla lista.
        e.target.parentElement.remove();
        saveData();
    }

// false indica che l'evento viene gestito nella fase di bubbling.
}, false);

// CLICK
//   ↓
// e.target
//   ↓
// ┌──────────────────────┐
// │ è un LI?             │ → toggle("checked")
// │                      │
// │ è uno SPAN?          │ → elimina il LI
// └──────────────────────┘

function saveData() {
    localStorage.setItem('data', listContainer.innerHTML);
}

function showTask() {
    listContainer.innerHTML = localStorage.getItem('data');
}
showTask();