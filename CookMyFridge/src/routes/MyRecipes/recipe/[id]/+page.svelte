<script lang="ts">
    import {Button, Card} from "flowbite-svelte";
    import {goto} from "$app/navigation";
    import {
        ArrowLeftSolid,
        CheckCircleSolid,
        CloseSolid,
        EditSolid,
        HeartOutline,
        TrashBinSolid
    } from "flowbite-svelte-icons";
    import {recipeEditMode} from "../../../../stores";

    export let data;

    let editMode = false;
    recipeEditMode.subscribe(value => editMode = value);

    let ingredients: string[] = data.recipe.recipe.ingredients;

    function addIngredient() {
        ingredients = [...ingredients, ""];
    }
</script>

<div class="flex justify-center pt-10">
    <Card size="xl" class="bg-secondary-400 text-white rounded-2xl">

        <!-- Card Header -->
        <div class="flex justify-between bg-secondary-600 px-5 py-4 rounded-xl -m-8">
            <button on:click={() => (goto("/MyRecipes"))}>
                <ArrowLeftSolid class="w-10 h-10 rounded-3xl border-2"/>
            </button>
            <h1 class="text-4xl">Recipe: {data.recipe.recipe.name}</h1>
            <div>
                <button type="button">
                    <HeartOutline class="w-10 h-10 rounded-3xl border-2 bg-red-600 p-1" color="white"/>
                </button>

                {#if editMode}
                    <button type="button" on:click={() => (recipeEditMode.set(false))}>
                        <CloseSolid class="w-10 h-10 rounded-3xl border-2 bg-primary-600 p-1" color="white"/>
                    </button>
                {:else}
                    <button type="button" on:click={() => (recipeEditMode.set(true))}>
                        <EditSolid class="w-10 h-10 rounded-3xl border-2 bg-primary-600 p-1" color="white"/>
                    </button>
                {/if}

            </div>
        </div>

        <!-- Card Body -->
        <div class="mt-14">

            <form method="POST" action="?/updateRecipe">

                <!-- Displaying a message if the recipe was not found -->
                {#if data.recipe.status !== 200}
                    <div class="text-center">
                        <h2 class="text-2xl">{data.recipe.message}</h2>
                    </div>
                {/if}

                <!-- Displaying the title and description of the recipe on top -->
                <div>
                    {#if editMode}
                        <label for="title" class="text-xl font-bold">Title:</label>
                        <input type="text" id="name" name="name" value="{data.recipe.recipe.name}"
                               class="w-full p-2 rounded-xl text-black mb-2"/>

                        <label for="description" class="text-xl font-bold">Description:</label>
                        <input type="text" id="description" name="description" value="{data.recipe.recipe.description}"
                               class="w-full p-2 rounded-xl text-black"/>
                    {:else}
                        <h2>{data.recipe.recipe.name}: {data.recipe.recipe.description}</h2>
                    {/if}
                </div>

                <!-- Image and Ingredients displayed next to each other -->
                <div class="flex space-x-2 py-4">

                    <!-- Displaying the image of the recipe -->
                    <div class="pr-6">
                        <img src={"data:image/jpg;base64," + data.recipe.recipe.image64} alt="{data.recipe.recipe.name}"
                             class="w-52 rounded-xl">
                    </div>

                    <!-- Displaying the ingredients of the recipe -->
                    <div>
                        <h3 class="text-xl font-bold pb-1">Zutaten</h3>
                        {#if editMode}
                            <ul>
                                {#each ingredients as ingredient, i (i)}
                                    <li>
                                        <input type="text" name="ingredient" bind:value="{ingredient}"
                                               class="p-1 rounded text-black"/>
                                    </li>
                                {/each}
                                <button type="button" on:click={() => (addIngredient())}>+ Add Ingredient</button>
                            </ul>
                        {:else}
                            <ul>
                                {#each data.recipe.recipe.ingredients as ingredient}
                                    <li>{ingredient}</li>
                                {/each}
                            </ul>
                        {/if}
                    </div>
                </div>

                <!-- Displaying the steps of the recipe underneath the image and ingredients -->
                <div>
                    <h3 class="text-xl font-bold pb-1">Zubereitung</h3>
                    {#if editMode}
                        <input type="text" name="instructions" bind:value="{data.recipe.recipe.instructions}"
                               class="w-full p-2 rounded-xl text-black"/>
                    {:else}
                        <p>{data.recipe.recipe.instructions}</p>
                    {/if}
                </div>

                {#if editMode}
                    <div class="flex justify-center pt-4">
                        <Button type="submit" class="bg-secondary-600 mr-6">
                            Save
                            <CheckCircleSolid class="w-3.5 h-3.5 ms-2.5 text-white" color="white"/>
                        </Button>
                        <Button type="button" formaction="?/deleteRecipe" class="bg-secondary-600">
                            Delete
                            <TrashBinSolid class="w-3.5 h-3.5 ms-2.5 text-white" color="white"/>
                        </Button>
                    </div>
                {/if}
            </form>
        </div>
    </Card>
</div>
