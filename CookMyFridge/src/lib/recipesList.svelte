<script lang="ts">
    import {goto} from "$app/navigation";

    export let recipes;

    function viewDetails(recipeId: any) {
        goto(`/MyRecipes/recipe/${recipeId}`);
    }
</script>

<div class="flex flex-col justify-center items-center px-6 py-8">
    <h1 class="text-white text-4xl mb-4">Recipes</h1>
    {#each recipes as recipe}
        <div class="bg-secondary-400 w-2/3 py-2 rounded-xl mt-4 ps-5 flex justify-between">
            <div>
                <h2 class="text-white text-2xl">{ recipe.title }</h2>
                <p class="text-white text-lg">
                    { recipe.time } { recipe.time === 1 ? 'min' : 'mins' } | { recipe.nutritionType }
                </p>
                <p class="text-white text-lg">Needed
                    Additions: { !recipe.additions.length ? 'None' : recipe.additions.join(', ') }
                </p>
            </div>
            <button on:click={() => viewDetails(recipe.id)}
                    class="bg-primary-500 text-white rounded-xl px-2 me-5">
                View Details
            </button>
        </div>
    {/each}
</div>