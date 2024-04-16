import type {Actions} from "@sveltejs/kit";

const API_URL = 'http://0.0.0.0:8000';


// The actions object contains the methods for updating and deleting a recipe
export const actions = {
    /**
     * This function is responsible for updating a recipe on the server.
     * It uses the fetch API to make a PUT request to the server.
     */
    updateRecipe: async ({request, fetch, params}) => {
        try {
            // Extracting the recipe data from the request
            const {
                name,
                description,
                ingredients,
                instructions
            } = Object.fromEntries(await request.formData());

            // Constructing the recipe object
            const recipe = {
                name,
                description,
                ingredients,
                instructions
            };

            // Making the PUT request to the server
            const response = await fetch(`${API_URL}/recipe/${params.id}`, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(recipe)
            });

            // If the request was successful, return a success message
            if (response.ok) {
                return {status: 200, message: 'Recipe updated'};
            } else {
                // If the request failed, return an error message
                return {status: 500, message: 'Failed to update recipe'};
            }
        } catch (error) {
            // If an error occurred, return an error message
            return {status: 500, message: 'Failed to update recipe'};
        }
    },

    /**
     * This function is responsible for deleting a recipe from the server.
     * It uses the fetch API to make a DELETE request to the server.
     */
    deleteRecipe: async ({fetch, params}) => {
        try {
            // Making the DELETE request to the server
            const response = await fetch(`${API_URL}/api/recipe/${params.id}`, {method: 'DELETE'});
            // If the request was successful, return a success message
            if (response.ok) {
                return {status: 200, message: 'Recipe deleted'};
            } else {
                // If the request failed, return an error message
                return {status: 500, message: 'Failed to delete recipe'};
            }
        } catch (error) {
            // If an error occurred, return an error message
            return {status: 500, message: 'Failed to delete recipe'};
        }
    }
} satisfies Actions;


/**
 * This function is responsible for loading a recipe from the server.
 * It uses the fetch API to make a GET request to the server.
 */
export const load = async ({fetch, params}) => {
    // This function fetches a recipe from the server
    const fetchRecipe = async () => {
        // Making the GET request to the server
        const response = await fetch(`http://0.0.0.0:8000/recipes/${params.id}`, {method: 'GET'});
        // If the request was successful, return the recipe
        if (response.ok) {
            const data = await response.json();
            return {
                status: 200,
                recipe: await data
            };
        } else {
            // If the request failed, return an error message and an empty recipe
            return {status: 404, message: 'Recipe not found', recipe: {}};
        }
    };

    // Returning the fetched recipe
    return {
        recipe: await fetchRecipe()
    };
}