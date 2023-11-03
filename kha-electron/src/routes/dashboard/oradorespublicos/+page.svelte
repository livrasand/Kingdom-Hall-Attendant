<script>
  import { onMount } from "svelte";
  import { load, loadById, save, eliminarOrador } from '$lib/oradorespublicos';

  let oradorespublicos = [];
  let formOrador = {
    id: '',
    nombre: '',
    apellidos: '',
    aprobado: false,
    correoElectronico: '',
    celular: '',
    telefono: '',
    nombramiento: '',
    discurso1: false,
    discurso2: false,
    discurso3: false,
    discurso4: false,
    discurso5: false,
    discurso6: false,
    discurso7: false,
    discurso8: false,
    discurso9: false,
    discurso10: false,
    discurso11: false,
    discurso12: false,
    discurso13: false,
    discurso14: false,
    discurso15: false,
    discurso16: false,
    discurso17: false,
    discurso18: false,
    discurso19: false,
    discurso20: false,
    discurso21: false,
    discurso22: false,
    discurso23: false,
    discurso24: false,
    discurso25: false,
    discurso26: false,
    discurso27: false,
    discurso28: false,
    discurso29: false,
    discurso30: false,
    discurso31: false,
    discurso32: false,
    discurso33: false,
    discurso34: false,
    discurso35: false,
    discurso36: false,
    discurso37: false,
    discurso38: false,
    discurso39: false,
    discurso40: false,
    discurso41: false,
    discurso42: false,
    discurso43: false,
    discurso44: false,
    discurso45: false,
    discurso46: false,
    discurso47: false,
    discurso48: false,
    discurso49: false,
    discurso50: false,
    discurso51: false,
    discurso52: false,
    discurso53: false,
    discurso54: false,
    discurso55: false,
    discurso56: false,
    discurso57: false,
    discurso58: false,
    discurso59: false,
    discurso60: false,
    discurso61: false,
    discurso62: false,
    discurso63: false,
    discurso64: false,
    discurso65: false,
    discurso66: false,
    discurso67: false,
    discurso68: false,
    discurso69: false,
    discurso70: false,
    discurso71: false,
    discurso72: false,
    discurso73: false,
    discurso74: false,
    discurso75: false,
    discurso76: false,
    discurso77: false,
    discurso78: false,
    discurso79: false,
    discurso80: false,
    discurso81: false,
    discurso82: false,
    discurso83: false,
    discurso84: false,
    discurso85: false,
    discurso86: false,
    discurso87: false,
    discurso88: false,
    discurso89: false,
    discurso90: false,
    discurso91: false,
    discurso92: false,
    discurso93: false,
    discurso94: false,
    discurso95: false,
    discurso96: false,
    discurso97: false,
    discurso98: false,
    discurso99: false,
    discurso100: false,
    discurso101: false,
    discurso102: false,
    discurso103: false,
    discurso104: false,
    discurso105: false,
    discurso106: false,
    discurso107: false,
    discurso108: false,
    discurso109: false,
    discurso110: false,
    discurso111: false,
    discurso112: false,
    discurso113: false,
    discurso114: false,
    discurso115: false,
    discurso116: false,
    discurso117: false,
    discurso118: false,
    discurso119: false,
    discurso120: false,
    discurso121: false,
    discurso122: false,
    discurso123: false,
    discurso124: false,
    discurso125: false,
    discurso126: false,
    discurso127: false,
    discurso128: false,
    discurso129: false,
    discurso130: false,
    discurso131: false,
    discurso132: false,
    discurso133: false,
    discurso134: false,
    discurso135: false,
    discurso136: false,
    discurso137: false,
    discurso138: false,
    discurso139: false,
    discurso140: false,
    discurso141: false,
    discurso142: false,
    discurso143: false,
    discurso144: false,
    discurso145: false,
    discurso146: false,
    discurso147: false,
    discurso148: false,
    discurso149: false,
    discurso150: false,
    discurso151: false,
    discurso152: false,
    discurso153: false,
    discurso154: false,
    discurso155: false,
    discurso156: false,
    discurso157: false,
    discurso158: false,
    discurso159: false,
    discurso160: false,
    discurso161: false,
    discurso162: false,
    discurso163: false,
    discurso164: false,
    discurso165: false,
    discurso166: false,
    discurso167: false,
    discurso168: false,
    discurso169: false,
    discurso170: false,
    discurso171: false,
    discurso172: false,
    discurso173: false,
    discurso174: false,
    discurso175: false,
    discurso176: false,
    discurso177: false,
    discurso178: false,
    discurso179: false,
    discurso180: false,
    discurso181: false,
    discurso182: false,
    discurso183: false,
    discurso184: false,
    discurso185: false,
    discurso186: false,
    discurso187: false,
    discurso188: false,
    discurso189: false,
    discurso190: false,
    discurso191: false,
    discurso192: false,
    discurso193: false,
    discurso194: false,
  };

  let isNew = true; // Variable para rastrear si se está creando un nuevo registro

  async function getData() {
    try {
      console.log("Fetching data...");
      let rows = await load();
      oradorespublicos = rows;
      console.log("Data fetched:", oradorespublicos);
    } catch (error) {
      console.error("Error fetching data:", error);
    }
  }

  async function selectData(id) {
    try {
      console.log("Selecting data for id:", id);
      const row = await loadById(id);
      formOrador = row;
      console.log("Selected data:", formOrador);
    } catch (error) {
      console.error("Error selecting data:", error);
    }
  }

  onMount(async () => {
    console.log("Component mounted. Calling getData()...");
    try {
      await getData();
    } catch (error) {
      console.error("Error onMount:", error);
    }
  });

  async function sendData(e) {
  e.preventDefault();
  try {
    console.log("Sending data:", formOrador);

    if (isNew) {
      await save(formOrador);
      console.log("Data saved successfully.");
    } else {
      console.log("Updating data...");
      // Implementa aquí la lógica para actualizar un registro existente
      // Debes asegurarte de que esta parte se esté ejecutando
    }

    if (formOrador && formOrador.id) {
      try {
        console.log("Reloading selected data...");
        const row = await loadById(formOrador.id);
        formOrador = row;
        console.log("Selected data reloaded:", formOrador);
      } catch (error) {
        console.error("Error reloading selected data:", error);
      }
    }

    isNew = true;
    
    await getData();
    console.log("Data re-fetched:", oradorespublicos);
  } catch (error) {
    console.error("Error sending data:", error);
  }
}

