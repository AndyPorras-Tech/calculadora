from calculadora import suma,resta,division
import pytest

def test_sumar():
    assert suma (2,3)==5

def test_resta():
    assert resta (10,6)==4

def test_division():
    assert division(9,3)==3

def test_dividir_cero():
    with pytest.raises(ValueError):
        division(10,0)