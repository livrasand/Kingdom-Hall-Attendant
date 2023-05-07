<script>
  import { onMount } from 'svelte';  
  import Input from '../../../lib/Input.svelte';
  import { load, save } from './configuracion';

  let formConfiguracion = {
    c_nombres: '',
    c_apellidos: '',
    c_correo_electronico: ''
  };

  onMount(async () => {
   try {
        let rows = await load();
        console.log(rows);
        formConfiguracion.c_nombres = rows[0].nombres;
        formConfiguracion.c_apellidos = rows[0].apellidos;
        formConfiguracion.c_correo_electronico = rows[0].correo_electronico;
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

<h1 class="pagetitle mb-4">Configuración</h1>
<form on:submit|preventDefault={sendData}>
  <center>
    <Input id="c_nombres" type="text" placeholder="Nombres" bind:value={formConfiguracion.c_nombres} />
  <Input id="c_apellidos" type="text" placeholder="Apellidos" bind:value={formConfiguracion.c_apellidos} />
  </center>  
  <Input id="c_correo_electronico" type="email" placeholder="Correo electrónico" bind:value={formConfiguracion.c_correo_electronico} />
  <div class="form-actions mt-4">
    <button type="submit" class="btn btn-primary">Guardar cambios</button>
  </div>
</form>