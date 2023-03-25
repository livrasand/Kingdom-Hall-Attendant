<svelte:head>
  <title>Publicadores</title>
</svelte:head>

<h1 class="pagetitle">Publicadores</h1>

<div class="">
  <div class="tabnav">
     <nav class="tabnav-tabs" aria-label="Foo bar">
      <a class="tabnav-tab" href="/dashboard/congregacion">Congregación</a>
      <a class="tabnav-tab" href="/dashboard/congregacion/publicadores" aria-current="page">Publicadores</a>
     </nav>
  </div>
</div>
<form id="form-congregacion">
  <input name="c_nombre" class="form-control" type="text" placeholder="Congregación" aria-label="Congregación" style="width: 79%;" />
  <input name="c_num" class="form-control" type="number" placeholder="Número" aria-label="Número" style="width:20%;" />
  <br>
  <p class="f4 mt-2 mb-0">Reunión de entre semana</p>
  <div class="radio-group">
     <input name="c_d_entresemana" value="Lunes" class="radio-input" id="option-a" type="radio">
     <label class="radio-label" for="option-a">Lunes</label>
     <input name="c_d_entresemana" value="Martes" class="radio-input" id="option-b" type="radio">
     <label class="radio-label" for="option-b">Martes</label>
     <input name="c_d_entresemana" value="Miércoles" class="radio-input" id="option-c" type="radio">
     <label class="radio-label" for="option-c">Miércoles</label>
     <input name="c_d_entresemana" value="Jueves" class="radio-input" id="option-d" type="radio">
     <label class="radio-label" for="option-d">Jueves</label>
     <input name="c_d_entresemana" value="Viernes" class="radio-input" id="option-e" type="radio">
     <label class="radio-label" for="option-e">Viernes</label>
     <input name="c_d_entresemana" value="Sábado" class="radio-input" id="option-f" type="radio">
     <label class="radio-label" for="option-f">Sábado</label>
     <input name="c_d_entresemana" value="Domingo" class="radio-input" id="option-g" type="radio">
     <label class="radio-label" for="option-g">Domingo</label>                
     <input name="c_h_entresemana" class="form-control ml-1" type="time" placeholder="Hora de inicio" aria-label="Hora de inicio" style="width:24.5%;" />
  </div>
  <br>
  <p class="f4 mt-2 mb-0">Reunión de fin de semana</p>
  <div class="radio-group">
     <input name="c_d_finsemana" value="Lunes" class="radio-input" id="option-h" type="radio">
     <label class="radio-label" for="option-h">Lunes</label>
     <input name="c_d_finsemana" value="Martes" class="radio-input" id="option-i" type="radio">
     <label class="radio-label" for="option-i">Martes</label>
     <input name="c_d_finsemana" value="Miércoles" class="radio-input" id="option-j" type="radio">
     <label class="radio-label" for="option-j">Miércoles</label>
     <input name="c_d_finsemana" value="Jueves" class="radio-input" id="option-k" type="radio">
     <label class="radio-label" for="option-k">Jueves</label>
     <input name="c_d_finsemana" value="Viernes" class="radio-input" id="option-l" type="radio">
     <label class="radio-label" for="option-l">Viernes</label>
     <input name="c_d_finsemana" value="Sábado" class="radio-input" id="option-m" type="radio">
     <label class="radio-label" for="option-m">Sábado</label>
     <input name="c_d_finsemana" value="Domingo" class="radio-input" id="option-n" type="radio">
     <label class="radio-label" for="option-n">Domingo</label> 
     <input name="c_h_finsemana" class="form-control ml-1" type="time" placeholder="Hora de inicio" aria-label="Hora de inicio" style="width:24.5%;" />
  </div>
  <br>
  <p class="f4 mb-0">Dirección del Salón del Reino</p>
  <textarea id="c_direccion" name="c_direccion" class="form-control width-full mb-3" ></textarea>
  <br>  
  <input name="c_s_nombre" class="form-control" type="text" placeholder="Superintendente de circuito" aria-label="Superintendente de circuito " style="width: 59%;" />
  <input name="c_s_numero" class="form-control" type="number" placeholder="Número de teléfono" aria-label="Número de teléfono" style="width:20%;" />  
  <input name="c_circuito" class="form-control" type="text" placeholder="Circuito" aria-label="Circuito" style="width:20%;" />
  <br><br>
  <div class="form-actions">
     <button type="submit" class="btn btn-primary">Guardar cambios</button>
     <button type="button" class="btn btn-danger">
        <!-- <%= octicon "trashcan" %> -->
        <svg class="octicon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" width="16" height="16">
           <path fill-rule="evenodd" d="M6.5 1.75a.25.25 0 01.25-.25h2.5a.25.25 0 01.25.25V3h-3V1.75zm4.5 0V3h2.25a.75.75 0 010 1.5H2.75a.75.75 0 010-1.5H5V1.75C5 .784 5.784 0 6.75 0h2.5C10.216 0 11 .784 11 1.75zM4.496 6.675a.75.75 0 10-1.492.15l.66 6.6A1.75 1.75 0 005.405 15h5.19c.9 0 1.652-.681 1.741-1.576l.66-6.6a.75.75 0 00-1.492-.149l-.66 6.6a.25.25 0 01-.249.225h-5.19a.25.25 0 01-.249-.225l-.66-6.6z"></path>
        </svg>
        <span>Borrar todo</span>
     </button>
  </div>
</form>