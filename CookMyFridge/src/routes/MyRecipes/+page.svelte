<script lang="ts">
    import {goto} from "$app/navigation";

    let search = '';

    interface Recipe {
        id: number;
        description: string;
        ingredients: string[];
        instructions: string;
        name: string;
        image64: string;
    }

    export let data;

    let recipes: Recipe[] = data.recipes.recipes;

    let filteredRecipes: Recipe[] = [];

    $: if (recipes) {
        filteredRecipes = recipes.filter(recipe =>
            recipe.name.toLowerCase().includes(search.toLowerCase())
        );
    }

    function viewDetails(recipeId: number) {
        goto(`/MyRecipes/recipe/${recipeId}`);
    }
</script>

<div class="flex flex-col justify-center items-center px-6 py-8">
    <div class="bg-secondary-600 w-2/3 py-2 px-5 rounded-xl sticky top-0 flex items-center justify-between">
        <h1 class="text-white text-3xl">My Recipes</h1>
        <input type="search" bind:value={search} class="rounded-xl text-black"
               placeholder="Search for a recipe..."/>
    </div>
    {#each filteredRecipes as recipe}
        <div class="bg-secondary-400 w-2/3 py-2 rounded-xl mt-4 ps-5 flex justify-between">
            <img src={"data:image/jpg;base64," + recipe.image64} alt={recipe.name} class="recipe-image"/>
            <div class="recipe-content ps-2 w-5/6">
                <h2 class="text-white text-2xl">{ recipe.name }</h2>
                <p class="text-white text-lg">
                    { recipe.description }
                </p>
                <p class="text-white text-lg">Needed
                    Ingredients: { !recipe.ingredients.length ? 'None' : recipe.ingredients.join(', ') }
                </p>
            </div>
            <button on:click={() => viewDetails(recipe.id)}
                    class="bg-primary-500 w-1/6 text-white rounded-xl px-2 me-5">
                View Details
            </button>
        </div>
    {/each}
</div>

<style>
    .recipe-image {
        width: 100px;
        height: 100px;
        object-fit: cover;
        border-radius: 50%;
    }

    .recipe-content {
        flex-grow: 1;
    }
</style>