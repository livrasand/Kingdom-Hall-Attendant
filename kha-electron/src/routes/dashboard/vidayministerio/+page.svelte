<script>
  import { onMount } from 'svelte';

  let link = 'link-vidayministerio';
  onMount(() => {
    let elem = document.getElementById(link);
    let atributo = document.createAttribute('aria-current');
    atributo.value = "page";
    elem.setAttributeNode(atributo);
  });
</script>

<svelte:head>
  <title>Vida y Ministerio</title>
</svelte:head>

<h1 class="pagetitle">Vida y Ministerio</h1>
<p>En construcción</p>

