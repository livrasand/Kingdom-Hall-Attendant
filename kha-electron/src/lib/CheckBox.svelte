<script>
    export let id;
    export let id_cl = "form-control";
    export let label;
    export let placeholder;
    export let value;
    export let style;
</script>

<label>
<input id={id} name={name} class={id_cl} type="checkbox" placeholder={placeholder} aria-label={label} style={style} bind:value />
<em class="highlight">{placeholder}</em>
</label>