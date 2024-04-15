<script lang="ts">
    import {goto} from "$app/navigation";

    export let recipes;

    function viewDetails(recipeId: any) {
        goto(`/MyRecipes/recipe/${recipeId}`);
    }
</script>

{#each recipes as recipe}
    <div class="recipe-card bg-secondary-400 w-full py-2 rounded-xl mt-4 ps-5 flex justify-between">
        <img src={"data:image/jpg;base64," + recipe.image} alt={recipe.name} class="recipe-image"/>
        <div class="recipe-content">
            <h3 class="text-white text-xl font-bold">{ recipe.name }</h3>
            <p class="text-white">
                { recipe.description }
            </p>
            <p class="text-white">Needed
                Ingredients: { !recipe.ingredients.length ? 'None' : recipe.ingredients.join(', ') }
            </p>
        </div>
        <button on:click={() => viewDetails(recipe.id)}
                class="bg-primary-500 text-white rounded-xl px-2 me-2">
            View Details
        </button>
    </div>
{/each}

<style>
    .recipe-card {
        display: flex;
        align-items: center;
        gap: 20px;
    }

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