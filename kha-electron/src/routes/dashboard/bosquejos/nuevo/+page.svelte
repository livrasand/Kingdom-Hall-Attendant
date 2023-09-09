<script>
  import { onMount } from 'svelte';
  import { load, save, cargarOradores } from './nuevobosquejo';


  let formBosquejos = {
    id: '',
    fechaImpartido: '',
    orador: '',
    anotaciones: '',
    haHospitalidad: false,
    haPresentadoTiempo: false,
    haPresentadoDiscurso: false
  };

  let bosquejos = [];
  let oradoresPublicos = [];
  let oradoresForaneos = [];

  async function cargarDatos() {
  try {
    console.log("Fetching data...");
    bosquejos = await load();
    console.log("Data fetched:", bosquejos);

    // Cargar la lista de oradores
    oradoresPublicos = await cargarOradores();
    console.log("Oradores cargados:", oradoresPublicos);
  } catch (error) {
    console.error("Error fetching data:", error);
  }
}

  onMount(async () => {
    console.log("Component mounted. Calling cargarDatos()...");
    await cargarDatos();
  });

  async function guardarDatos() {
    try {
      await save(formBosquejos);
      // Limpia el formulario después de guardar
      formBosquejos = {
        id: '',
        fechaImpartido: '',
        orador: '',
        anotaciones: '',
        haHospitalidad: false,
        haPresentadoTiempo: false,
        haPresentadoDiscurso: false
      };
    } catch (error) {
      console.error('Error al guardar los datos', error);
    }
  }
</script>

<svelte:head>
  <title>Bosquejos</title>
</svelte:head>

<div class="col-9 float-left pl-2">
  <p class="h1">Registrar un discurso impartido</p>
  <div class="container-lg clearfix">
    <form on:submit={guardarDatos}>      
      <!-- Input para ID -->
      <input style="display:none;" id="id" bind:value={formBosquejos.id} />
      
      <!-- Input para Fecha impartido -->
      <p class="f5 mt-2 mb-n1">Fecha impartido:</p>
      <input class="form-control mt-1" type="date" placeholder="Fecha impartido" aria-label="Fecha impartido" style="width:24.5%;" bind:value={formBosquejos.fechaImpartido} />
      

      <select class="form-select mb-2 mt-2 width-full" aria-label="Orador" bind:value={formBosquejos.orador}>
        <option value="">Seleccione un Orador</option>
<!-- Renderizar oradoresPublicos -->
{#each oradoresPublicos as orador (orador.id)}
  <option value={orador.id}>{orador.nombre + ' ' + orador.apellidos}</option>
{/each}

<!-- Renderizar oradoresForaneos -->
{#each oradoresForaneos as orador (orador.id + '_foraneo')}
  <option value={orador.id}>{orador.nombre + ' ' + orador.apellidos} (Foráneo)</option>
{/each}
      </select>
      
      
      
      <!-- Checkbox para hospitalidad -->
      <div class="form-checkbox mt-3 mb-0">
        <label for="hospitalidadCheckbox">
          <input type="checkbox" id="hospitalidadCheckbox" bind:checked={formBosquejos.haHospitalidad} />
          <em class="highlight">Se ha quedado a la hospitalidad</em>
        </label>
      </div>
      
      <!-- Checkbox para presentado a tiempo -->
      <div class="form-checkbox mt-3 mb-0">
        <label for="tiempoCheckbox">
          <input type="checkbox" id="tiempoCheckbox" bind:checked={formBosquejos.haPresentadoTiempo} />
          <em class="highlight">Se ha presentado a tiempo</em>
        </label>
      </div>
      
      <!-- Checkbox para presentado al discurso -->
      <div class="form-checkbox mt-3 mb-2">
        <label for="discursoCheckbox">
          <input type="checkbox" id="discursoCheckbox" bind:checked={formBosquejos.haPresentadoDiscurso} />
          <em class="highlight">Se ha presentado al discurso</em>
        </label>
      </div>
      
      <!-- Textarea para anotaciones -->
      <p class="f5 mt-2 mb-n1">Anotaciones:</p>
      <textarea class="form-control width-full mt-2" type="text" bind:value={formBosquejos.anotaciones} />
      
      <!-- Botones de acción -->
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
          </span>
          <span contenteditable="true" class="Text-sc-125xb1i-0 cTqQd ml-2">
            Enviar datos a su congregación
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
