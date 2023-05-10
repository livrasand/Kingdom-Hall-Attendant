<script>
  let privilegios = [
		{ id: 1, text: `No especificado` },
		{ id: 2, text: `superintendente de circuito` },
		{ id: 3, text: `anciano` },
    { id: 4, text: `siervo ministerial` },
    { id: 5, text: `precursor regular` },
    { id: 6, text: `Ninguno de los anteriores` }
	];

  import { onMount } from 'svelte';  
  import Input from '../../../lib/Input.svelte';
  import { load, save } from './configuracion';

  let formConfiguracion = {
    c_nombres: '',
    c_apellidos: '',
    c_correo_electronico: '',
    user_profile_location: '',
    user_profile_pronouns_select: ''
  };

  onMount(async () => {
   try {
        let rows = await load();
        console.log(rows);
        formConfiguracion.c_nombres = rows[0].nombres;
        formConfiguracion.c_apellidos = rows[0].apellidos;
        formConfiguracion.c_correo_electronico = rows[0].correo_electronico;
        formConfiguracion.user_profile_location = rows[0].ubicacion;
        formConfiguracion.user_profile_pronouns_select = rows[0].user_profile_pronouns_select;
     } catch (error) {
        console.error(error);
     }
 });

  function sendData(e) {
     e.preventDefault();
     save(formConfiguracion);
  }
</script>

<svelte:head>
  <title>Configuración</title>
</svelte:head>

<!-- INICIO DE CONFIGURACIÓN -->
            <div data-view-component="true" class="container-md">          <turbo-frame id="settings-frame" data-turbo-action="advance">
            
  <!-- Public Profile -->
  <div data-view-component="true" class="Subhead mt-0 mb-0">
  <h2 id="public-profile-heading" data-view-component="true" class="Subhead-heading">Configuración</h2>
  
  
</div>  <div class="clearfix gutter d-flex flex-shrink-0 flex-column-reverse flex-md-row">
    <div class="col-12 col-md-8">
      
      <waiting-form data-catalyst="">
        <!-- '"` --><!-- </textarea></xmp> -->
        <form on:submit|preventDefault={sendData}>
            <div>       
              <dl class="form-group">                
              <dt><label for="user_profile_name">Nombre</label></dt>
                <dd class="d-inline-block">
                  <div>
    <input id="c_nombres" class="form-control" type="text" placeholder="Nombres" bind:value={formConfiguracion.c_nombres} />
  <input id="c_apellidos" class="form-control mt-2" type="text" placeholder="Apellidos" bind:value={formConfiguracion.c_apellidos} />
                  </div>  
                </dd>
              </dl>
              
            <dl class="form-group">
              <dt><label for="user_profile_email">Correo electrónico público</label></dt>
              <dd class="d-inline-block">
                <div>
                    <input class="form-control" type="email" bind:value={formConfiguracion.c_correo_electronico} id="c_correo_electronico">
                    <p class="note">
                      Su dirección de correo electrónico es privada. Para alternar la privacidad del correo electrónico, use la configuración de correo electrónico y desmarque "Mantener mi dirección de correo electrónico privada".
                    </p>
                </div>
              </dd>
            </dl>

                <dl class="form-group">
                  <dt><label for="user_profile_pronouns_select">Privilegio</label></dt>
                  <dd class="user-profile-bio-field-container js-length-limited-input-container">
                    <select bind:value={formConfiguracion.user_profile_pronouns_select} id="user_profile_pronouns_select" class="form-select js-profile-editable-pronouns-select form-select form-control">
                      {#each privilegios as privilegio}
                      <option value={privilegio}>
                        {privilegio.text}
                      </option>
                      {/each}                      
                    </select>
                    </dd>
                </dl>
                               
              <dl class="form-group">
                <dt><label for="user_profile_location">Ubicación</label></dt>
                <dd><input class="form-control" type="text"  name="user[profile_location]" id="user_profile_location" bind:value={formConfiguracion.user_profile_location}></dd>
              </dl>
              
                <p class="note mb-2">
                  Todos los campos de esta página son opcionales y se pueden eliminar en cualquier momento, y al completarlos, nos está dando su consentimiento para compartir estos datos dondequiera que aparezca su perfil de usuario. Consulte nuestra declaración de privacidad para obtener más información sobre cómo usamos esta información.
                </p>

              <p>
                  <button data-target="waiting-form.submit" data-action="click:waiting-form#submitPolitely" type="submit" data-view-component="true" class="btn Button--primary Button--medium Button">    <span class="Button-content">
      <span class="Button-label">Actualizar el perfil</span>
    </span>
</button>  

              </p>
          </div>
</form>      </waiting-form>

    </div>

    <div class="col-12 col-md-4">
      
<dl>
  <dt><label class="d-block mb-2">Foto de usuario</label></dt>
  <dd class="avatar-upload-container clearfix position-relative">
      <div class="avatar-upload">
        <details class="dropdown details-reset details-overlay">
          <summary aria-haspopup="menu" role="button">
            <img class="avatar rounded-2 avatar-user" src="/img/GoAttendantLogo.png" width="200" height="200">
            <div class="position-absolute color-bg-default rounded-2 color-fg-default px-2 py-1 left-0 bottom-0 ml-2 mb-2 border">
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-pencil">
    <path d="M11.013 1.427a1.75 1.75 0 0 1 2.474 0l1.086 1.086a1.75 1.75 0 0 1 0 2.474l-8.61 8.61c-.21.21-.47.364-.756.445l-3.251.93a.75.75 0 0 1-.927-.928l.929-3.25c.081-.286.235-.547.445-.758l8.61-8.61Zm.176 4.823L9.75 4.81l-6.286 6.287a.253.253 0 0 0-.064.108l-.558 1.953 1.953-.558a.253.253 0 0 0 .108-.064Zm1.238-3.763a.25.25 0 0 0-.354 0L10.811 3.75l1.439 1.44 1.263-1.263a.25.25 0 0 0 0-.354Z"></path>
</svg>
              Editar
            </div>
          </summary>
          <details-menu class="dropdown-menu dropdown-menu-se" style="z-index: 99" role="menu">
            <label for="avatar_upload" class="dropdown-item text-normal" style="cursor: pointer;" role="menuitem" tabindex="0">Sube una foto…</label>
          </details-menu>
        </details>

        
      </div>
  </dd>
</dl>

    </div>
  </div>
          </turbo-frame>
</div>
         <!-- FIN DE CONFIGURACIÓN -->