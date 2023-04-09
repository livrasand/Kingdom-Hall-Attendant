<script>
  import { onMount } from "svelte";
  import CheckBox from "../../../../lib/CheckBox.svelte";
  import Input from "../../../../lib/Input.svelte";
  import { load } from './publicadores';

  let publicadores = [];

  let formPublicador = {
    p_nombre: '',
    p_apellidos: '',
    p_sexo: '',
    p_cabeza: false,
    p_fecha_nacimiento: '',
    p_email: '',
    p_celular: '',
    p_telefono: '',
    p_bautizado: '',
    p_fecha_bautismo: '',
    p_grupo: '',
    p_nombramiento: ''
  }

  onMount(async () => {
		try {
         let rows = await load();
         publicadores = rows;
         formPublicador.p_nombre = publicadores[0].nombre;
         formPublicador.p_apellidos = publicadores[0].apellidos;
      } catch (error) {
         console.error(error);
      }
	});
</script>

<svelte:head>
  <title>Publicadores</title>
</svelte:head>

<div class="">
  <div class="tabnav">
     <nav class="tabnav-tabs" aria-label="Foo bar">
      <a class="tabnav-tab" href="/dashboard/congregacion">Congregación</a>
      <a class="tabnav-tab" href="/dashboard/congregacion/publicadores" aria-current="page">Publicadores</a>
     </nav>
  </div>
