// Importing the writable function from Svelte's store module
import {writable} from 'svelte/store';

/**
 * A writable store that holds the state of the login card.
 * It starts as false, meaning the login card is not open.
 * When set to true, the login card opens.
 */
export const openLoginCard = writable(false);

/**
 * A writable store that holds the state of the recipe edit mode.
 * It starts as false, meaning the recipe edit mode is not active.
 * When set to true, the recipe edit mode becomes active.
 */
export const recipeEditMode = writable(false);