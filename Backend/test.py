from matcher import match

def test_get_matches():
    mymatch=match(["Fish meat","Chicken meat", "Spices"])
    #remove image from the response and print the rest
    for recipe in mymatch:
        recipe.pop("image")
    
    #get list with only names
    names=[recipe["name"] for recipe in mymatch]
    assert("Fish Tacos" in names)
    assert("Chicken Curry" in names)

if __name__ == "__main__":
    test_get_matches()