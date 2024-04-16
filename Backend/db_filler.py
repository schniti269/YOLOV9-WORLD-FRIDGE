from db import get_db, Ingredient, Recipe


def fill_db():
    #fill recipes
    fill_recipes()

    





def fill_recipes():
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
    print("filling recipes")
    add_recipe("Banana Bread", "A delicious bread made from bananas", "Mix bananas with flour and bake", ["Bananas"], imaages_path+"banana_bread.jpg")
    add_recipe("Blueberry Muffins", "A delicious muffin made from blueberries", "Mix blueberries with flour and bake", ["Blueberries"], imaages_path+"aFM5az0.jpg")
    add_recipe("Citrus Salad", "A delicious salad made from citrus fruits", "Mix citrus fruits with lettuce", ["Citrus (Lemons, Oranges)", "Leafy Greens (Spinach, Lettuce)"], imaages_path+"citrus_salad.jpg")
    add_recipe("Grape Juice", "A delicious juice made from grapes", "Blend grapes and add water", ["Grapes"], imaages_path+"grape_juice.jpg")
    add_recipe("Mango Smoothie", "A delicious smoothie made from mangoes", "Blend mangoes and add milk", ["Mangoes"], imaages_path+"mango_smoothie.jpg")
    add_recipe("Chicken Curry", "A delicious curry made from chicken", "Cook chicken with spices", ["Chicken meat", "spinach"], imaages_path+"chicken_curry.jpg")
    add_recipe("Beef Stew", "A delicious stew made from beef", "Cook beef with vegetables", ["Beef meat", "Vegetables"], imaages_path+"beef_stew.jpg")
    add_recipe("Fish Tacos", "A delicious taco made from fish", "Cook fish with spices", ["Fish meat", "taco"], imaages_path+"fish_tacos.jpg")
    add_recipe("Pork Chops", "A delicious dish made from pork", "Cook pork with spices", ["Pork meat"], imaages_path+"pork_chops.jpg")
    add_recipe("Egg Salad", "A delicious salad made from eggs", "Boil eggs and mix with mayonnaise", ["Eggs", "Mayonnaise"], imaages_path+"egg_salad.jpg")
    add_recipe("Milkshake", "A delicious drink made from milk", "Blend milk with ice cream", ["Milk", "Ice Cream"], imaages_path+"milkshake.jpg")
    add_recipe("Cheeseburger", "A delicious burger made from cheese", "Cook beef and add cheese", ["Beef meat", "Cheese","Bread"], imaages_path+"cheeseburger.jpg")
    add_recipe("Spaghetti", "A delicious pasta made from spaghetti", "Cook spaghetti and add tomato sauce", ["Tomatoes"], imaages_path+"spaghetti.jpg")
    add_recipe("Salad", "A delicious salad made from vegetables", "Mix vegetables and add dressing", ["Leafy Greens (Spinach, Lettuce)", "Tomatoes"], imaages_path+"salad.jpg")
    add_recipe("Omelette", "A delicious dish made from eggs", "Cook eggs with vegetables", ["Eggs", "Vegetables"], imaages_path+"omelette.jpg")
    add_recipe("Fruit Salad", "A delicious salad made from fruits", "Mix fruits and add dressing", ["Bananas", "Blueberries"], imaages_path+"fruitsalad.jpg")
    add_recipe("Filled Peppers", "A delicious dish made from peppers", "Cook peppers with meat", ["Peppers", "Beef meat"], imaages_path+"filled_peppers.jpg")
    add_recipe("Tomato Soup", "A delicious soup made from tomatoes", "Cook tomatoes with spices", ["Tomatoes"], imaages_path+"tomato_soup.jpg")
    add_recipe("Mushroom Risotto", "A delicious risotto made from mushrooms", "Cook mushrooms with rice", ["Mushrooms"], imaages_path+"mushroom_risotto.jpg")
    add_recipe("Orange Chicken", "A delicious dish made from chicken", "Cook chicken with orange sauce", ["Chicken meat", "Citrus (Lemons, Oranges)"], imaages_path+"orange_chicken.jpg")
    add_recipe("Oven Baked Potatoes", "A delicious dish made from potatoes", "Bake potatoes with spices", ["Potatoes","Yogurt"], imaages_path+"oven_potatoe.jpg")
    add_recipe("Baked Pumpkin", "A delicious dish made from pumpkin", "Bake pumpkin with spices", ["Pumpkin"], imaages_path+"baked_pumpkin.jpg")


if __name__ == "__main__":
    fill_db()