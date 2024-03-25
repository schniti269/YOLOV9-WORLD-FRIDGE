<script lang="ts">
    import {Card} from "flowbite-svelte";
    import {goto} from "$app/navigation";
    import {ArrowLeftSolid, HeartOutline} from "flowbite-svelte-icons";

    export let data;
</script>

<div class="flex justify-center pt-10">
    <Card size="xl" class="bg-secondary-400 text-white rounded-2xl">

        <!-- Card Header -->
        <div class="flex justify-between bg-secondary-600 px-5 py-4 rounded-xl -m-8">
            <button on:click={() => (goto("/MyRecipes"))}>
                <ArrowLeftSolid class="w-10 h-10 rounded-3xl border-2"/>
            </button>
            <h1 class="text-4xl">Recipe: {data.recipe.title}</h1>
            <button>
                <HeartOutline class="w-10 h-10 rounded-3xl border-2 bg-red-600 p-1" color="white"/>
            </button>
        </div>

        <!-- Card Body -->
        <div class="mt-14">

            <!-- Displaying the title and description of the recipe on top -->
            <div>
                <h2>{data.recipe.title}: {data.recipe.description}</h2>
            </div>

            <!-- Image and Ingredients displayed next to each other -->
            <div class="flex space-x-2 py-4">

                <!-- Displaying the image of the recipe -->
                <div class="pr-6">
                    <img src="{data.recipe.image}" alt="{data.recipe.title}" class="w-52 rounded-xl">
                </div>

                <!-- Displaying the ingredients of the recipe -->
                <div>
                    <h3 class="text-xl font-bold pb-1">Zutaten</h3>
                    <ul>
                        {#each data.recipe.ingredients as ingredient}
                            <li>{ingredient.amount} {ingredient.unit} {ingredient.name}</li>
                        {/each}
                    </ul>
                </div>
            </div>

            <!-- Displaying the steps of the recipe underneath the image and ingredients -->
            <div>
                <h3 class="text-xl font-bold pb-1">Zubereitung</h3>
                <ol>
                    {#each data.recipe.steps as step}
                        <li>{step.description}</li>
                    {/each}
                </ol>
            </div>
        </div>
    </Card>
</div>
