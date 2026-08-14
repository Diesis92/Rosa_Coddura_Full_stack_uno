<template>
  <!-- LoginView.vue -->

  <!--
    min-vh-100 = altezza minima pari al 100% della finestra (viewport)

    d-flex = attiva Flexbox sul container

    align-items-center = centra verticalmente il contenuto
  -->
  <div class="container min-vh-100 d-flex align-items-center">

    <!--
      row = riga Bootstrap

      justify-content-center = centra orizzontalmente
      gli elementi contenuti nella riga

      w-100 = width: 100%
      La row occupa tutta la larghezza disponibile,
      così il centraggio orizzontale funziona correttamente.
    -->
    <div class="row justify-content-center w-100">

      <!--
        col-12 = 12 colonne su dispositivi piccoli → tutta la larghezza

        col-md-6 = 6 colonne su dispositivi medi → metà larghezza

        col-lg-4 = 4 colonne su dispositivi grandi → un terzo della larghezza
      -->
      <div class="col-12 col-md-6 col-lg-4">

        <!-- Card del login -->
        <div class="card shadow">

          <div class="card-body">

            <h1 class="text-center mb-4">Login</h1>

            <p class="text-center">
              Benvenuto nella pagina di login!
            </p>

            <!-- campo email -->
            <div class="mb-3">

              <label for="identifier" class="form-label">
                Email o Username
              </label>

              <input
                type="text"
                id="identifier"
                class="form-control"
                placeholder="Inserisci la tua email o username"
              >

            </div>

            <!-- campo password -->
            <div class="mb-3">

              <label for="password" class="form-label">
                Password
              </label>

              <input
                type="password"
                id="password"
                class="form-control"
                placeholder="Inserisci la tua password"
              >

            </div>

            <!-- recupero account -->
            <div class="mb-3 text-center">

              <router-link to="/forgot-password">
                Password o email dimenticata?
              </router-link>

            </div>

            <!-- pulsante login -->
            <div class="d-grid">

              <button type="button" class="btn btn-primary">
                Accedi
              </button>

            </div>

            <!-- Registrazione -->
            <div class="text-center mt-3">

              <span>Non sei registrato?</span>

              <router-link to="/register" class="btn btn-link">
                Registrati!
              </router-link>

            </div>

          </div>
        </div>
      </div>
    </div>
  </div>
</template>
