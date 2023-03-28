
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
                <h4 class="text-normal lh-condensed color-fg-default">Apellidos, Nombre</h4>
                <p class="h4 color-fg-muted text-normal mb-2"> </p>
                <p class="color-fg-muted text-small">usuario@correo.com</p>
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
    <a class="menu-item" href="/dashboard/consejooratoria" aria-current={$page.url.pathname === '/dashboard/consejooratoria' ? 'page' : undefined}>
    <i class="jwIcon e185"></i>
    Consejo de la Oratoria
    </a>
    <a class="menu-item" href="/dashboard/esquemapresidente" aria-current={$page.url.pathname === '/dashboard/esquemapresidente' ? 'page' : undefined}>
    <i class="jwIcon e23"></i>
    Esquema del Presidente
    </a>
    <a class="menu-item" href="/dashboard/soportetecnico" aria-current={$page.url.pathname === '/dashboard/soportetecnico' ? 'page' : undefined}>
    <i class="jwIcon e35"></i>
    Soporte tecnico
    </a>
    <a class="menu-item" href="/dashboard/orgreuniones" aria-current={$page.url.pathname === '/dashboard/orgreuniones' ? 'page' : undefined}>
    <i class="jwIcon e186"></i>
    Organización de las reuniones
    </a>
    <a class="menu-item" href="/dashboard/oradorespublicos" aria-current={$page.url.pathname === '/dashboard/oradorespublicos' ? 'page' : undefined}>
    <i class="jwIcon e175"></i>
    Oradores públicos
    </a>
    <a class="menu-item" href="/dashboard/hospitalidades" aria-current={$page.url.pathname === '/dashboard/hospitalidades' ? 'page' : undefined}>
    <i class="jwIcon e53"></i>
    Hospitalidades
    </a>
    <a class="menu-item" href="/dashboard/bosquejos" aria-current={$page.url.pathname === '/dashboard/bosquejos' ? 'page' : undefined}>
    <i class="jwIcon siete"></i>
    Bosquejos
    </a>
    <a class="menu-item" href="/dashboard/limpieza" aria-current={$page.url.pathname === '/dashboard/limpieza' ? 'page' : undefined}>
    <i class="jwIcon e111"></i>
    Limpieza y Matenimiento
    </a>  
    <a class="menu-item" href="/dashboard/territorios" aria-current={$page.url.pathname === '/dashboard/territorios' ? 'page' : undefined}>
    <i class="jwIcon e33"></i>
    Territorios
    </a>
    <a class="menu-item" href="/dashboard/visitassc" aria-current={$page.url.pathname === '/dashboard/visitassc' ? 'page' : undefined}>
    <i class="jwIcon e87"></i>
    Visitas del Superintendente de Circuito 
    </a>
    <a class="menu-item" href="/dashboard/cuidadocj" aria-current={$page.url.pathname === '/dashboard/cuidadocj' ? 'page' : undefined}>
    <i class="jwIcon e17"></i>
    Cuidado de cesped y jardin
    </a>
    <a class="menu-item" href="/dashboard/mantenimientoldc" aria-current={$page.url.pathname === '/dashboard/mantenimientoldc' ? 'page' : undefined}>
    <i class="jwIcon e172"></i>
    Matenimiento de LDC
    </a>
    <a class="menu-item" href="/dashboard/grupopredicacion" aria-current={$page.url.pathname === '/dashboard/grupopredicacion' ? 'page' : undefined}>
    <i class="jwIcon e114"></i>
    Grupos de predicación
    </a>
    <a class="menu-item" href="/dashboard/visitaspastoreo" aria-current={$page.url.pathname === '/dashboard/visitaspastoreo' ? 'page' : undefined}>
    <i class="jwIcon e106"></i>
    Visitas de pastoreo
    </a>
    <a class="menu-item" href="/dashboard/exhibidores" aria-current={$page.url.pathname === '/dashboard/exhibidores' ? 'page' : undefined}>
    <i class="jwIcon e140"></i>
    Mesas y exhibidores portatiles
    </a>
    <a class="menu-item" href="/dashboard/serviciocampo" aria-current={$page.url.pathname === '/dashboard/serviciocampo' ? 'page' : undefined}>
    <i class="jwIcon e56"></i>
    Servicio del campo
    </a>
    <a class="menu-item" href="/dashboard/informes" aria-current={$page.url.pathname === '/dashboard/informes' ? 'page' : undefined}>
    <i class="jwIcon e184"></i>
    Informes
    </a>
    <a class="menu-item" href="/dashboard/contabilidad" aria-current={$page.url.pathname === '/dashboard/contabilidad' ? 'page' : undefined}>
    <i class="jwIcon e24"></i>
    Contabilidad
    </a>
    <a class="menu-item" href="/dashboard/asistenciareu" aria-current={$page.url.pathname === '/dashboard/asistenciareu' ? 'page' : undefined}>
    <i class="jwIcon e173"></i>
    Asistencia a las reuniones
    </a>
    <a class="menu-item" href="/dashboard/literrevistas" aria-current={$page.url.pathname === '/dashboard/literrevistas' ? 'page' : undefined}>
    <i class="jwIcon e40"></i>
    Literatura y revistas
    </a>
    <a class="menu-item" href="/dashboard/asuntosjudiciales" aria-current={$page.url.pathname === '/dashboard/asuntosjudiciales' ? 'page' : undefined}>
    <i class="jwIcon e46"></i>
    Asuntos judiciales
    </a>
    <a class="menu-item" href="/dashboard/estadisticas" aria-current={$page.url.pathname === '/dashboard/estadisticas' ? 'page' : undefined}>
    <i class="jwIcon e181"></i>
    Estadisticas de la congregacion
    </a>
    <a class="menu-item" href="/dashboard/copias" aria-current={$page.url.pathname === '/dashboard/copias' ? 'page' : undefined}>
    <i class="jwIcon e120"></i>
    Copias de seguridad
    </a>
    <a class="menu-item" href="/dashboard/configuracion" aria-current={$page.url.pathname === '/dashboard/configuracion' ? 'page' : undefined}>
    <i class="jwIcon e77"></i>
    Configuracion
    </a>
 </nav>