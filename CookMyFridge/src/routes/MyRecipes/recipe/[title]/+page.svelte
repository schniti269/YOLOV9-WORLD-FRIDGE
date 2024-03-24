<script lang="ts">
    export let data;
</script>

<h1 class="text-5xl">Rezept</h1>
<h2>{data.recipe.title}</h2>
<p>{data.recipe.description}</p>
{#each data.recipe.ingredients as ingredient}
    <p>{ingredient.amount} {ingredient.unit} {ingredient.name}</p>
{/each}
{#each data.recipe.steps as step}
    <p>{step.description}</p>
{/each}