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
            return { status: 404, message: 'No recipe found', recipe: {} };
        }
    };*/

    return {
        //recipe: fetchRecipe()
        recipe: {
            title: 'Recipe title',
            description: 'Recipe description',
            ingredients: [
                {name: 'Ingredient 1', amount: '1', unit: 'unit'},
                {name: 'Ingredient 2', amount: '2', unit: 'unit'}
            ],
            steps: [
                {description: 'Step 1'},
                {description: 'Step 2'}
            ]
        }
    };
}