async function handleEliminarOrador() {
    const idOrador = formOrador.id; // Obtén el ID del orador que deseas eliminar

    try {
      await eliminarOrador(idOrador); // Llama a la función para eliminar el orador
      // Aquí debes actualizar la lista de oradores en el cliente para reflejar la eliminación
    } catch (error) {
      console.error('Error al eliminar el orador:', error);
    }
  }
</script> 

<svelte:head>
  <title>Oradores públicos</title>
</svelte:head>

<div class="tabnav">   
  <button class="btn btn-sm float-right" type="button" on:click={() => { isNew = true; formOrador = {} }}>Nuevo</button>
   <nav class="tabnav-tabs" aria-label="Foo bar">
      <a class="tabnav-tab" href="/dashboard/oradorespublicos" aria-current="page">Locales</a>
      <a class="tabnav-tab" href="/dashboard/oradorespublicos/foraneos">Foraneos</a>
   </nav>
</div>

<div class="container-lg clearfix">
  <div class="col-4 float-left">
   {#each oradorespublicos as oradorpublico}
     <div class="Box mb-2">
        <div class="Box-row d-flex flex-items-center">
           <div class="flex-auto">
            <strong>{oradorpublico.apellidos}, {oradorpublico.nombre}</strong>
           </div>
           <button class="btn mr-2 btn-sm" type="button" on:click={() => { selectData(oradorpublico.id) }}>
              <!-- <%= octicon "search" %> -->
              <svg class="octicon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" width="16" height="16">
                 <path d="M8 2c1.981 0 3.671.992 4.933 2.078 1.27 1.091 2.187 2.345 2.637 3.023a1.62 1.62 0 0 1 0 1.798c-.45.678-1.367 1.932-2.637 3.023C11.67 13.008 9.981 14 8 14c-1.981 0-3.671-.992-4.933-2.078C1.797 10.83.88 9.576.43 8.898a1.62 1.62 0 0 1 0-1.798c.45-.677 1.367-1.931 2.637-3.022C4.33 2.992 6.019 2 8 2ZM1.679 7.932a.12.12 0 0 0 0 .136c.411.622 1.241 1.75 2.366 2.717C5.176 11.758 6.527 12.5 8 12.5c1.473 0 2.825-.742 3.955-1.715 1.124-.967 1.954-2.096 2.366-2.717a.12.12 0 0 0 0-.136c-.412-.621-1.242-1.75-2.366-2.717C10.824 4.242 9.473 3.5 8 3.5c-1.473 0-2.825.742-3.955 1.715-1.124.967-1.954 2.096-2.366 2.717ZM8 10a2 2 0 1 1-.001-3.999A2 2 0 0 1 8 10Z"></path>
              </svg>
           </button>
        </div>
     </div>
   {/each}   
  </div>

  <div class="col-8 float-left p-4 mt-n4">
    <form on:submit={sendData}>
      <input style="display:none;" id="id" bind:value={formOrador.id} />
      <input class="form-control" type="text" placeholder="Nombres" aria-label="Nombres" style="width: 49%;" bind:value={formOrador.nombre} />
      <input class="form-control" type="text" placeholder="Apellidos" aria-label="Apellidos" style="width:49%;" bind:value={formOrador.apellidos} />
      
      <div class="form-checkbox mt-2">
        <label>
          <input type="checkbox" bind:checked={formOrador.aprobado} />
          <em class="highlight">Aprobado para salir</em>
        </label>
      </div>
      
      <input class="form-control width-full mt-2" type="email" placeholder="Correo electrónico" aria-label="Correo electrónico" bind:value={formOrador.correoElectronico} />
      <input class="form-control width-full mt-2" type="number" placeholder="Celular" aria-label="Celular" bind:value={formOrador.celular} />
      <input class="form-control width-full mt-2" type="number" placeholder="Teléfono" aria-label="Teléfono" bind:value={formOrador.telefono} />
      
      <div class="radio-group mt-2">
        <input class="radio-input" id="option-anciano" type="radio" name="nombramientos" value="Anciano" bind:group={formOrador.nombramiento} />
        <label class="radio-label" for="option-anciano">Anciano</label>
        
        <input class="radio-input" id="option-siervom" type="radio" name="nombramientos" value="Siervo ministerial" bind:group={formOrador.nombramiento} />
        <label class="radio-label" for="option-siervom">Siervo ministerial</label>
      </div>  
        <p class="f5 mb-n3 mt-3">Bosquejos preparados</p>
        <div class="container-lg clearfix mt-3">
           <div class="col-2 float-left p-0">
              <div class="form-checkbox mt-0 mb-0">
                 <label>
                 <input type="checkbox" bind:checked={formOrador.discurso1} />
                 <em class="">1</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" bind:checked={formOrador.discurso7} />
                 <em class="">7</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" bind:checked={formOrador.discurso13}/>
                 <em class="">13</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" bind:checked={formOrador.discurso19} />
                 <em class="">19</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" bind:checked={formOrador.discurso25} />
                 <em class="">25</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" bind:checked={formOrador.discurso31} />
                 <em class="">31</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" bind:checked={formOrador.discurso37} />
                 <em class="">37</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" bind:checked={formOrador.discurso43} />
                 <em class="">43</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" bind:checked={formOrador.discurso49} />
                 <em class="">49</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" bind:checked={formOrador.discurso55} />
                 <em class="">55</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" bind:checked={formOrador.discurso61} />
                 <em class="">61</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" bind:checked={formOrador.discurso67} />
                 <em class="">67</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" bind:checked={formOrador.discurso73} />
                 <em class="">73</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" bind:checked={formOrador.discurso79} />
                 <em class="">79</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" bind:checked={formOrador.discurso85} />
                 <em class="">85</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" bind:checked={formOrador.discurso91} />
                 <em class="">91</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" bind:checked={formOrador.discurso103} />
                 <em class="">103</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" bind:checked={formOrador.discurso109} />
                 <em class="">109</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" bind:checked={formOrador.discurso115} />
                 <em class="">115</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" bind:checked={formOrador.discurso121} />
                 <em class="">121</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" bind:checked={formOrador.discurso127} />
                 <em class="">127</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" bind:checked={formOrador.discurso133} />
                 <em class="">133</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" bind:checked={formOrador.discurso139} />
                 <em class="">139</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" bind:checked={formOrador.discurso145} />
                 <em class="">145</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" bind:checked={formOrador.discurso151} />
                 <em class="">151</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" bind:checked={formOrador.discurso157} />
                 <em class="">157</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" bind:checked={formOrador.discurso163} />
                 <em class="">163</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" bind:checked={formOrador.discurso169} />
                 <em class="">169</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" bind:checked={formOrador.discurso175} />
                 <em class="">175</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" bind:checked={formOrador.discurso181} />
                 <em class="">181</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" bind:checked={formOrador.discurso187} />
                 <em class="">187</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" bind:checked={formOrador.discurso193} />
                 <em class="">193</em>
                 </label>
              </div>
           </div>
           <div class="col-2 float-left p-0">
            <div class="form-checkbox mt-0 mb-0">
              <label>
                <input type="checkbox" bind:checked={formOrador.discurso2} />
                <em class="">2</em>
              </label>
              <br>
              <label>
                <input type="checkbox" bind:checked={formOrador.discurso8} />
                <em class="">8</em>
              </label>
              <br>
              <label>
                <input type="checkbox" bind:checked={formOrador.discurso14} />
                <em class="">14</em>
              </label>
              <br>
              <label>
                <input type="checkbox" bind:checked={formOrador.discurso20} />
                <em class="">20</em>
              </label>
              <br>
              <label>
                <input type="checkbox" bind:checked={formOrador.discurso26} />
                <em class="">26</em>
              </label>
              <br>
              <label>
                <input type="checkbox" bind:checked={formOrador.discurso32} />
                <em class="">32</em>
              </label>
              <br>
              <label>
                <input type="checkbox" bind:checked={formOrador.discurso38} />
                <em class="">38</em>
              </label>
              <br>
              <label>
                <input type="checkbox" bind:checked={formOrador.discurso44} />
                <em class="">44</em>
              </label>
              <br>
              <label>
                <input type="checkbox" bind:checked={formOrador.discurso50} />
                <em class="">50</em>
              </label>
              <br>
              <label>
                <input type="checkbox" bind:checked={formOrador.discurso56} />
                <em class="">56</em>
              </label>
              <br>
              <label>
                <input type="checkbox" bind:checked={formOrador.discurso62} />
                <em class="">62</em>
              </label>
              <br>
              <label>
                <input type="checkbox" bind:checked={formOrador.discurso68} />
                <em class="">68</em>
              </label>
              <br>
              <label>
                <input type="checkbox" bind:checked={formOrador.discurso74} />
                <em class="">74</em>
              </label>
              <br>
              <label>
                <input type="checkbox" bind:checked={formOrador.discurso80} />
                <em class="">80</em>
              </label>
              <br>
              <label>
                <input type="checkbox" bind:checked={formOrador.discurso86} />
                <em class="">86</em>
              </label>
              <br>
              <label>
                <input type="checkbox" bind:checked={formOrador.discurso92} />
                <em class="">92</em>
              </label>
              <br>
              <label>
                <input type="checkbox" bind:checked={formOrador.discurso104} />
                <em class="">104</em>
              </label>
              <br>
              <label>
                <input type="checkbox" bind:checked={formOrador.discurso110} />
                <em class="">110</em>
              </label>
              <br>
              <label>
                <input type="checkbox" bind:checked={formOrador.discurso116} />
                <em class="">116</em>
              </label>
              <br>
              <label>
                <input type="checkbox" bind:checked={formOrador.discurso122} />
                <em class="">122</em>
              </label>
                 <br>
                 <label>
                 <input type="checkbox" bind:checked={formOrador.discurso128} />
                 <em class="">128</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" bind:checked={formOrador.discurso134} />
                 <em class="">134</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" bind:checked={formOrador.discurso140} />
                 <em class="">140</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" bind:checked={formOrador.discurso146} />
                 <em class="">146</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" bind:checked={formOrador.discurso152} />
                 <em class="">152</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" bind:checked={formOrador.discurso158} />
                 <em class="">158</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" bind:checked={formOrador.discurso164} />
                 <em class="">164</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" bind:checked={formOrador.discurso170} />
                 <em class="">170</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" bind:checked={formOrador.discurso176} />
                 <em class="">176</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" bind:checked={formOrador.discurso182} />
                 <em class="">182</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" bind:checked={formOrador.discurso188} />
                 <em class="">188</em>
                 </label>
                 <br>
                 <label>
                 <input type="checkbox" bind:checked={formOrador.discurso194} />
                 <em class="">194</em>
                 </label>
              </div>
           </div>
           <div class="col-2 float-left p-0">
            <div class="form-checkbox mt-0 mb-0">
              <label>
                <input type="checkbox" bind:checked={formOrador.discurso3} />
                <em class="">3</em>
              </label>
              <br>
              <label>
                <input type="checkbox" bind:checked={formOrador.discurso9} />
                <em class="">9</em>
              </label>
              <br>
              <label>
                <input type="checkbox" bind:checked={formOrador.discurso15} />
                <em class="">15</em>
              </label>
              <br>
              <label>
                <input type="checkbox" bind:checked={formOrador.discurso21} />
                <em class="">21</em>
              </label>
              <br>
              <label>
                <input type="checkbox" bind:checked={formOrador.discurso27} />
                <em class="">27</em>
              </label>
              <br>
              <label>
                <input type="checkbox" bind:checked={formOrador.discurso33} />
                <em class="">33</em>
              </label>
              <br>
              <label>
                <input type="checkbox" bind:checked={formOrador.discurso39} />
                <em class="">39</em>
              </label>
              <br>
              <label>
                <input type="checkbox" bind:checked={formOrador.discurso45} />
                <em class="">45</em>
              </label>
              <br>
              <label>
                <input type="checkbox" bind:checked={formOrador.discurso51} />
                <em class="">51</em>
              </label>
              <br>
              <label>
                <input type="checkbox" bind:checked={formOrador.discurso57} />
                <em class="">57</em>
              </label>
              <br>
                  <label>
                    <input type="checkbox" bind:checked={formOrador.discurso63} />
                    <em class="">63</em>
                  </label>
                  <br>
                  <label>
                    <input type="checkbox" bind:checked={formOrador.discurso69} />
                    <em class="">69</em>
                  </label>
                  <br>
                  <label>
                    <input type="checkbox" bind:checked={formOrador.discurso75} />
                    <em class="">75</em>
                  </label>
                  <br>
                  <label>
                    <input type="checkbox" bind:checked={formOrador.discurso81} />
                    <em class="">81</em>
                  </label>
                  <br>
                  <label>
                    <input type="checkbox" bind:checked={formOrador.discurso87} />
                    <em class="">87</em>
                  </label>
                  <br>
                  <label>
                    <input type="checkbox" bind:checked={formOrador.discurso93} />
                    <em class="">93</em>
                  </label>
                  <br>
                  <label>
                    <input type="checkbox" bind:checked={formOrador.discurso105} />
                    <em class="">105</em>
                  </label>
                  <br>
                  <label>
                    <input type="checkbox" bind:checked={formOrador.discurso111} />
                    <em class="">111</em>
                  </label>
                  <br>
                  <label>
                    <input type="checkbox" bind:checked={formOrador.discurso117} />
                    <em class="">117</em>
                  </label>
                  <br>
                  <label>
                    <input type="checkbox" bind:checked={formOrador.discurso123} />
                    <em class="">123</em>
                  </label>
                  <br>
                      <label>
                        <input type="checkbox" bind:checked={formOrador.discurso129} />
                        <em class="">129</em>
                      </label>
                      <br>
                      <label>
                        <input type="checkbox" bind:checked={formOrador.discurso135} />
                        <em class="">135</em>
                      </label>
                      <br>
                      <label>
                        <input type="checkbox" bind:checked={formOrador.discurso141} />
                        <em class="">141</em>
                      </label>
                      <br>
                      <label>
                        <input type="checkbox" bind:checked={formOrador.discurso147} />
                        <em class="">147</em>
                      </label>
                      <br>
                      <label>
                        <input type="checkbox" bind:checked={formOrador.discurso153} />
                        <em class="">153</em>
                      </label>
                      <br>
                      <label>
                        <input type="checkbox" bind:checked={formOrador.discurso159} />
                        <em class="">159</em>
                      </label>
                      <br>
                      <label>
                        <input type="checkbox" bind:checked={formOrador.discurso165} />
                        <em class="">165</em>
                      </label>
                      <br>
                      <label>
                        <input type="checkbox" bind:checked={formOrador.discurso171} />
                        <em class="">171</em>
                      </label>
                      <br>
                      <label>
                        <input type="checkbox" bind:checked={formOrador.discurso177} />
                        <em class="">177</em>
                      </label>
                      <br>
                      <label>
                        <input type="checkbox" bind:checked={formOrador.discurso183} />
                        <em class="">183</em>
                      </label>
                      <br>
                      <label>
                        <input type="checkbox" bind:checked={formOrador.discurso189} />
                        <em class="">189</em>
                      </label>
                      <br>
                    </div>
                  </div>                   
           <div class="col-2 float-left p-0">
              <div class="form-checkbox mt-0 mb-0">
                <label>
                  <input type="checkbox" bind:checked={formOrador.discurso4} />
                  <em class="">4</em>
                </label>
                <br>
                <label>
                  <input type="checkbox" bind:checked={formOrador.discurso10} />
                  <em class="">10</em>
                </label>
                <br>
                <label>
                  <input type="checkbox" bind:checked={formOrador.discurso16} />
                  <em class="">16</em>
                </label>
                <br>
                <label>
                  <input type="checkbox" bind:checked={formOrador.discurso22} />
                  <em class="">22</em>
                </label>
                <br>
                <label>
                  <input type="checkbox" bind:checked={formOrador.discurso28} />
                  <em class="">28</em>
                </label>
                <br>
                <label>
                  <input type="checkbox" bind:checked={formOrador.discurso34} />
                  <em class="">34</em>
                </label>
                <br>
                <label>
                  <input type="checkbox" bind:checked={formOrador.discurso40} />
                  <em class="">40</em>
                </label>
                <br>
                <label>
                  <input type="checkbox" bind:checked={formOrador.discurso46} />
                  <em class="">46</em>
                </label>
                <br>
                <label>
                  <input type="checkbox" bind:checked={formOrador.discurso52} />
                  <em class="">52</em>
                </label>
                <br>
                <label>
                  <input type="checkbox" bind:checked={formOrador.discurso58} />
                  <em class="">58</em>
                </label>
                <br>
                <label>
                  <input type="checkbox" bind:checked={formOrador.discurso64} />
                  <em class="">64</em>
                </label>
                <br>
                <label>
                  <input type="checkbox" bind:checked={formOrador.discurso70} />
                  <em class="">70</em>
                </label>
                <br>
                <label>
                  <input type="checkbox" bind:checked={formOrador.discurso76} />
                  <em class="">76</em>
                </label>
                <br>
                <label>
                  <input type="checkbox" bind:checked={formOrador.discurso82} />
                  <em class="">82</em>
                </label>
                <br>
                <label>
                  <input type="checkbox" bind:checked={formOrador.discurso88} />
                  <em class="">88</em>
                </label>
                <br>
                <label>
                  <input type="checkbox" bind:checked={formOrador.discurso94} />
                  <em class="">94</em>
                </label>
                <br>
                <label>
                  <input type="checkbox" bind:checked={formOrador.discurso106} />
                  <em class="">106</em>
                </label>
                <br>
                <label>
                  <input type="checkbox" bind:checked={formOrador.discurso112} />
                  <em class="">112</em>
                </label>
                <br>
                <label>
                  <input type="checkbox" bind:checked={formOrador.discurso118} />
                  <em class="">118</em>
                </label>
                <br>
                <label>
                  <input type="checkbox" bind:checked={formOrador.discurso124} />
                  <em class="">124</em>
                </label>
                <br>
                <label>
                  <input type="checkbox" bind:checked={formOrador.discurso130} />
                  <em class="">130</em>
                </label>
                <br>
                <label>
                  <input type="checkbox" bind:checked={formOrador.discurso136} />
                  <em class="">136</em>
                </label>
                <br>
                <label>
                  <input type="checkbox" bind:checked={formOrador.discurso142} />
                  <em class="">142</em>
                </label>
                <br>
                <label>
                  <input type="checkbox" bind:checked={formOrador.discurso148} />
                  <em class="">148</em>
                </label>
                <br>
                <label>
                  <input type="checkbox" bind:checked={formOrador.discurso154} />
                  <em class="">154</em>
                </label>
                <br>
                <label>
                  <input type="checkbox" bind:checked={formOrador.discurso160} />
                  <em class="">160</em>
                </label>
                <br>
                <label>
                  <input type="checkbox" bind:checked={formOrador.discurso166} />
                  <em class="">166</em>
                </label>
                <br>
                <label>
                  <input type="checkbox" bind:checked={formOrador.discurso172} />
                  <em class="">172</em>
                </label>
                <br>
                <label>
                  <input type="checkbox" bind:checked={formOrador.discurso178} />
                  <em class="">178</em>
                </label>
                <br>
                <label>
                  <input type="checkbox" bind:checked={formOrador.discurso184} />
                  <em class="">184</em>
                </label>
                <br>
                <label>
                  <input type="checkbox" bind:checked={formOrador.discurso190} />
                  <em class="">190</em>
                </label>
                <br>                                                
              </div>
           </div>
           <div class="col-2 float-left p-0">
              <div class="form-checkbox mt-0 mb-0">
                <label>
                  <input type="checkbox" bind:checked={formOrador.discurso5} />
                  <em class="">5</em>
                </label>
                <br>
                <label>
                  <input type="checkbox" bind:checked={formOrador.discurso11} />
                  <em class="">11</em>
                </label>
                <br>
                <label>
                  <input type="checkbox" bind:checked={formOrador.discurso17} />
                  <em class="">17</em>
                </label>
                <br>
                <label>
                  <input type="checkbox" bind:checked={formOrador.discurso23} />
                  <em class="">23</em>
                </label>
                <br>
                <label>
                  <input type="checkbox" bind:checked={formOrador.discurso29} />
                  <em class="">29</em>
                </label>
                <br>
                <label>
                  <input type="checkbox" bind:checked={formOrador.discurso35} />
                  <em class="">35</em>
                </label>
                <br>
                <label>
                  <input type="checkbox" bind:checked={formOrador.discurso41} />
                  <em class="">41</em>
                </label>
                <br>
                <label>
                  <input type="checkbox" bind:checked={formOrador.discurso47} />
                  <em class="">47</em>
                </label>
                <br>
                <label>
                  <input type="checkbox" bind:checked={formOrador.discurso53} />
                  <em class="">53</em>
                </label>
                <br>
                <label>
                  <input type="checkbox" bind:checked={formOrador.discurso59} />
                  <em class="">59</em>
                </label>
                <br>
                <label>
                  <input type="checkbox" bind:checked={formOrador.discurso65} />
                  <em class="">65</em>
                </label>
                <br>
                <label>
                  <input type="checkbox" bind:checked={formOrador.discurso71} />
                  <em class="">71</em>
                </label>
                <br>
                <label>
                  <input type="checkbox" bind:checked={formOrador.discurso77} />
                  <em class="">77</em>
                </label>
                <br>
                <label>
                  <input type="checkbox" bind:checked={formOrador.discurso83} />
                  <em class="">83</em>
                </label>
                <br>
                <label>
                  <input type="checkbox" bind:checked={formOrador.discurso89} />
                  <em class="">89</em>
                </label>
                <br>
                <label>
                  <input type="checkbox" bind:checked={formOrador.discurso95} />
                  <em class="">95</em>
                </label>
                <br>
                <label>
                  <input type="checkbox" bind:checked={formOrador.discurso107} />
                  <em class="">107</em>
                </label>
                <br>
                <label>
                  <input type="checkbox" bind:checked={formOrador.discurso113} />
                  <em class="">113</em>
                </label>
                <br>
                <label>
                  <input type="checkbox" bind:checked={formOrador.discurso119} />
                  <em class="">119</em>
                </label>
                <br>
                <label>
                  <input type="checkbox" bind:checked={formOrador.discurso125} />
                  <em class="">125</em>
                </label>
                <br>
                <label>
                  <input type="checkbox" bind:checked={formOrador.discurso131} />
                  <em class="">131</em>
                </label>
                <br>
                <label>
                  <input type="checkbox" bind:checked={formOrador.discurso137} />
                  <em class="">137</em>
                </label>
                <br>
                <label>
                  <input type="checkbox" bind:checked={formOrador.discurso143} />
                  <em class="">143</em>
                </label>
                <br>
                <label>
                  <input type="checkbox" bind:checked={formOrador.discurso149} />
                  <em class="">149</em>
                </label>
                <br>
                <label>
                  <input type="checkbox" bind:checked={formOrador.discurso155} />
                  <em class="">155</em>
                </label>
                <br>
                <label>
                  <input type="checkbox" bind:checked={formOrador.discurso161} />
                  <em class="">161</em>
                </label>
                <br>
                <label>
                  <input type="checkbox" bind:checked={formOrador.discurso167} />
                  <em class="">167</em>
                </label>
                <br>
                <label>
                  <input type="checkbox" bind:checked={formOrador.discurso173} />
                  <em class="">173</em>
                </label>
                <br>
                <label>
                  <input type="checkbox" bind:checked={formOrador.discurso179} />
                  <em class="">179</em>
                </label>
                <br>
                <label>
                  <input type="checkbox" bind:checked={formOrador.discurso185} />
                  <em class="">185</em>
                </label>
                <br>
                <label>
                  <input type="checkbox" bind:checked={formOrador.discurso191} />
                  <em class="">191</em>
                </label>
                <br>                                                
              </div>
           </div>
           <div class="col-2 float-left p-0">
              <div class="form-checkbox mt-0 mb-0">
                <label>
                  <input type="checkbox" bind:checked={formOrador.discurso6} />
                  <em class="">6</em>
                </label>
                <br>
                <label>
                  <input type="checkbox" bind:checked={formOrador.discurso12} />
                  <em class="">12</em>
                </label>
                <br>
                <label>
                  <input type="checkbox" bind:checked={formOrador.discurso18} />
                  <em class="">18</em>
                </label>
                <br>
                <label>
                  <input type="checkbox" bind:checked={formOrador.discurso24} />
                  <em class="">24</em>
                </label>
                <br>
                <label>
                  <input type="checkbox" bind:checked={formOrador.discurso30} />
                  <em class="">30</em>
                </label>
                <br>
                <label>
                  <input type="checkbox" bind:checked={formOrador.discurso36} />
                  <em class="">36</em>
                </label>
                <br>
                <label>
                  <input type="checkbox" bind:checked={formOrador.discurso42} />
                  <em class="">42</em>
                </label>
                <br>
                <label>
                  <input type="checkbox" bind:checked={formOrador.discurso48} />
                  <em class="">48</em>
                </label>
                <br>
                <label>
                  <input type="checkbox" bind:checked={formOrador.discurso54} />
                  <em class="">54</em>
                </label>
                <br>
                <label>
                  <input type="checkbox" bind:checked={formOrador.discurso60} />
                  <em class="">60</em>
                </label>
                <br>
                <label>
                  <input type="checkbox" bind:checked={formOrador.discurso66} />
                  <em class="">66</em>
                </label>
                <br>
                <label>
                  <input type="checkbox" bind:checked={formOrador.discurso72} />
                  <em class="">72</em>
                </label>
                <br>
                <label>
                  <input type="checkbox" bind:checked={formOrador.discurso78} />
                  <em class="">78</em>
                </label>
                <br>
                <label>
                  <input type="checkbox" bind:checked={formOrador.discurso84} />
                  <em class="">84</em>
                </label>
                <br>
                <label>
                  <input type="checkbox" bind:checked={formOrador.discurso90} />
                  <em class="">90</em>
                </label>
                <br>
                <label>
                  <input type="checkbox" bind:checked={formOrador.discurso96} />
                  <em class="">96</em>
                </label>
                <br>
                <label>
                  <input type="checkbox" bind:checked={formOrador.discurso108} />
                  <em class="">108</em>
                </label>
                <br>
                <label>
                  <input type="checkbox" bind:checked={formOrador.discurso114} />
                  <em class="">114</em>
                </label>
                <br>
                <label>
                  <input type="checkbox" bind:checked={formOrador.discurso120} />
                  <em class="">120</em>
                </label>
                <br>
                <label>
                  <input type="checkbox" bind:checked={formOrador.discurso126} />
                  <em class="">126</em>
                </label>
                <br>
<label>
  <input type="checkbox" bind:checked={formOrador.discurso132} />
  <em class="">132</em>
</label>
<br>
<label>
  <input type="checkbox" bind:checked={formOrador.discurso138} />
  <em class="">138</em>
</label>
<br>
<label>
  <input type="checkbox" bind:checked={formOrador.discurso144} />
  <em class="">144</em>
</label>
<br>
<label>
  <input type="checkbox" bind:checked={formOrador.discurso150} />
  <em class="">150</em>
</label>
<br>
<label>
  <input type="checkbox" bind:checked={formOrador.discurso156} />
  <em class="">156</em>
</label>
<br>
<label>
  <input type="checkbox" bind:checked={formOrador.discurso162} />
  <em class="">162</em>
</label>
<br>
<label>
  <input type="checkbox" bind:checked={formOrador.discurso168} />
  <em class="">168</em>
</label>
<br>
<label>
  <input type="checkbox" bind:checked={formOrador.discurso174} />
  <em class="">174</em>
</label>
<br>
<label>
  <input type="checkbox" bind:checked={formOrador.discurso180} />
  <em class="">180</em>
</label>
<br>
<label>
  <input type="checkbox" bind:checked={formOrador.discurso186} />
  <em class="">186</em>
</label>
<br>
<label>
  <input type="checkbox" bind:checked={formOrador.discurso192} />
  <em class="">192</em>
</label>                                
              </div>
           </div>
        </div>
        <br><br>
        <div class="form-actions">
           <button type="submit" class="btn btn-primary">Guardar</button>  
           <button type="button" class="btn btn-danger" on:click={handleEliminarOrador}>
            <svg class="octicon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" width="16" height="16">
              <path fill-rule="evenodd" d="M6.5 1.75a.25.25 0 01.25-.25h2.5a.25.25 0 01.25.25V3h-3V1.75zm4.5 0V3h2.25a.75.75 0 010 1.5H2.75a.75.75 0 010-1.5H5V1.75C5 .784 5.784 0 6.75 0h2.5C10.216 0 11 .784 11 1.75zM4.496 6.675a.75.75 0 10-1.492.15l.66 6.6A1.75 1.75 0 005.405 15h5.19c.9 0 1.652-.681 1.741-1.576l.66-6.6a.75.75 0 00-1.492-.149l-.66 6.6a.25.25 0 01-.249.225h-5.19a.25.25 0 01-.249-.225l-.66-6.6z"></path>
            </svg>
            <span>Eliminar</span>
          </button>                   
        </div>
     </form>
  </div>
</div>