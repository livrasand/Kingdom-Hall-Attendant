
<script>
import { page } from '$app/stores';
 </script>

<nav class="menu" aria-label="Person settings">
    <div class="Header color-bg-inset menu-heading" id="menu-heading">
       <!-- Image item  -->
       <div class="Header-item">
          <a href="/" class="mr-2 ml-n2">
             <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24">
                <path d="M15.28 5.22a.75.75 0 0 1 0 1.06L9.56 12l5.72 5.72a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215l-6.25-6.25a.75.75 0 0 1 0-1.06l6.25-6.25a.75.75 0 0 1 1.06 0Z"></path>
             </svg>
             
          </a>
          <img class="avatar CircleBadge" height="50" alt="@octocat" src="/img/GoAttendantLogo.png" width="50">
          <div class="d-table col-12">
            <div class="col-10 d-table-cell v-align-middle pl-4">
               <h4 class="text-normal lh-condensed color-fg-default">nombre</h4>
               <p class="h4 color-fg-muted text-normal mb-2"></p>
               <p class="color-fg-muted text-small">correo</p>
             </div>
          </div>
       </div>
    </div>
    <a class="menu-item" href="/dashboard/congregacion" aria-current={$page.url.pathname === '/dashboard/congregacion' ? 'page' : undefined}>
    <i class="jwIcon e51"></i>
    Congregación
    </a>
    <a class="menu-item" href="/dashboard/vidayministerio" aria-current={$page.url.pathname === '/dashboard/vidayministerio' ? 'page' : undefined}>
    <i class="jwIcon e118"></i>
    Vida y Ministerio
    </a>
    <a class="menu-item" href="/dashboard/estudioatalaya" aria-current={$page.url.pathname === '/dashboard/estudioatalaya' ? 'page' : undefined}>
    <i class="jwIcon e95"></i>
    Estudio de la Atalaya
    </a>
    <a class="menu-item" href="/dashboard/orgreuniones" aria-current={$page.url.pathname === '/dashboard/orgreuniones' ? 'page' : undefined}>
    <i class="jwIcon e186"></i>
    Organización de las reuniones
    </a>
    <a class="menu-item" href="/dashboard/oradorespublicos" aria-current={$page.url.pathname === '/dashboard/oradorespublicos' ? 'page' : undefined}>
    <i class="jwIcon e175"></i>
    Oradores públicos
    </a>
    <a class="menu-item" href="/dashboard/bosquejos" aria-current={$page.url.pathname === '/dashboard/bosquejos' ? 'page' : undefined}>
    <i class="jwIcon siete"></i>
    Bosquejos
    </a>
    <a class="menu-item" href="/dashboard/grupopredicacion" aria-current={$page.url.pathname === '/dashboard/grupopredicacion' ? 'page' : undefined}>
    <i class="jwIcon e114"></i>
    Grupos de predicación
    </a>
    <a class="menu-item" href="/dashboard/configuracion" aria-current={$page.url.pathname === '/dashboard/configuracion' ? 'page' : undefined}>
    <i class="jwIcon e77"></i>
    Configuración
    </a>
 </nav>