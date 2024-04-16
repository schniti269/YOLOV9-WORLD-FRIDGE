<script lang="ts">
    // Importing the goto function from SvelteKit's navigation module
    import {goto} from "$app/navigation";

    // Variable to hold the search string
    let search = '';

    // Interface for the Recipe type
    interface Recipe {
        id: number;
        description: string;
        ingredients: string[];
        instructions: string;
        name: string;
        image64: string;
    }

    // Exported variable to hold the data passed to the component
    export let data;

    // Variable to hold the list of recipes
    let recipes: Recipe[] = data.recipes.recipes;

    // Variable to hold the list of recipes that match the search string
    let filteredRecipes: Recipe[] = [];

    // Reactive statement to filter the recipes based on the search string
    $: if (recipes) {
        filteredRecipes = recipes.filter(recipe =>
            recipe.name.toLowerCase().includes(search.toLowerCase())
        );
    }

    /**
     * Function to navigate to the details page of a recipe
     * @param {number} recipeId - The ID of the recipe
     */
    function viewDetails(recipeId: number) {
        goto(`/MyRecipes/recipe/${recipeId}`);
    }
</script>

<!-- Main container for the page -->
<div class="flex flex-col justify-center items-center px-6 py-8">
    <!-- Header with title and search input -->
    <div class="bg-secondary-600 w-2/3 py-2 px-5 rounded-xl sticky top-0 flex items-center justify-between">
        <h1 class="text-white text-3xl">My Recipes</h1>
        <input type="search" bind:value={search} class="rounded-xl text-black"
               placeholder="Search for a recipe..."/>
    </div>
    <!-- List of recipes -->
    {#each filteredRecipes as recipe}
        <div class="bg-secondary-400 w-2/3 py-2 rounded-xl mt-4 ps-5 flex justify-between">
            <!-- Recipe image -->
            <img src={"data:image/jpg;base64," + recipe.image64} alt={recipe.name} class="recipe-image"/>
            <!-- Recipe content -->
            <div class="recipe-content ps-2 w-5/6">
                <h2 class="text-white text-2xl">{ recipe.name }</h2>
                <p class="text-white text-lg">
                    { recipe.description }
                </p>
                <p class="text-white text-lg">Needed
                    Ingredients: { !recipe.ingredients.length ? 'None' : recipe.ingredients.join(', ') }
                </p>
            </div>
            <!-- View details button -->
            <button on:click={() => viewDetails(recipe.id)}
                    class="bg-primary-500 w-1/6 text-white rounded-xl px-2 me-5">
                View Details
            </button>
        </div>
    {/each}
</div>

<!-- Styles for the recipe image and content -->
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