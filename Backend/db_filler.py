from db import get_db, Ingredient, Recipe

kitchen_items = [
    "Bananas", "Blueberries", "Citrus (Lemons, Oranges)", "Grapes", "Mangoes",
    "Leafy Greens (Spinach, Lettuce)", "Tomatoes", "Mushrooms", "Zucchini", "Potatoes",
    "Chicken meat", "Beef meat", "Fish meat", "Pork meat", "Eggs",
    "Milk", "Cheese", "Butter", "Yogurt", "Cream",
    "Water", "Juices", "Soft Drinks", "Beer", "Wine",
    "Bread", "Cereal", "Pasta", "Rice", "Flour",
    "Sugar", "Salt", "Pepper", "Spices", "Oil",
    "Tomato Sauce", "Mayonnaise", "Mustard", "Ketchup", "Soy Sauce",
    "paprika","pak choi","peas","pepper","pineapple","pomegranate","potato","pumpkin","radish","raspberry",
    "onion","packaged food","egg","coconut","cucumber","butter","carrots"
]

def fill_db