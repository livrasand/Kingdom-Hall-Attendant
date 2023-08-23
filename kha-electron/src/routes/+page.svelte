<svelte:head>
  <title>Kingdom Hall Attendant</title>
</svelte:head>

<main class="mb-6">
  <div class="Header color-bg-inset">
    <!-- Image item  -->
    <div class="Header-item">
       <img class="avatar CircleBadge" height="100" alt="@octocat" src="/img/GoAttendantLogo.png" width="100">
       <div class="d-table col-12">
          <div class="col-10 d-table-cell v-align-middle pl-4">
             <h2 class="text-normal lh-condensed color-fg-default">Apellidos, Nombres</h2>
             <p class="h4 color-fg-muted text-normal mb-2"> </p>
             <p class="color-fg-muted text-small">usuario@correo.com</p>
          </div>
       </div>
    </div>
 </div>
 <div class="container-lg clearfix">
    <div class="col-4 float-left p-3">
       <div class="col-6 width-full">
          <a class="d-block color-shadow-large px-2 pt-2 pb-2 position-relative rounded-2 overflow-hidden no-underline" href="/dashboard/congregacion">
             <div class="position-absolute top-0 left-2" style="margin-top:2%;"><i class="jwIcon e51"></i></div>
             <h5 class="color-fg-default" style="margin-left: 25%;">Congregación</h5>
             <p class="color-fg-muted text-small" style="margin-left: 25%;">
                Administra la información de la congregación y de los publicadores
             </p>
          </a>
       </div>
    </div>
    <div class="col-4 float-left p-3">
       <div class="col-6 width-full">
          <a class="d-block color-shadow-large px-2 pt-2 pb-2 position-relative rounded-2 overflow-hidden no-underline" href="/dashboard/vidayministerio">
             <div class="position-absolute top-0 left-2" style="margin-top:2%;"><i class="jwIcon e118"></i></div>
             <h5 class="color-fg-default" style="margin-left: 25%;">Vida y Ministerio</h5>
             <p class="color-fg-muted text-small" style="margin-left: 25%;">
                Programa automáticamente las asignaciones para la reunión
             </p>
          </a>
       </div>
    </div>
    <div class="col-4 float-left p-3">
       <div class="col-6 width-full">
          <a class="d-block color-shadow-large px-2 pt-2 pb-2 position-relative rounded-2 overflow-hidden no-underline" href="/dashboard/estudioatalaya">
             <div class="position-absolute top-0 left-2" style="margin-top:2%;"> <i class="jwIcon e95"></i></div>
             <h5 class="color-fg-default" style="margin-left: 25%;">Estudio de la Atalaya</h5>
             <p class="color-fg-muted text-small" style="margin-left: 25%;">
                Programa automáticamente los roles y las asignaciones para la reunión
             </p>
          </a>
       </div>
    </div>
 </div>
 <div class="container-lg clearfix">
    <div class="col-4 float-left p-3">
       <div class="col-6 width-full">
          <a class="d-block color-shadow-large px-2 pt-2 pb-2 position-relative rounded-2 overflow-hidden no-underline" href="/dashboard/orgreuniones">
             <div class="position-absolute top-0 left-2" style="margin-top:2%;"> <i class="jwIcon e186"></i></div>
             <h5 class="color-fg-default" style="margin-left: 25%;">Organización de las reuniones</h5>
             <p class="color-fg-muted text-small" style="margin-left: 25%;">
                Coordine los voluntarios de la plataforma, acomodadores, entre otros
             </p>
          </a>
       </div>
    </div>
    <div class="col-4 float-left p-3">
       <div class="col-6 width-full">
          <a class="d-block color-shadow-large px-2 pt-2 pb-2 position-relative rounded-2 overflow-hidden no-underline" href="/dashboard/oradorespublicos">
             <div class="position-absolute top-0 left-2" style="margin-top:2%;"><i class="jwIcon e175"></i></div>
             <h5 class="color-fg-default" style="margin-left: 25%;">Oradores públicos</h5>
             <p class="color-fg-muted text-small" style="margin-left: 25%;">
                Organiza las visitas y las salidas de los oradores de la congregación
             </p>
          </a>
       </div>
    </div> 
    <div class="col-4 float-left p-3">
      <div class="col-6 width-full">
         <a class="d-block color-shadow-large px-2 pt-2 pb-2 position-relative rounded-2 overflow-hidden no-underline" href="/dashboard/bosquejos">
            <div class="position-absolute top-0 left-2" style="margin-top:2%;"><i class="jwIcon siete"></i></div>
            <h5 class="color-fg-default" style="margin-left: 25%;">Bosquejos</h5>
            <p class="color-fg-muted text-small" style="margin-left: 25%;">
               Vea los discursos públicos que se han impartido en su congregación o fuera
            </p>
         </a>
      </div>
   </div>   
 </div>
 <div class="container-lg clearfix">
    <div class="col-4 float-left p-3">
       <div class="col-6 width-full">
          <a class="d-block color-shadow-large px-2 pt-2 pb-2 position-relative rounded-2 overflow-hidden no-underline" href="/dashboard/grupopredicacion">
             <div class="position-absolute top-0 left-2" style="margin-top:2%;"><i class="jwIcon e114"></i></div>
             <h5 class="color-fg-default" style="margin-left: 25%;">Grupos de predicación</h5>
             <p class="color-fg-muted text-small" style="margin-left: 25%;">
                Cree grupos, asigne a los miembros y organize visitas
             </p>
          </a>
       </div>
    </div>   
    <div class="col-4 float-left p-3">
      <div class="col-6 width-full" style="border-left: 6px solid #1a7f37;border-left-color: #1a7f37;border-color: #1a7f37;background-color: #dafbe1;border-radius: 6px;">
         <a class="d-block color-shadow-large px-2 pt-2 pb-2 position-relative rounded-2 overflow-hidden no-underline" href="/dashboard/configuracion">
            <div class="position-absolute top-0 left-2" style="margin-top:2%;"><i class="jwIcon e77"></i></div>
            <h5 class="color-fg-default" style="margin-left: 25%;">Configuración</h5>
            <p class="color-fg-muted text-small" style="margin-left: 25%;">
               Añada sus datos personales, cambie la apariencia o el idioma, entre otros más
            </p>
         </a>
      </div>
   </div> 
 </div>

</main>

<style lang="scss">
  
</style>