</div>
<div class="container-lg clearfix">
  <div class="col-4 float-left">
   {#each publicadores as publicador}
     <div class="Box">
         <div class="Box-row d-flex flex-items-center">
            <div class="flex-auto">
               <strong>{publicador.apellidos} , {publicador.nombre}</strong>
            </div>
            <button class="btn mr-2 btn-sm" type="button">
               <!-- <%= octicon "search" %> -->
               <svg class="octicon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" width="16" height="16">
                  <path d="M8 2c1.981 0 3.671.992 4.933 2.078 1.27 1.091 2.187 2.345 2.637 3.023a1.62 1.62 0 0 1 0 1.798c-.45.678-1.367 1.932-2.637 3.023C11.67 13.008 9.981 14 8 14c-1.981 0-3.671-.992-4.933-2.078C1.797 10.83.88 9.576.43 8.898a1.62 1.62 0 0 1 0-1.798c.45-.677 1.367-1.931 2.637-3.022C4.33 2.992 6.019 2 8 2ZM1.679 7.932a.12.12 0 0 0 0 .136c.411.622 1.241 1.75 2.366 2.717C5.176 11.758 6.527 12.5 8 12.5c1.473 0 2.825-.742 3.955-1.715 1.124-.967 1.954-2.096 2.366-2.717a.12.12 0 0 0 0-.136c-.412-.621-1.242-1.75-2.366-2.717C10.824 4.242 9.473 3.5 8 3.5c-1.473 0-2.825.742-3.955 1.715-1.124.967-1.954 2.096-2.366 2.717ZM8 10a2 2 0 1 1-.001-3.999A2 2 0 0 1 8 10Z"></path>
               </svg>
            </button>
         </div>
     </div>
   {/each}
  </div>
  <div class="col-8 float-left p-4">
     <p class="h2 mt-n5">Datos personales</p>
     <form>
        <Input id="p_nombre" placeholder="Nombre" style="width: 49%;" bind:value={formPublicador.p_nombre} />
        <Input id="p_apellidos" placeholder="Apellidos" style="width: 49%;" bind:value={formPublicador.p_apellidos} />
        <div class="radio-group mt-1">
           <input class="radio-input" id="option-a" type="radio" name="p_sexo" />
           <label class="radio-label" for="option-a">Hermano</label>
           <input class="radio-input" id="option-b" type="radio" name="p_sexo">
           <label class="radio-label" for="option-b">Hermana</label>    
         </div>
         <div class="form-checkbox mt-2">
           <CheckBox id="p_cabeza" placeholder="Cabeza de familia" bind:value={formPublicador.p_cabeza} />
         </div>
         {#if formPublicador.p_cabeza}
            <!-- MOSTRAR ESTA OPCIÓN SOLO SI ES CABEZA DE FAMILIA-->
            <button class="btn-link ml-1" type="button">Crear familia {formPublicador.p_apellidos}</button>
            <!-- FIN DE OPCIÓN-->
            <select class="form-select mb-2 mt-0" aria-label="Preference">
               <option>Seleccione una familia</option>
            </select>
            <!-- NOTA SOLO VISIBLE SI ES MIEMBRO DE LA FAMILIA -->        
            <div class="flash-messages">
               <div class="flash">
                  Este publicador es 
                  <select id="p_" class="form-select select-sm" aria-label="Preference">
                     <option>esposa</option>
                     <option>hija</option>
                     <option>hijo</option>
                  </select>
                  del hermano <button class="btn-link ml-1" type="button">{formPublicador.p_apellidos, formPublicador.p_nombre}</button>
               </div>
            </div>
            <!-- FIN DE LA NOTA -->
         {/if}
        
        <p class="f5 mb-0">Fecha de nacimiento</p>
        <input id="fecha_nacimiento" class="form-control" type="date" placeholder="Fecha de nacimiento" aria-label="Fecha de nacimiento" style="width:49%;" />
        <p class="f5 mb-0 mt-2">Dirección</p>
        <textarea class="form-control width-full" id="example-textarea"></textarea>
        <input id="p_email" class="form-control width-full mt-2" type="email" placeholder="Correo electrónico" aria-label="Correo electrónico" />
        <input id="p_celular" class="form-control width-full mt-2" type="number" placeholder="Celular" aria-label="Celular" />
        <input id="p_telefono" class="form-control width-full mt-2" type="number" placeholder="Teléfono" aria-label="Teléfono" />
        <hr>
        <div class="form-checkbox mt-3 mb-0">
           <label>
           <input id="p_bautizado" type="checkbox" />
           <em class="highlight">Bautizado</em>
           </label>
        </div>
        <p class="f5 mb-0">Fecha de bautizo</p>
        <input id="p_fecha_bautismo" class="form-control" type="date" placeholder="Fecha de bautizo" aria-label="Fecha de bautizo" style="width:49%;" />
        <p class="f5 mb-0 mt-2">Grupo de predicación</p>
        <select id="p_grupo" class="form-select" aria-label="Preference">
           <option>Seleccione un grupo</option>
        </select>
        <div class="container-lg clearfix mt-3">
           <div class="col-6 float-left p-0">
              <div class="form-checkbox mt-0 mb-0">
                 <label>
                 <input id="p_w" type="checkbox" />
                 <em class="">Recibe La Atalaya (edición de estudio)</em>
                 </label>
                 <br>
                 <label>
                 <input id="p_ga" type="checkbox" />
                 <em class="">Recibe la Guía de actividades</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">Publicador no bautizado</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">Publicador temporal</em>
                 </label>
                 <br>
                 <label>
                 <input id="p_ungido" type="checkbox" />
                 <em class="">Ungido</em>
                 </label>
                 <br>
                 <label>
                 <input id="p_nino" type="checkbox" />
                 <em class="">Niño</em>
                 </label>
                 <br>
                 <label>
                 <input id="p_ra" type="checkbox" />
                 <em class="">Readmitido</em>
                 </label>
                 <br>
                 <label>
                 <input id="p_ir" type="checkbox" />
                 <em class="">Irregular</em>
                 </label>
              </div>
           </div>
           <div class="col-6 float-left p-0">
              <label>
              <input type="checkbox" />
              <em class="">Sordo</em>
              </label>
              <br>
              <label>
              <input type="checkbox" />
              <em class="">Enfermo</em>
              </label>
              <br>
              <label>
              <input type="checkbox" />
              <em class="">Voluntario del LDC</em>
              </label>
              <br>
              <label>
              <input type="checkbox" />
              <em class="">Llaves del Salón del Reino</em>
              </label>
              <br>
              <label>
              <input type="checkbox" />
              <em class="">Utiliza Kingdom Hall Attendant</em>
              </label>
              <br>
              <label>
              <input type="checkbox" />
              <em class="">Censurado</em>
              </label>
              <br>
              <label>
              <input type="checkbox" />
              <em class="">Inactivo</em>
              </label>
              <br>
              <label>
              <input type="checkbox" />
              <em class="">Expulsado</em>
              </label>
              <br>
              <label>
              <input type="checkbox" />
              <em class="">Fallecido</em>
              </label>
           </div>
        </div>
        <hr>
        <p class="h2 mt-0">Datos espirituales</p>
        <div class="radio-group mt-1">
           <input class="radio-input" id="option-anciano" type="radio" name="p_nombramiento">
           <label class="radio-label" for="option-anciano">Anciano</label>
           <input class="radio-input" id="option-siervom" type="radio" name="p_nombramiento">
           <label class="radio-label" for="option-siervom">Siervo ministerial</label> 
           <input class="radio-input" id="option-ninguno" type="radio" name="p_nombramiento">
           <label class="radio-label" for="option-ninguno">Ninguno</label>    
        </div>
        <p class="f5 mb-0 mt-2">Privilegios de servicio</p>
        <select class="form-select" aria-label="Preference">
           <option>Ninguno</option>
           <option>Precursor auxiliar de continuo</option>
           <option>Precursor regular</option>
           <option>Precursor especial</option>
           <option>Misionero</option>
        </select>
        <p class="f5 mb-0 mt-2">Fecha de inicio</p>
        <input class="form-control" type="date" placeholder="Fecha de inicio" aria-label="Fecha de inicio" style="width:49%;" />
        <input class="form-control" type="number" placeholder="Número de precursor" aria-label="Número de precursor" style="width:49%;" />
        <p class="f5 mb-0 mt-2">Responsabilidades en la congregación</p>
        <div class="container-lg clearfix mt-3">
           <div class="col-6 float-left p-0">
              <div class="form-checkbox mt-0 mb-0">
                 <label>
                 <input type="checkbox" />
                 <em class="">Coordinador del cuerpo de ancianos</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">Secretario</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">Superintendente de servicio</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">Siervo de acomodadores</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">Siervo de sonido y video</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">Siervo de literatura</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">Coordinador de matenimiento</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">Comité de Mantenimiento del Salón del Reino</em>
                 </label>
              </div>
           </div>
           <div class="col-6 float-left p-0">
              <label>
              <input type="checkbox" />
              <em class="">Conductor del Estudio de La Atalaya</em>
              </label>    
              <br>
              <label>
              <input type="checkbox" />
              <em class="">Coordinador de discursos públicos</em>
              </label>
              <br>
              <label>
              <input type="checkbox" />
              <em class="">Siervo de informes</em>
              </label>
              <br>
              <label>
              <input type="checkbox" />
              <em class="">Siervo de cuentas</em>
              </label>
              <br>
              <label>
              <input type="checkbox" />
              <em class="">Siervo de territorios</em>
              </label>
              <br>
              <label>
              <input type="checkbox" />
              <em class="">Coordinador de limpieza</em>
              </label>
              <br>
              <label>
              <input type="checkbox" />
              <em class="">Superintendente de la reunión Vida y Ministerio Cristianos</em>
              </label>
           </div>
        </div>
        <hr>
        <p class="h2 mt-0">Utilización de participantes</p>
        <div class="color-bg-emphasis color-fg-on-emphasis p-2 rounded mb-2">TESOROS DE LA BIBLIA</div>
        <div class="container-lg clearfix mt-3">
           <div class="col-6 float-left p-0">
              <div class="form-checkbox mt-0 mb-0">
                 <label>
                 <input type="checkbox" />
                 <em class="">Presidente</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">Oración</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">Discurso (10 mins.)</em>
                 </label>
              </div>
           </div>
           <div class="col-6 float-left p-0">
              <label>
              <input type="checkbox" />
              <em class="">Busquemos perlas escondidas</em>
              </label>    
              <br>
              <label>
              <input type="checkbox" />
              <em class="">Consejero de la sala auxiliar</em>
              </label>
              <br>
              <label>
              <input type="checkbox" />
              <em class="">Lectura de la Biblia</em>
              </label>
           </div>
        </div>
        <div class="color-bg-attention-emphasis color-fg-on-emphasis p-2 rounded mb-2 mt-2">SEAMOS MEJORES MAESTROS</div>
        <div class="container-lg clearfix mt-3">
           <div class="col-6 float-left p-0">
              <div class="form-checkbox mt-0 mb-0">
                 <label>
                 <input type="checkbox" />
                 <em class="">Discusión de un video</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">Primera conversación</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">Revisita</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">No utilizar en la sala principal</em>
                 </label>
              </div>
           </div>
           <div class="col-6 float-left p-0">
              <label>
              <input type="checkbox" />
              <em class="">Curso bíblico</em>
              </label>    
              <br>
              <label>
              <input type="checkbox" />
              <em class="">Ayudante</em>
              </label>
              <br>
              <label>
              <input type="checkbox" />
              <em class="">Discurso (5 mins.)</em>
              </label>
              <br>
              <label>
              <input type="checkbox" />
              <em class="">Utilizar solo en la sala principal</em>
              </label>
           </div>
        </div>
        <div class="color-bg-closed-emphasis color-fg-on-emphasis p-2 rounded mb-2 mt-2">NUESTRA VIDA CRISTIANA</div>
        <div class="container-lg clearfix mt-3">
           <div class="col-6 float-left p-0">
              <div class="form-checkbox mt-0 mb-0">
                 <label>
                 <input type="checkbox" />
                 <em class="">Intervenciones</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">Estudio bíblico de la congregación</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">Lector</em>
                 </label>
              </div>
           </div>
        </div>
        <div class="color-bg-inset p-2 rounded mb-2 mt-2">ESTUDIO DE LA ATALAYA</div>
        <div class="container-lg clearfix mt-3">
           <div class="col-6 float-left p-0">
              <div class="form-checkbox mt-0 mb-0">
                 <label>
                 <input type="checkbox" />
                 <em class="">Discursante público local</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">Presidente de la reunión pública</em>
                 </label>
              </div>
           </div>
           <div class="col-6 float-left p-0">
              <div class="form-checkbox mt-0 mb-0">
                 <label>
                 <input type="checkbox" />
                 <em class="">Lector de La Atalaya</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">Anfitrión para las hospitalidades</em>
                 </label>
              </div>
           </div>
        </div>
        <div class="color-bg-inset p-2 rounded mb-2 mt-2">TAREAS</div>
        <div class="container-lg clearfix mt-3">
           <div class="col-6 float-left p-0">
              <div class="form-checkbox mt-0 mb-0">
                 <label>
                 <input type="checkbox" />
                 <em class="">Sonido</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">Plataforma</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">Anfitrión en Zoom</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">Mantenimiento</em>
                 </label>
              </div>
           </div>
           <div class="col-6 float-left p-0">
              <div class="form-checkbox mt-0 mb-0">
                 <label>
                 <input type="checkbox" />
                 <em class="">Micrófonos</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">Coanfitrión en Zoom</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">Acomodador</em>
                 </label>
              </div>
           </div>
        </div>
        <div class="color-bg-inset p-2 rounded mb-2 mt-2">SERVICIO DEL CAMPO</div>
        <div class="container-lg clearfix mt-3">
           <div class="col-6 float-left p-0">
              <div class="form-checkbox mt-0 mb-0">
                 <label>
                 <input type="checkbox" />
                 <em class="">Aprobado para predicación pública</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">Dirigir reuniones para el servicio del campo</em>
                 </label>
              </div>
           </div>
           <div class="col-6 float-left p-0">
              <div class="form-checkbox mt-0 mb-0">
                 <label>
                 <input type="checkbox" />
                 <em class="">Orar en reuniones para el servicio del campo</em>
                 </label>
              </div>
           </div>
        </div>
        <div class="color-bg-inset p-2 rounded mb-2 mt-2">LIMPIEZA</div>
        <div class="container-lg clearfix mt-3">
           <div class="col-6 float-left p-0">
              <div class="form-checkbox mt-0 mb-0">
                 <label>
                 <input type="checkbox" />
                 <em class="">Limpieza semanal del Salón del Reino</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">Limpieza después de la reunión</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">Cuidado del jardín</em>
                 </label>
              </div>
           </div>
           <div class="col-6 float-left p-0">
              <div class="form-checkbox mt-0 mb-0">
                 <label>
                 <input type="checkbox" />
                 <em class="">Limpieza mensual del Salón del Reino</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">Limpieza trimestral del Salón del Reino</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" />
                 <em class="">Cuidado del césped</em>
                 </label>
              </div>
           </div>
        </div>
        <br><br>
        <div class="form-actions">
           <button type="submit" class="btn btn-primary">Guardar</button>
           <button type="button" class="btn btn-danger">
              <!-- <%= octicon "trashcan" %> -->
              <svg class="octicon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" width="16" height="16">
                 <path fill-rule="evenodd" d="M6.5 1.75a.25.25 0 01.25-.25h2.5a.25.25 0 01.25.25V3h-3V1.75zm4.5 0V3h2.25a.75.75 0 010 1.5H2.75a.75.75 0 010-1.5H5V1.75C5 .784 5.784 0 6.75 0h2.5C10.216 0 11 .784 11 1.75zM4.496 6.675a.75.75 0 10-1.492.15l.66 6.6A1.75 1.75 0 005.405 15h5.19c.9 0 1.652-.681 1.741-1.576l.66-6.6a.75.75 0 00-1.492-.149l-.66 6.6a.25.25 0 01-.249.225h-5.19a.25.25 0 01-.249-.225l-.66-6.6z"></path>
              </svg>
              <span>Eliminar publicador</span>
           </button>
           <button type="button" class="btn btn-outline">
              <span data-component="text">
                 <svg width="16" height="16" viewBox="0 0 16 16" fill="currentColor" style="display: inline-block; vertical-align: text-bottom;">
                    <path  d="M.989 8 .064 2.68a1.342 1.342 0 0 1 1.85-1.462l13.402 5.744a1.13 1.13 0 0 1 0 2.076L1.913 14.782a1.343 1.343 0 0 1-1.85-1.463L.99 8Zm.603-5.288L2.38 7.25h4.87a.75.75 0 0 1 0 1.5H2.38l-.788 4.538L13.929 8Z"></path>
                 </svg>
                 <span contenteditable="true" class="Text-sc-125xb1i-0 cTqQd ml-2">Transferir publicador</span>
              </span>
           </button>
           <button type="button" class="btn tooltipped tooltipped-ne tooltipped-align-left-1 border ml-1" aria-label="Registro de publicador">
              <!-- <%= octicon "pencil" %> -->
              <span data-component="text">
                 <svg class="octicon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" width="16" height="16">
                    <path fill-rule="evenodd" d="M3 7.5a.5.5 0 0 1 .5-.5h2a.5.5 0 0 1 .5.5v3a.5.5 0 0 1-.5.5h-2a.5.5 0 0 1-.5-.5v-3Zm10 .25a.75.75 0 0 1-.75.75h-4.5a.75.75 0 0 1 0-1.5h4.5a.75.75 0 0 1 .75.75ZM10.25 11a.75.75 0 0 0 0-1.5h-2.5a.75.75 0 0 0 0 1.5h2.5Z"></path>
                    <path fill-rule="evenodd" d="M7.25 0h1.5c.966 0 1.75.784 1.75 1.75V3h3.75c.966 0 1.75.784 1.75 1.75v8.5A1.75 1.75 0 0 1 14.25 15H1.75A1.75 1.75 0 0 1 0 13.25v-8.5C0 3.784.784 3 1.75 3H5.5V1.75C5.5.784 6.284 0 7.25 0Zm3.232 4.5A1.75 1.75 0 0 1 8.75 6h-1.5a1.75 1.75 0 0 1-1.732-1.5H1.75a.25.25 0 0 0-.25.25v8.5c0 .138.112.25.25.25h12.5a.25.25 0 0 0 .25-.25v-8.5a.25.25 0 0 0-.25-.25ZM7 1.75v2.5c0 .138.112.25.25.25h1.5A.25.25 0 0 0 9 4.25v-2.5a.25.25 0 0 0-.25-.25h-1.5a.25.25 0 0 0-.25.25Z"></path>
                 </svg>
              </span>
           </button>
           <details class="details-reset details-overlay details-overlay-dark">
              <summary class="btn" aria-haspopup="dialog tooltipped tooltipped-ne tooltipped-align-left-1 border" aria-label="Historial de roles y asignaciones">
                 <!-- <%= octicon "pencil" %> -->
                 <span data-component="text">
                    <svg class="octicon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" width="16" height="16">
                       <path fill-rule="evenodd" d="m.427 1.927 1.215 1.215a8.002 8.002 0 1 1-1.6 5.685.75.75 0 1 1 1.493-.154 6.5 6.5 0 1 0 1.18-4.458l1.358 1.358A.25.25 0 0 1 3.896 6H.25A.25.25 0 0 1 0 5.75V2.104a.25.25 0 0 1 .427-.177ZM7.75 4a.75.75 0 0 1 .75.75v2.992l2.028.812a.75.75 0 0 1-.557 1.392l-2.5-1A.751.751 0 0 1 7 8.25v-3.5A.75.75 0 0 1 7.75 4Z"></path>
                    </svg>
                 </span>
              </summary>
              <details-dialog class="Box Box--overlay d-flex flex-column anim-fade-in fast" style="width: 90%;">
                 <div class="Box-header">
                    <button class="Box-btn-octicon btn-octicon float-right" type="button" aria-label="Close dialog" data-close-dialog>
                       <!-- <%= octicon "x" %> -->
                       <svg class="octicon octicon-x" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true">
                          <path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48L7.48 8z"></path>
                       </svg>
                    </button>
                    <h3 class="Box-title">Historial del publicador</h3>
                 </div>
                 <div class="overflow-auto">
                    <div class="container-lg clearfix width-full">
                       <div class="col-3 float-left border p-4">
                          Reunión Vida y Ministerios Cristianos
                       </div>
                       <div class="col-3 float-left border p-4">
                          Discursos públicos
                       </div>
                       <div class="col-3 float-left border p-4">
                          Asignaciones
                       </div>
                       <div class="col-3 float-left border p-4">
                          Tareas
                       </div>
                    </div>
                 </div>
                 <div class="Box-footer">
                    <button type="button" class="btn btn-block" data-close-dialog>Okidoki</button>
                 </div>
              </details-dialog>
           </details>
           <!-- Temporary overrides (don't use in production) -->
           <link href="index.css" rel="stylesheet" />
        </div>
     </form>
  </div>
</div>
