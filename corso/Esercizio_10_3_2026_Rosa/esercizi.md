# 🧩 Scheda Esercizi HTML + CSS

*(Senza Bootstrap)*

---

## Esercizio 1 — Card Profilo

### Obiettivo

Creare una **card profilo** usando HTML e CSS.

### Requisiti

La card deve contenere:

- immagine profilo
- nome
- breve descrizione
- bottone "Contattami"

### Vincoli

La card deve avere:

- larghezza massima **300px**
- contenuto **centrato**
- **bordo arrotondato**
- immagine larga **100%**

### Struttura HTML di partenza

```html
<div class="card">
  <img src="profile.jpg" alt="Profilo">

  <h2>Mario Rossi</h2>

  <p>Sviluppatore web appassionato di tecnologia.</p>

  <a href="#">Contattami</a>
</div>
```

Suggerimenti CSS

Proprietà utili:

- width
- margin
- padding
- border-radius
- text-align
- background

#### Extra (Facoltativo)

Aggiungere effetti shadow

Proprietá utili:

- box-shadow

---

## Esercizio 2 — Navbar Orizzontale

### Obiettivo

Creare un menu di navigazione orizzontale.

### Requisiti

Il menu deve contenere

- Home

- Servizi

- Chi siamo

- Contatti

### Requisiti grafici

La navbar deve avere:

- sfondo scuro

- link bianchi

- link disposti orizzontalmente

- effetto hover

- spazio interno (padding)

HTML di partenza

```html

<nav>
  <a href="#">Home</a>
  <a href="#">Servizi</a>
  <a href="#">Chi siamo</a>
  <a href="#">Contatti</a>
</nav>

```

### Suggerimenti CSS

#### Proprietà utili:

- display
- padding
- background
- color
- margin
- text-decoration
- :hover
  
---

## Esercizio 3 — Galleria Immagini

## Obiettivo

Creare una galleria di immagini responsive.

### Requisiti

Ogni elemento deve contenere:

- immagine

- titolo

- descrizione

- Requisiti

- le immagini devono adattarsi al contenitore

- gli elementi devono stare su una riga

- su schermi piccoli devono andare uno sotto l'altro

HTML di partenza
(i nomi delle immagini possono essere cambiati ovviamente...)

```html

<section class="gallery">

  <div class="item">
    <img src="img1.jpg" alt="">
    <h3>Montagna</h3>
    <p>Descrizione paesaggio montano</p>
  </div>

  <div class="item">
    <img src="img2.jpg" alt="">
    <h3>Mare</h3>
    <p>Descrizione paesaggio marino</p>
  </div>

  <div class="item">
    <img src="img3.jpg" alt="">
    <h3>Lago</h3>
    <p>Descrizione paesaggio lacustre</p>
  </div>

</section>
```

### Suggerimenti CSS

#### Proprietà utili:

- display: flex
- flex-wrap
- width
- img { width: 100% }
- margin
- @media

### Extra (Facoltativa)

Aggiungere effetti hover:

- ingrandimento card

- ombra più intensa

Esempio:

```css

.card:hover {
  transform: scale(1.05);
}
```

