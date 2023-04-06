<svelte:head>
  <title>Territorios</title>
</svelte:head>

<div class="tabnav">
  <button class="btn-octicon float-right tooltipped tooltipped-sw" aria-label="Exportar" type="button">
     <svg class="octicon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" width="16" height="16">
        <path
           d="M2.75 14A1.75 1.75 0 0 1 1 12.25v-2.5a.75.75 0 0 1 1.5 0v2.5c0 .138.112.25.25.25h10.5a.25.25 0 0 0 .25-.25v-2.5a.75.75 0 0 1 1.5 0v2.5A1.75 1.75 0 0 1 13.25 14Z">
        </path>
        <path
           d="M11.78 4.72a.749.749 0 1 1-1.06 1.06L8.75 3.811V9.5a.75.75 0 0 1-1.5 0V3.811L5.28 5.78a.749.749 0 1 1-1.06-1.06l3.25-3.25a.749.749 0 0 1 1.06 0l3.25 3.25Z">
        </path>
     </svg>
  </button>
  <button class="btn-octicon float-right tooltipped tooltipped-sw" type="button" aria-label="Importar">
     <svg class="octicon float-right" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" width="16"
        height="16">
        <path
           d="M2.75 14A1.75 1.75 0 0 1 1 12.25v-2.5a.75.75 0 0 1 1.5 0v2.5c0 .138.112.25.25.25h10.5a.25.25 0 0 0 .25-.25v-2.5a.75.75 0 0 1 1.5 0v2.5A1.75 1.75 0 0 1 13.25 14Z">
        </path>
        <path
           d="M7.25 7.689V2a.75.75 0 0 1 1.5 0v5.689l1.97-1.969a.749.749 0 1 1 1.06 1.06l-3.25 3.25a.749.749 0 0 1-1.06 0L4.22 6.78a.749.749 0 1 1 1.06-1.06l1.97 1.969Z">
        </path>
     </svg>
  </button>
  <button class="btn btn-sm ml-2 float-right" href="#url" role="button">
     <!-- <%= octicon "trashcan" %> -->
     <svg class="octicon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" width="16" height="16">
        <path
           d="m.427 1.927 1.215 1.215a8.002 8.002 0 1 1-1.6 5.685.75.75 0 1 1 1.493-.154 6.5 6.5 0 1 0 1.18-4.458l1.358 1.358A.25.25 0 0 1 3.896 6H.25A.25.25 0 0 1 0 5.75V2.104a.25.25 0 0 1 .427-.177ZM7.75 4a.75.75 0 0 1 .75.75v2.992l2.028.812a.75.75 0 0 1-.557 1.392l-2.5-1A.751.751 0 0 1 7 8.25v-3.5A.75.75 0 0 1 7.75 4Z">
        </path>
     </svg>
     <span>Historial</span>
  </button>
  <a class="btn btn-sm float-right" href="#url" role="button">Nuevo</a>
  <nav class="tabnav-tabs" aria-label="Foo bar">
     <a class="tabnav-tab" href="/dashboard/territorios" aria-current="page">Territorios</a>
  </nav>
</div>

<div class="container-lg clearfix">
  <div class="col-4 float-left">
     <div class="Box">
        <div class="Box-row d-flex flex-items-center">
           <div class="flex-auto">
              <strong>Territorio 1</strong>
           </div>
           <button class="btn mr-2 btn-sm" type="button">
              <!-- <%= octicon "search" %> -->
              <svg class="octicon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" width="16"
                 height="16">
                 <path
                    d="M8 2c1.981 0 3.671.992 4.933 2.078 1.27 1.091 2.187 2.345 2.637 3.023a1.62 1.62 0 0 1 0 1.798c-.45.678-1.367 1.932-2.637 3.023C11.67 13.008 9.981 14 8 14c-1.981 0-3.671-.992-4.933-2.078C1.797 10.83.88 9.576.43 8.898a1.62 1.62 0 0 1 0-1.798c.45-.677 1.367-1.931 2.637-3.022C4.33 2.992 6.019 2 8 2ZM1.679 7.932a.12.12 0 0 0 0 .136c.411.622 1.241 1.75 2.366 2.717C5.176 11.758 6.527 12.5 8 12.5c1.473 0 2.825-.742 3.955-1.715 1.124-.967 1.954-2.096 2.366-2.717a.12.12 0 0 0 0-.136c-.412-.621-1.242-1.75-2.366-2.717C10.824 4.242 9.473 3.5 8 3.5c-1.473 0-2.825.742-3.955 1.715-1.124.967-1.954 2.096-2.366 2.717ZM8 10a2 2 0 1 1-.001-3.999A2 2 0 0 1 8 10Z">
                 </path>
              </svg>
           </button>
        </div>
     </div>
  </div>
  <div class="col-8 float-left p-4 mt-n4">
     <form>
        <input class="form-control width-full" type="text" placeholder="Nombre del territorio"
           aria-label="Nombre del territorio" />
        <input class="form-control mt-2 width-full" type="text" placeholder="Número" aria-label="Número" />
        <select class="form-select mb-0 mt-2 width-full" aria-label="Preference">
           <option>Capitán asignado</option>
        </select>

        <p class="f5 mt-2 mb-n1">Fecha asignado:</p>
        <input class="form-control mt-1" type="date" placeholder="Hora de inicio" aria-label="Hora de inicio"
           style="width:24.5%;" />
        <div class="form-checkbox mt-3">
           <label>
              <input type="checkbox" />
              <em class="highlight">Campaña</em>
           </label>
        </div>
        <p class="f5 mt-2 mb-n1">Fecha terminado:</p>
        <input class="form-control mt-1" type="date" placeholder="Hora de inicio" aria-label="Hora de inicio"
           style="width:24.5%;" />
        <p class="f5 mt-2 mb-n1">Anotaciones:</p>
        <textarea class="form-control width-full mt-2" type="text"></textarea>
        <br><br>
        <div class="form-actions">
           <button type="submit" class="btn btn-primary">Guardar</button>
           <button class="btn btn-outline" type="button">Actualizar</button>
           <button type="button" class="btn btn-danger">
              <!-- <%= octicon "trashcan" %> -->
              <svg class="octicon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" width="16"
                 height="16">
                 <path fill-rule="evenodd"
                    d="M6.5 1.75a.25.25 0 01.25-.25h2.5a.25.25 0 01.25.25V3h-3V1.75zm4.5 0V3h2.25a.75.75 0 010 1.5H2.75a.75.75 0 010-1.5H5V1.75C5 .784 5.784 0 6.75 0h2.5C10.216 0 11 .784 11 1.75zM4.496 6.675a.75.75 0 10-1.492.15l.66 6.6A1.75 1.75 0 005.405 15h5.19c.9 0 1.652-.681 1.741-1.576l.66-6.6a.75.75 0 00-1.492-.149l-.66 6.6a.25.25 0 01-.249.225h-5.19a.25.25 0 01-.249-.225l-.66-6.6z">
                 </path>
              </svg>
              <span>Eliminar</span>
           </button>
        </div>
     </form>
  </div>
</div>