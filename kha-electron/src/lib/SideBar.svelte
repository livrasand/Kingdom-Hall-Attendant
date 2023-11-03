
<script>
import { page } from '$app/stores';
 </script>

<div class="Header color-bg-inset">
   <!-- Image item  -->
   <div class="Header-item width-full">
      <a onclick="history.back()" style="cursor: pointer;" class="mr-2 ml-n2">
         <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24">
            <path d="M15.28 5.22a.75.75 0 0 1 0 1.06L9.56 12l5.72 5.72a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215l-6.25-6.25a.75.75 0 0 1 0-1.06l6.25-6.25a.75.75 0 0 1 1.06 0Z"></path>
         </svg>
      </a>
      <img class="avatar CircleBadge" height="100" alt="@octocat" src="https://github.com/octocat.png" width="100">
      <div class="d-table col-12">
         <div class="col-10 d-table-cell v-align-middle pl-4">
            <h2 class="text-normal lh-condensed color-fg-default" name="user">Apellidos, Nombre</h2>
            <p class="color-fg-muted text-small mt-4" name="user_email">usuario@correo.com</p>
         </div>
      </div>
   </div>
</div>