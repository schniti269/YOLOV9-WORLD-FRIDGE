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
            image: '/SampleRecipe.png'
        }
    };
}