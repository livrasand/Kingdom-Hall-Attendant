<script>
  import SideBar from "$lib/SideBar.svelte";
</script>

<div class="container-xl mt-6">
  <div class="col-3 float-left pr-2">
     <div class="">
        <SideBar />
     </div>
  </div>
  <div class="col-9 float-left pl-2">
    <slot />
  </div>
</div>
