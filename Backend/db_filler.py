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

def fill_db():
    db=get_db()

    #fill ingredients
    fill_ingredients(db)

    #fill recipes
    fill_recipes(db)

    db.commit()



def fill_ingredients(db):
    for item in kitchen_items:
        db.add(Ingredient(name=item))


def fill_recipes(db):
    """
    class Recipe(Base):
    __tablename__ = "recipies"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    instructions = Column(String)
    ingredients = Column(PickleType)
    image = Column(PickleType)"""

    from matcher import add_recipe
    imaages_path = "images/"
    add_recipe("Banana Bread", "A delicious bread made from bananas", "Mix bananas with flour and bake", ["Bananas", "Flour"], imaages_path+"banana_bread.jpg")
    add_recipe("Blueberry Muffins", "A delicious muffin made from blueberries", "Mix blueberries with flour and bake", ["Blueberries", "Flour"], imaages_path+"aFM5az0.jpg")
    add_recipe("Citrus Salad", "A delicious salad made from citrus fruits", "Mix citrus fruits with lettuce", ["Citrus (Lemons, Oranges)", "Leafy Greens (Spinach, Lettuce)"], imaages_path+"citrus_salad.jpg")
    add_recipe("Grape Juice", "A delicious juice made from grapes", "Blend grapes and add water", ["Grapes", "Water"], imaages_path+"grape_juice.jpg")
    add_recipe("Mango Smoothie", "A delicious smoothie made from mangoes", "Blend mangoes and add milk", ["Mangoes", "Milk"], imaages_path+"mango_smoothie.jpg")
    add_recipe("Chicken Curry", "A delicious curry made from chicken", "Cook chicken with spices", ["Chicken meat", "Spices"], imaages_path+"chicken_curry.jpg")
    add_recipe("Beef Stew", "A delicious stew made from beef", "Cook beef with vegetables", ["Beef meat", "Vegetables"], imaages_path+"beef_stew.jpg")
    add_recipe("Fish Tacos", "A delicious taco made from fish", "Cook fish with spices", ["Fish meat", "Spices"], imaages_path+"fish_tacos.jpg")
    add_recipe("Pork Chops", "A delicious dish made from pork", "Cook pork with spices", ["Pork meat", "Spices"], imaages_path+"pork_chops.jpg")
    add_recipe("Egg Salad", "A delicious salad made from eggs", "Boil eggs and mix with mayonnaise", ["Eggs", "Mayonnaise"], imaages_path+"egg_salad.jpg")
    add_recipe("Milkshake", "A delicious drink made from milk", "Blend milk with ice cream", ["Milk", "Ice Cream"], imaages_path+"milkshake.jpg")

                    