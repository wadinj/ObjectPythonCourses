import pytest
# Par defaut, la découverte des tests, recherche des fichiers finissant par _test ou commençant par test_
def addition(x, y):
    return x + y

def test_add_should_return_correct_results():
    assert addition(1, 2) == 3
