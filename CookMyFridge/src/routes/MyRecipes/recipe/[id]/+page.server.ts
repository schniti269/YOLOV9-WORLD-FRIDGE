import type {Actions} from "@sveltejs/kit";

const API_URL = 'http://0.0.0.0:8000';

export const actions = {
    updateRecipe: async ({request, fetch, params}) => {
        try {
            const {
                name,
                description,
                ingredients,
                instructions
            } = Object.fromEntries(await request.formData());

            const recipe = {
                name,
                description,
                ingredients,
                instructions
            };
            console.log(recipe);

            const response = await fetch(`${API_URL}/recipe/${params.id}`, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(recipe)
            });

            if (response.ok) {
                return {status: 200, message: 'Recipe updated'};
            } else {
                return {status: 500, message: 'Failed to update recipe'};
            }
        } catch (error) {
            return {status: 500, message: 'Failed to update recipe'};
        }
    },

    deleteRecipe: async ({fetch, params}) => {
        try {
            const response = await fetch(`${API_URL}/api/recipe/${params.id}`, {method: 'DELETE'});
            if (response.ok) {
                return {status: 200, message: 'Recipe deleted'};
            } else {
                return {status: 500, message: 'Failed to delete recipe'};
            }
        } catch (error) {
            return {status: 500, message: 'Failed to delete recipe'};
        }
    }
} satisfies Actions;

export const load = async ({fetch, params}) => {
    const fetchRecipe = async () => {
        const response = await fetch(`http://0.0.0.0:8000/recipes/${params.id}`, { method: 'GET' });
        if (response.ok) {
            const data = await response.json();
            return {
                status: 200,
                recipe: await data
            };
        } else {
            return { status: 404, message: 'Recipe not found', recipe: {} };
        }
    };

    return {
        recipe: await fetchRecipe()
    };
}