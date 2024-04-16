<script lang="ts">
    // Importing the goto function from SvelteKit's navigation module
    import {goto} from "$app/navigation";

    // Exported variable to hold the data passed to the component
    export let recipes;

    /**
     * Function to navigate to the details page of a recipe
     * @param {any} recipeId - The ID of the recipe
     */
    function viewDetails(recipeId: any) {
        goto(`/MyRecipes/recipe/${recipeId}`);
    }
</script>

<!-- Loop over each recipe and display its details -->
{#each recipes as recipe}
    <!-- Container for each recipe -->
    <div class="recipe-card bg-secondary-400 w-full py-2 rounded-xl mt-4 ps-5 flex justify-between">
        <!-- Recipe image with base64 encoded image data -->
        <img src={"data:image/jpg;base64," + recipe.image} alt={recipe.name} class="recipe-image"/>
        <!-- Recipe content -->
        <div class="recipe-content">
            <!-- Recipe name -->
            <h3 class="text-white text-xl font-bold">{ recipe.name }</h3>
            <!-- Recipe description -->
            <p class="text-white">
                { recipe.description }
            </p>
            <!-- Recipe ingredients -->
            <p class="text-white">Needed
                Ingredients: { !recipe.ingredients.length ? 'None' : recipe.ingredients.join(', ') }
            </p>
        </div>
        <!-- Button to view the details of the recipe -->
        <button on:click={() => viewDetails(recipe.id)}
                class="bg-primary-500 text-white rounded-xl px-2 me-2">
            View Details
        </button>
    </div>
{/each}

<style>
    /* Styles for the recipe card */
    .recipe-card {
        display: flex;
        align-items: center;
        gap: 20px;
    }

    /* Styles for the recipe image */
    .recipe-image {
        width: 100px;
        height: 100px;
        object-fit: cover;
        border-radius: 50%;
    }

    /* Styles for the recipe content */
    .recipe-content {
        flex-grow: 1;
    }
</style>