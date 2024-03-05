#!/usr/bin/env python3

class Dog:
    def __init__(self, name, breed="Mutt"):
        self.name = name
        self.breed = breed

def test_self_name(self):
    fido = Dog("Fido")
    assert(fido.name == "Fido")

def test_saves_self_breed(self):
    fido = Dog("Fido", "Dalmatian")
    assert(fido.breed == "Dalmatian")

def test_default_breed(self):
    fido = Dog("Fido")
    assert(fido.breed == "Mutt")

    

    
