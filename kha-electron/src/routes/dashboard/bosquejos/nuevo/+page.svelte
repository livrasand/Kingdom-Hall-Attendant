<svelte:head>
  <title>Bosquejos</title>
</svelte:head>

<div class="col-9 float-left pl-2">
  <p class="h1">Registrar un discurso impartido</p>
  <div class="container-lg clearfix">
    <form>
      <p class="f5 mt-2 mb-n1">Fecha impartido:</p>
      <input
        class="form-control mt-1"
        type="date"
        placeholder="Fecha impartido"
        aria-label="Fecha impartido"
        style="width:24.5%;"
      />
      <select class="form-select mb-2 mt-2 width-full" aria-label="Preference">
        <option>Seleccione un Orador</option>
      </select>
      <div class="flash-messages">
        <div class="flash">
          Este Orador es invitado de la congregación <button
            class="btn-link ml-1"
            type="button">Congregación</button
          >
        </div>
      </div>
      <!-- FIN DE LA NOTA -->
      <div class="form-checkbox mt-n2 mb-0">
        <label>
          <input type="checkbox" />
          <em class="highlight">Se ha quedado a la hospitalidad</em>
        </label>
      </div>
      <div class="form-checkbox mt-3 mb-0">
        <label>
          <input type="checkbox" />
          <em class="highlight">Se ha presentado a tiempo</em>
        </label>
      </div>
      <div class="form-checkbox mt-3 mb-2">
        <label>
          <input type="checkbox" />
          <em class="highlight">Se ha presentado al discurso</em>
        </label>
      </div>
      <p class="f5 mt-2 mb-n1">Anotaciones:</p>
      <textarea class="form-control width-full mt-2" type="text" />
      <br /><br />
      <div class="form-actions">
        <button type="submit" class="btn btn-primary">Guardar</button>
        <button type="button" class="btn btn-outline">
          <span data-component="text">
            <svg
              width="16"
              height="16"
              viewBox="0 0 16 16"
              fill="currentColor"
              style="display: inline-block; vertical-align: text-bottom;"
            >
              <path
                d="M.989 8 .064 2.68a1.342 1.342 0 0 1 1.85-1.462l13.402 5.744a1.13 1.13 0 0 1 0 2.076L1.913 14.782a1.343 1.343 0 0 1-1.85-1.463L.99 8Zm.603-5.288L2.38 7.25h4.87a.75.75 0 0 1 0 1.5H2.38l-.788 4.538L13.929 8Z"
              />
            </svg>
            <span contenteditable="true" class="Text-sc-125xb1i-0 cTqQd ml-2"
              >Enviar datos a su congregación</span
            >
          </span>
        </button>
        <button type="button" class="btn btn-danger">
          <!-- <%= octicon "trashcan" %> -->
          <svg
            class="octicon"
            xmlns="http://www.w3.org/2000/svg"
            viewBox="0 0 16 16"
            width="16"
            height="16"
          >
            <path
              fill-rule="evenodd"
              d="M6.5 1.75a.25.25 0 01.25-.25h2.5a.25.25 0 01.25.25V3h-3V1.75zm4.5 0V3h2.25a.75.75 0 010 1.5H2.75a.75.75 0 010-1.5H5V1.75C5 .784 5.784 0 6.75 0h2.5C10.216 0 11 .784 11 1.75zM4.496 6.675a.75.75 0 10-1.492.15l.66 6.6A1.75 1.75 0 005.405 15h5.19c.9 0 1.652-.681 1.741-1.576l.66-6.6a.75.75 0 00-1.492-.149l-.66 6.6a.25.25 0 01-.249.225h-5.19a.25.25 0 01-.249-.225l-.66-6.6z"
            />
          </svg>
          <span>Eliminar</span>
        </button>
      </div>
    </form>
  </div>
</div>
