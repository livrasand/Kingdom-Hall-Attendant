<script>
   import { onMount } from 'svelte';
   import Input from '../../../lib/Input.svelte';
   import { load, save } from './congregacion';

   let formCongregacion = {
      c_nombre: '',
      c_numero: '',
      c_d_entresemana: '',
      c_h_entresemana: '',
      c_d_finsemana: '',
      c_h_finsemana: '',
      c_direccion: '',
      c_n_super: '',
      c_t_super: '',
      c_circuito: ''
   };

   onMount(async () => {
		try {
         let rows = await load();
         console.log(rows);
         formCongregacion.c_nombre = rows[0].nombre;
         formCongregacion.c_numero = rows[0].numero;
         formCongregacion.c_d_entresemana = rows[0].d_entresemana;
         formCongregacion.c_h_entresemana = rows[0].h_entresemana;
         formCongregacion.c_d_finsemana = rows[0].d_finsemana;
         formCongregacion.c_h_finsemana = rows[0].h_finsemana;
         formCongregacion.c_direccion = rows[0].direccion;
         formCongregacion.c_n_super = rows[0].n_super;
         formCongregacion.c_t_super = rows[0].t_super;
         formCongregacion.c_circuito = rows[0].circuito;
      } catch (error) {
         console.error(error);
      }
	});

   function sendData(e) {
      e.preventDefault();
      save(formCongregacion);
   }
</script>

<svelte:head>
  <title>Congregación</title>
</svelte:head>

<div class="">
  <div class="tabnav">
     <nav class="tabnav-tabs" aria-label="Foo bar">
        <a class="tabnav-tab" href="/dashboard/congregacion" aria-current="page">Congregación</a>
        <a class="tabnav-tab" href="/dashboard/congregacion/publicadores">Publicadores</a>
     </nav>
  </div>
</div>
<form on:submit|preventDefault={sendData}>
   <Input id="c_nombre" placeholder="Nombre" style="width: 78%;" bind:value={formCongregacion.c_nombre} />
   <Input id="c_num" placeholder="Número" label="Número" style="width:20%;" bind:value={formCongregacion.c_numero} />
  <br>
  <p class="f4 mt-2 mb-0">Reunión de entre semana</p>
  <div class="radio-group">
     <input name="c_d_entresemana" value="Lunes" class="radio-input" id="option-a" type="radio" bind:group={formCongregacion.c_d_entresemana}>
     <label class="radio-label" for="option-a">Lunes</label>
     <input name="c_d_entresemana" value="Martes" class="radio-input" id="option-b" type="radio" bind:group={formCongregacion.c_d_entresemana}>
     <label class="radio-label" for="option-b">Martes</label>
     <input name="c_d_entresemana" value="Miércoles" class="radio-input" id="option-c" type="radio" bind:group={formCongregacion.c_d_entresemana}>
     <label class="radio-label" for="option-c">Miércoles</label>
     <input name="c_d_entresemana" value="Jueves" class="radio-input" id="option-d" type="radio" bind:group={formCongregacion.c_d_entresemana}>
     <label class="radio-label" for="option-d">Jueves</label>
     <input name="c_d_entresemana" value="Viernes" class="radio-input" id="option-e" type="radio" bind:group={formCongregacion.c_d_entresemana}>
     <label class="radio-label" for="option-e">Viernes</label>
     <input name="c_d_entresemana" value="Sábado" class="radio-input" id="option-f" type="radio" bind:group={formCongregacion.c_d_entresemana}>
     <label class="radio-label" for="option-f">Sábado</label>
     <input name="c_d_entresemana" value="Domingo" class="radio-input" id="option-g" type="radio" bind:group={formCongregacion.c_d_entresemana}>
     <label class="radio-label" for="option-g">Domingo</label>
  </div>
  <input name="c_h_entresemana" class="form-control ml-1" type="time" placeholder="Hora de inicio" aria-label="Hora de inicio" style="width:15%;" bind:value={formCongregacion.c_h_entresemana} />
  <br>
  <p class="f4 mt-2 mb-0">Reunión de fin de semana</p>
  <div class="radio-group">
     <input name="c_d_finsemana" value="Lunes" class="radio-input" id="option-h" type="radio" bind:group={formCongregacion.c_d_finsemana}>
     <label class="radio-label" for="option-h">Lunes</label>
     <input name="c_d_finsemana" value="Martes" class="radio-input" id="option-i" type="radio" bind:group={formCongregacion.c_d_finsemana}>
     <label class="radio-label" for="option-i">Martes</label>
     <input name="c_d_finsemana" value="Miércoles" class="radio-input" id="option-j" type="radio" bind:group={formCongregacion.c_d_finsemana}>
     <label class="radio-label" for="option-j">Miércoles</label>
     <input name="c_d_finsemana" value="Jueves" class="radio-input" id="option-k" type="radio" bind:group={formCongregacion.c_d_finsemana}>
     <label class="radio-label" for="option-k">Jueves</label>
     <input name="c_d_finsemana" value="Viernes" class="radio-input" id="option-l" type="radio" bind:group={formCongregacion.c_d_finsemana}>
     <label class="radio-label" for="option-l">Viernes</label>
     <input name="c_d_finsemana" value="Sábado" class="radio-input" id="option-m" type="radio" bind:group={formCongregacion.c_d_finsemana}>
     <label class="radio-label" for="option-m">Sábado</label>
     <input name="c_d_finsemana" value="Domingo" class="radio-input" id="option-n" type="radio" bind:group={formCongregacion.c_d_finsemana}>
     <label class="radio-label" for="option-n">Domingo</label> 
   </div>
   <input name="c_h_finsemana" class="form-control ml-1" type="time" placeholder="Hora de inicio" aria-label="Hora de inicio" style="width:15%;" bind:value={formCongregacion.c_h_finsemana} />
  <br>
  <p class="f4 mb-0">Dirección del Salón del Reino</p>
  <textarea id="c_direccion" name="c_direccion" class="form-control width-full mb-3" bind:value={formCongregacion.c_direccion}></textarea>
  <br>  
  <input name="c_n_super" class="form-control" type="text" placeholder="Superintendente de circuito" aria-label="Superintendente de circuito " style="width: 59%;" bind:value={formCongregacion.c_n_super} />
  <input name="c_t_super" class="form-control" type="number" placeholder="Número de teléfono" aria-label="Número de teléfono" style="width:20%;" bind:value={formCongregacion.c_t_super} />  
  <input name="c_circuito" class="form-control" type="text" placeholder="Circuito" aria-label="Circuito" style="width:20%;" bind:value={formCongregacion.c_circuito} />
  <br><br>
  <div class="form-actions">
     <button type="submit" class="btn btn-primary">Guardar</button>     
  </div>
</form>