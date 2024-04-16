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

    // Exported variable to hold the data passed to the component
    export let data;

    // Variable to hold the edit mode state. It starts as false.
    let editMode = false;
    // Subscribing to the recipeEditMode store. Whenever the store's value changes,
    // the new value is assigned to the editMode variable.
    recipeEditMode.subscribe(value => editMode = value);

    // Variable to hold the list of ingredients of the recipe.
    // It is initialized with the ingredients of the recipe passed in the data prop.
    let ingredients: string[] = data.recipe.recipe.ingredients;

    /**
     * Function to add a new ingredient to the ingredients list.
     * It creates a new array with the current ingredients and an empty string at the end,
     * and assigns it to the ingredients variable.
     */
    function addIngredient() {
        ingredients = [...ingredients, ""];
    }
</script>

<!-- Main container for the page -->
<div class="flex justify-center pt-10">
    <!-- Card component from Flowbite Svelte library -->
    <Card size="xl" class="bg-secondary-400 text-white rounded-2xl">

        <!-- Card Header -->
        <div class="flex justify-between bg-secondary-600 px-5 py-4 rounded-xl -m-8">
            <!-- Button to navigate back to the MyRecipes page -->
            <button on:click={() => (goto("/MyRecipes"))}>
                <ArrowLeftSolid class="w-10 h-10 rounded-3xl border-2"/>
            </button>
            <!-- Displaying the name of the recipe -->
            <h1 class="text-4xl">Recipe: {data.recipe.recipe.name}</h1>
            <!-- Container for the buttons -->
            <div>
                <!-- Button to add the recipe to favorites -->
                <button type="button">
                    <HeartOutline class="w-10 h-10 rounded-3xl border-2 bg-red-600 p-1" color="white"/>
                </button>

                <!-- If the edit mode is active, display the Close button -->
                {#if editMode}
                    <!-- Button to close the edit mode -->
                    <button type="button" on:click={() => (recipeEditMode.set(false))}>
                        <CloseSolid class="w-10 h-10 rounded-3xl border-2 bg-primary-600 p-1" color="white"/>
                    </button>
                    <!-- If the edit mode is not active, display the Edit button -->
                {:else}
                    <!-- Button to activate the edit mode -->
                    <button type="button" on:click={() => (recipeEditMode.set(true))}>
                        <EditSolid class="w-10 h-10 rounded-3xl border-2 bg-primary-600 p-1" color="white"/>
                    </button>
                {/if}

            </div>
        </div>

        <!-- Card Body -->
        <div class="mt-14">

            <!-- Form to update the recipe -->
            <form method="POST" action="?/updateRecipe">

                <!-- If the recipe was not found, display a message -->
                {#if data.recipe.status !== 200}
                    <div class="text-center">
                        <h2 class="text-2xl">{data.recipe.message}</h2>
                    </div>
                {/if}

                <!-- Displaying the title and description of the recipe -->
                <div>
                    <!-- If the edit mode is active, display input fields for the title and description -->
                    {#if editMode}
                        <label for="title" class="text-xl font-bold">Title:</label>
                        <input type="text" id="name" name="name" value="{data.recipe.recipe.name}"
                               class="w-full p-2 rounded-xl text-black mb-2"/>

                        <label for="description" class="text-xl font-bold">Description:</label>
                        <input type="text" id="description" name="description" value="{data.recipe.recipe.description}"
                               class="w-full p-2 rounded-xl text-black"/>
                        <!-- If the edit mode is not active, display the title and description as text -->
                    {:else}
                        <h2>{data.recipe.recipe.name}: {data.recipe.recipe.description}</h2>
                    {/if}
                </div>

                <!-- Displaying the image and ingredients of the recipe -->
                <div class="flex space-x-2 py-4">

                    <!-- Displaying the image of the recipe -->
                    <div class="pr-6">
                        <img src={"data:image/jpg;base64," + data.recipe.recipe.image64} alt="{data.recipe.recipe.name}"
                             class="w-52 rounded-xl">
                    </div>

                    <!-- Displaying the ingredients of the recipe -->
                    <div>
                        <h3 class="text-xl font-bold pb-1">Zutaten</h3>
                        <!-- If the edit mode is active, display input fields for the ingredients -->
                        {#if editMode}
                            <ul>
                                {#each ingredients as ingredient, i (i)}
                                    <li>
                                        <input type="text" name="ingredient" bind:value="{ingredient}"
                                               class="p-1 rounded text-black"/>
                                    </li>
                                {/each}
                                <!-- Button to add a new ingredient -->
                                <button type="button" on:click={() => (addIngredient())}>+ Add Ingredient</button>
                            </ul>
                            <!-- If the edit mode is not active, display the ingredients as text -->
                        {:else}
                            <ul>
                                {#each data.recipe.recipe.ingredients as ingredient}
                                    <li>{ingredient}</li>
                                {/each}
                            </ul>
                        {/if}
                    </div>
                </div>

                <!-- Displaying the steps of the recipe -->
                <div>
                    <h3 class="text-xl font-bold pb-1">Zubereitung</h3>
                    <!-- If the edit mode is active, display an input field for the steps -->
                    {#if editMode}
                        <input type="text" name="instructions" bind:value="{data.recipe.recipe.instructions}"
                               class="w-full p-2 rounded-xl text-black"/>
                        <!-- If the edit mode is not active, display the steps as text -->
                    {:else}
                        <p>{data.recipe.recipe.instructions}</p>
                    {/if}
                </div>

                <!-- If the edit mode is active, display the Save and Delete buttons -->
                {#if editMode}
                    <div class="flex justify-center pt-4">
                        <!-- Button to submit the form and save the changes -->
                        <Button type="submit" class="bg-secondary-600 mr-6">
                            Save
                            <CheckCircleSolid class="w-3.5 h-3.5 ms-2.5 text-white" color="white"/>
                        </Button>
                        <!-- Button to delete the recipe -->
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