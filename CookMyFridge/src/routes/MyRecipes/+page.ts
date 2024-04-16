/**
 * This function is responsible for loading recipes from the server.
 * It uses the fetch API to make a GET request to the server.
 */
export const load = async ({fetch}) => {

    const fetchRecipes = async () => {
        try {
            const response = await fetch('http://0.0.0.0:8000/recipes', {method: 'GET'});
            if (response.ok) {
                const data = await response.json();
                return {status: 200, recipes: await data};
            } else {
                return {status: 500, message: 'Failed to fetch recipes'};
            }
        } catch (error) {
            return {status: 500, message: 'Failed to fetch recipes: ' + error};
        }
    };

    return {
        recipes: await fetchRecipes()
    };
};