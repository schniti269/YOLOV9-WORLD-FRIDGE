from matcher import match
import pytest

import cv2
import numpy as np
from app import cookie_auth



def test_get_matches1():
    mymatch=match(["Fish meat","Chicken meat", "Spices","taco"])
    #remove image from the response and print the rest
    for recipe in mymatch:
        recipe.pop("image")
    print(mymatch)
    
    #get list with only names
    names=[recipe["name"] for recipe in mymatch]
    assert("Fish Tacos" in names)


def test_get_matches2():
    #test no matches
    mymatch=match([])

    assert(mymatch==[])

def test_get_matches3():
    #test multiple same objects
    #banana bread and banana bread
    mymatch=match(["Bananas","Bananas"])

    assert(len(mymatch)==1)

def test_get_matches4():
    #test multiple same objects with som other object in between
    #banana bread and banana bread
    mymatch=match(["Bananas","Chicken meat","Bananas"])

    assert(len(mymatch)==1)


#test cookie_auth
def test_cookie_auth_invalid_cookie():
    #test if the cookie is invalid if error is raised
    with pytest.raises(Exception):
        cookie_auth(0)

from db import add_recipe



from db import badword_filter
def test_badword_filter():
    #test badword filter
    assert(badword_filter("Test Description")==False)
    assert(badword_filter("Test Description DRUGS")==True)





if __name__ == "__main__":
    #test the test.py
    pytest.main(["-v", __file__])
