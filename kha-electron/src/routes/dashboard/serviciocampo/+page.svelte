<svelte:head>
  <title>Servicio del campo</title>
</svelte:head>

<div class="tabnav">                 
  <button class="btn btn-sm float-right btn-outline ml-2" type="button">Enviar informes a la sucursal</button>
  <a class="btn btn-sm float-right" href="#url" role="button">Registrar nuevo informe</a>
    <nav class="tabnav-tabs" aria-label="Foo bar">
       <a class="tabnav-tab" href="/dashboard/serviciocampo" aria-current="page">Servicio del campo</a>                     
    </nav>
 </div>

 <div class="container-lg clearfix">  
  <select class="form-select mt-2 width-full" aria-label="Preference">
      <option>Seleccione el publicador</option>
   </select>
   <input class="form-control mt-2" type="text" placeholder="Publicaciones" aria-label="Publicaciones" style="width: 20%;" /><br>
 <input class="form-control mt-2" type="text" placeholder="Presentaciones de videos" aria-label="Presentaciones de videos" style="width: 20%;" /><br>
 <input class="form-control mt-2" type="text" placeholder="Horas" aria-label="Horas" style="width: 20%;" /><br>
 <input class="form-control mt-2" type="text" placeholder="Revisitas" aria-label="Revisitas" style="width: 20%;" /><br>
 <input class="form-control mt-2" type="text" placeholder="Cursos bíblicos" aria-label="Cursos bíblicos" style="width: 20%;" />
 <div class="form-checkbox mt-3 mb-2">
  <label>
  <input type="checkbox" />
  <em class="highlight">Precursor auxiliar</em>
  </label>
</div>
 <p class="f5 mt-2 mb-n1">Anotaciones:</p>
                     <textarea class="form-control width-full mt-2" type="text"></textarea> 
                     <div class="color-bg-inset p-2 rounded mb-2 mt-2">SITUACIÓN DEL PUBLICADOR</div>
                     
                      <div class="radio-group">
                        <input class="radio-input" id="option-a" type="radio" name="options">
                        <label class="radio-label" for="option-a">Nuevo</label>
                        <input class="radio-input" id="option-b" type="radio" name="options">
                        <label class="radio-label" for="option-b">Regular</label>
                        <input class="radio-input" id="option-c" type="radio" name="options">
                        <label class="radio-label" for="option-c">Irregular</label>
                        <input class="radio-input" id="option-d" type="radio" name="options">
                        <label class="radio-label" for="option-d">Inactivo</label>
                        <input class="radio-input" id="option-e" type="radio" name="options">
                        <label class="radio-label" for="option-e">Reactivado</label>
                      </div>
                      <p class="f5 mt-2 mb-n1">Se mudó aquí el:</p>
                      <input class="form-control mt-1" type="date" placeholder="Se mudó aquí" aria-label="Se mudó aquí" style="width:24.5%;" />
                      <p class="f5 mt-2 mb-n1">Empezó a publicar en:</p>
                      <input class="form-control mt-1" type="date" placeholder="Empezó a publicar" aria-label="Empezó a publicar" style="width:24.5%;" />
                      <p class="f5 mt-2 mb-n1">Inactivo por última vez el día:</p>
                      <input class="form-control mt-1" type="date" placeholder="Inactivo por última vez" aria-label="Inactivo por última vez" style="width:24.5%;" />
                      <p class="f5 mt-2 mb-n1">Reactivado por última vez el día:</p>
                      <input class="form-control mt-1" type="date" placeholder="Reactivado por última vez" aria-label="Reactivado por última vez" style="width:24.5%;" />
                      
                     <br><br>
                     <div class="form-actions">
                        <button type="submit" class="btn btn-primary">Guardar</button>
                        <button type="submit" class="btn">Ver registro del publicador</button>                      
                        <button type="button" class="btn btn-danger">
                           <!-- <%= octicon "trashcan" %> -->
                           <svg class="octicon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" width="16" height="16">
                              <path fill-rule="evenodd" d="M6.5 1.75a.25.25 0 01.25-.25h2.5a.25.25 0 01.25.25V3h-3V1.75zm4.5 0V3h2.25a.75.75 0 010 1.5H2.75a.75.75 0 010-1.5H5V1.75C5 .784 5.784 0 6.75 0h2.5C10.216 0 11 .784 11 1.75zM4.496 6.675a.75.75 0 10-1.492.15l.66 6.6A1.75 1.75 0 005.405 15h5.19c.9 0 1.652-.681 1.741-1.576l.66-6.6a.75.75 0 00-1.492-.149l-.66 6.6a.25.25 0 01-.249.225h-5.19a.25.25 0 01-.249-.225l-.66-6.6z"></path>
                           </svg>
                           <span>Eliminar</span>
                        </button>
                     </div>
</div>