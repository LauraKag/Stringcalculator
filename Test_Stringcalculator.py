# -*- coding: utf-8 -*-

#%%
from Stringcalculator import Stringcalculator

def test_Stringcalculator_emptystrings():
    emptystrings=["   "," ",""]
    for emptystring in emptystrings:
        assert Stringcalculator(emptystring)==0
        
def test_Stringcalculator_single_string():
    assert Stringcalculator("4")==4
    assert Stringcalculator("8282")==8282

def test_Stringcalculator_long_string():
    assert Stringcalculator("2,3,4,5,3,2")==19
    
    
