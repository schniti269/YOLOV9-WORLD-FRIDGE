from db import get_db, User, Recipe, Ingredient, image_to_base64
import pandas as pd

db = next(get_db())




def match(items: pd.DataFrame):
    matches = []
    for item in items:
        #query the recipes in ingredients
        ingredient = db.query(Ingredient).filter(Ingredient.name == item).first()
        if ingredient is None:
            continue
        for recipe in ingredient.recipes:
            matches.append(recipe)
    
    for recipe in matches:
        #recipie neets to have all 
        if not all([item in recipe.ingredients for item in items]):
            matches.remove(recipe)

    if len(matches) == 0:
        #todo query list to chat GPT
        pass
    
    return matches


   

def add_recipe(name, description, instructions, ingredients, path_image):

    base64_image = image_to_base64(path_image)
    
    db = next(get_db())
    recipe = Recipe(name=name, description=description, instructions=instructions, ingredients=ingredients, image64=base64_image)
    db.add(recipe)
    db.commit()

    #reverse index in ingredients
    ctr=0
    for ingredient in ingredients:
        #query for ingredient
        ingredient = db.query(Ingredient).filter(Ingredient.name == ingredient).first()
        if ingredient is None:
            ctr+=1
            ingredient = Ingredient(name=ingredient, recipes=[])
            db.add(ingredient)
            db.commit()
        
        recipies= ingredient.recipes
        #cast to list
        recipies.append(recipe)
        ingredient.recipes=recipies
        db.commit()
    
    return recipe , "Recipe added successfully", f"learning {ctr} new ingredients"

def query_recipies_from_LLM(items):
    

    task="You are supposed to behave like an API You can only return a JSON object"
    promt=task+"I have "+", ".join(items)+" what can I cook with this?"
    instructions= promt+"Return your Suggestions in the format of JSON {\"name\":\"name\",\"description\":\"description\",\"instructions\":\"instructions\",\"ingredients\":[\"ingredient1\",\"ingredient2\"]}"

    #todo query list to chat GPT
    pass


