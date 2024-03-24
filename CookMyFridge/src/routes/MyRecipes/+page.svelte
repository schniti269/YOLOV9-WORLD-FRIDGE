<script lang="ts">
    import {goto} from "$app/navigation";

    let search = '';

    let recipes = [
        {
            title: 'Pancakes',
            time: 30,
            nutritionType: 'Vegetarian',
            additions: [],
        },
        {
            title: 'Pasta',
            time: 60,
            nutritionType: 'Vegetarian',
            additions: [],
        },
        {
            title: 'Salad',
            time: 15,
            nutritionType: 'Vegan',
            additions: ['dressing', 'croutons'],
        },
        {
            title: 'Burger',
            time: 30,
            nutritionType: 'Omnivore',
            additions: ['ketchup'],
        },
        {
            title: 'Pizza',
            time: 60,
            nutritionType: 'Vegetarian',
            additions: ['cheese', 'sauce'],
        },
        {
            title: 'Tacos',
            time: 45,
            nutritionType: 'Omnivore',
            additions: ['salsa', 'guacamole'],
        },
        {
            title: 'Sushi',
            time: 90,
            nutritionType: 'Pescatarian',
            additions: ['soy sauce', 'wasabi'],
        }
    ];

    $: filteredRecipes = recipes.filter(recipe =>
        recipe.title.toLowerCase().includes(search.toLowerCase())
    );

    function viewDetails(recipeTitle: any) {
        goto(`/MyRecipes/recipe/${recipeTitle}`);
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
            <div>
                <h2 class="text-white text-2xl">{ recipe.title }</h2>
                <p class="text-white text-lg">
                    { recipe.time } { recipe.time === 1 ? 'min' : 'mins' } | { recipe.nutritionType }
                </p>
                <p class="text-white text-lg">Needed
                    Additions: { !recipe.additions.length ? 'None' : recipe.additions.join(', ') }
                </p>
            </div>
            <button on:click={() => viewDetails(recipe.title)}
                    class="bg-primary-500 text-white rounded-xl px-2 me-5">
                View Details
            </button>
        </div>
    {/each}
</div>