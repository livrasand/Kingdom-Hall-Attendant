<script>
    export let id;
    export let id_cl = "form-control";
    export let label;
    export let label_cl
    export let placeholder;
    export let value;
    export let style;
</script>

{#if label_cl}
<label class={label_cl} for={id}>{label}</label>
{/if}
<input id={id} name={name} class={id_cl} type="text" placeholder={placeholder} aria-label={label} style={style} bind:value />