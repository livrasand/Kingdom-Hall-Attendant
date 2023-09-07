<!-- ErrorDisplay.svelte -->
<script>
    import { onMount, onDestroy } from "svelte";
  
    let errorMessage = "";
  
    // Función para mostrar el mensaje de error
    function showError(message) {
      errorMessage = message;
    }
  
    // Escuchar el evento IPC para manejar errores
    onMount(() => {
      window.electron.ipcRenderer.on("uncaughtException", (event, error) => {
        showError(`Error: ${error.message}`);
      });
    });
  
    // Limpiar la suscripción al destruir el componente
    onDestroy(() => {
      window.electron.ipcRenderer.removeAllListeners("uncaughtException");
    });
  </script>
  
  {#if errorMessage}
    <div class="error-message">{errorMessage}</div>
  {/if}
  
  <style>
    .error-message {
      color: red;
      font-weight: bold;
    }
  </style>
  