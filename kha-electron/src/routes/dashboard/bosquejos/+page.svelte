<svelte:head>
  <title>Bosquejos</title>
</svelte:head>

<div class="tabnav">
  <a class="btn btn-sm float-right" href="/dashboard/bosquejos/nuevo" role="button">Nuevo</a>
  <nav class="tabnav-tabs" aria-label="Foo bar">
     <a class="tabnav-tab" href="/dashboard/bosquejos" aria-current="page">Bosquejos</a>
  </nav>
</div>

<div class="container-lg clearfix">
  <div class="Box">
     <div class="Box-row d-flex flex-items-center">
        <div class="flex-auto">
           <strong>Discurso público 1</strong>
        </div>
        <div class="container-lg clearfix" style="width: 70%;">
           <div class="col-4 float-left">
              <p class="h4">Fecha:</p>
              <p class="mt-n2">05/04/2023</p>
           </div>
           <div class="col-4 float-left">
              <p class="h4">Orador:</p>
              <p class="mt-n2">Ignacio Benham</p>
           </div>
           <div class="col-4 float-left">
              <p class="h4">Congregación:</p>
              <p class="mt-n2">Aurora</p>
           </div>
        </div>
        <button class="btn mr-2 btn-sm" type="button">
           <!-- <%= octicon "search" %> -->
           <svg class="octicon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" width="16" height="16">
              <path
                 d="M8 2c1.981 0 3.671.992 4.933 2.078 1.27 1.091 2.187 2.345 2.637 3.023a1.62 1.62 0 0 1 0 1.798c-.45.678-1.367 1.932-2.637 3.023C11.67 13.008 9.981 14 8 14c-1.981 0-3.671-.992-4.933-2.078C1.797 10.83.88 9.576.43 8.898a1.62 1.62 0 0 1 0-1.798c.45-.677 1.367-1.931 2.637-3.022C4.33 2.992 6.019 2 8 2ZM1.679 7.932a.12.12 0 0 0 0 .136c.411.622 1.241 1.75 2.366 2.717C5.176 11.758 6.527 12.5 8 12.5c1.473 0 2.825-.742 3.955-1.715 1.124-.967 1.954-2.096 2.366-2.717a.12.12 0 0 0 0-.136c-.412-.621-1.242-1.75-2.366-2.717C10.824 4.242 9.473 3.5 8 3.5c-1.473 0-2.825.742-3.955 1.715-1.124.967-1.954 2.096-2.366 2.717ZM8 10a2 2 0 1 1-.001-3.999A2 2 0 0 1 8 10Z">
              </path>
           </svg>
        </button>
     </div>
  </div>
</div>