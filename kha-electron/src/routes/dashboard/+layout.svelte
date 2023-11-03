<script>
  import SideBar from "$lib/SideBar.svelte";
</script>

<style>
  .container-xl {
    padding: 0 10px;
  }
</style>

<link href="/css/jw-icons-for-options.css" rel="stylesheet" />
<link rel="stylesheet" href="/static/css/style.css">

<SideBar />
  <div class="container-xl mt-6">
    <slot />
</div>
