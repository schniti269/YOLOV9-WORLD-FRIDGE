import type {Actions} from "@sveltejs/kit";

const API_URL = 'http://localhost:3000';

export const actions = {
    updateRecipe: async ({request, fetch}) => {
        try {
            const formData = await request.formData();

            const title = formData.get('title');
            const description = formData.get('description');

            // Construct the ingredients array manually
            const ingredients = [];
            for (let i = 0; i < formData.getAll('ingredient_name').length; i++) {
                ingredients.push({
                    name: formData.getAll('ingredient_name')[i],
                    amount: formData.getAll('ingredient_amount')[i],
                    unit: formData.getAll('ingredient_unit')[i]
                });
            }

            // Construct the steps array manually
            const steps = [];
            for (let i = 0; i < formData.getAll('step_description').length; i++) {
                steps.push({
                    description: formData.getAll('step_description')[i]
                });
            }

            const recipe = {
                title,
                description,
                ingredients,
                steps
            };

            const response = await fetch(`${API_URL}/api/recipe`, {
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
            const response = await fetch(`${API_URL}/api/recipe/${params.title}`, {method: 'DELETE'});
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
    /*const fetchRecipe = async () => {
        const response = await fetch(`/api/recipe/${params.title}`, { method: 'GET' });
        const data = await response.json();
        if (data.recipe) {
            return {
                status: 200,
                recipe: data.recipe
            };
        } else {
            return { status: 404, message: 'Recipe not found', recipe: {} };
        }
    };*/

    return {
        //recipe: fetchRecipe()
        recipe: {
            title: 'Recipe title',
            description: 'Recipe description',
            ingredients: [
                {name: 'Ingredient 1', amount: '1', unit: 'unit'},
                {name: 'Ingredient 2', amount: '2', unit: 'unit'},
                {name: 'Ingredient 3', amount: '3', unit: 'unit'},
                {name: 'Ingredient 4', amount: '4', unit: 'unit'}
            ],
            steps: [
                {description: 'Step 1'},
                {description: 'Step 2'},
                {description: 'Step 3'},
                {description: 'Step 4'}
            ],
            image: '/SampleRecipe.png',
            status: 200,
            message: 'Recipe found'
        }
    };
}