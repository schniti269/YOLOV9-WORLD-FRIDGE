from db import get_db, User, Recipe, Ingredient, image_to_base64
import pandas as pd
print("loading matcher")
db = next(get_db())
print("matcher loaded")




def match(items: list):

    matchesid = []
    #get all recipies that contain ANY items
    for item in items:
        #query the recipes in ingredients
        ingredient = db.query(Ingredient).filter(Ingredient.name == item).first()
        if ingredient is None:
            #this should not happen ever but just in case
            continue
        for recipeid in ingredient.recipes:
            matchesid.append(recipeid)
    
    #filter out all where request items cannot fulfill the recipe
    for recipeid in matchesid:
        #recipie neets to have all 
        recipe = db.query(Recipe).filter(Recipe.id == recipeid).first()
        if recipe is None:
            #this should not happen ever but just in case
            continue
        for item in items:
            if item not in recipe.ingredients:
                matchesid.remove(recipeid)
                break
    
    if len(matchesid) == 0:
        #todo query list to chat GPT
        pass
    #remove duplicates
    matchesid = list(set(matchesid))
    #ready matches
    matches = []
    for recipeid in matchesid:
        recipe = db.query(Recipe).filter(Recipe.id == recipeid).first()
        matches.append(recipe)
    #prepare the response
    matches = [{"id":recipe.id,"name": recipe.name, "description": recipe.description, "instructions": recipe.instructions, "ingredients": recipe.ingredients,"image":recipe.image64} for recipe in matches]
    
    return matches


   

def add_recipe(name, description, instructions, ingredients, path_image):
    print("adding recipe")
    base64_image = image_to_base64(path_image)
    print("image converted")
    
    db = next(get_db())
    dbrecipe = Recipe(name=name, description=description, instructions=instructions, ingredients=ingredients, image64=base64_image)
    db.add(dbrecipe)
    db.commit()


    for ingredient in ingredients:
        #query for ingredient
        dbingredient = db.query(Ingredient).filter(Ingredient.name == ingredient).first()#

        ctr=0
        if dbingredient is None:
            ctr+=1
            newdbingredient = Ingredient(name=ingredient, recipes=[])
            db.add(newdbingredient)
            db.commit()

        dbingredient = db.query(Ingredient).filter(Ingredient.name == ingredient).first()
        recipies=dbingredient.recipes.copy()
        #cast to list
        recipies.append(dbrecipe.id)
        dbingredient.recipes=recipies
        db.commit()
    
    return dbrecipe , "Recipe added successfully", f"learning {ctr} new ingredients"

def query_recipies_from_LLM(items):
    

    task="You are supposed to behave like an API You can only return a JSON object"
    promt=task+"I have "+", ".join(items)+" what can I cook with this?"
    instructions= promt+"Return your Suggestions in the format of JSON {\"name\":\"name\",\"description\":\"description\",\"instructions\":\"instructions\",\"ingredients\":[\"ingredient1\",\"ingredient2\"]}"

    #todo query list to chat GPT
    pass


