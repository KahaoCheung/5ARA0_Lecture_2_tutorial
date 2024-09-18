import pytest
from product import Product


def __init__():
    pass


@pytest.fixture
def product():
    return Product(2, 2)