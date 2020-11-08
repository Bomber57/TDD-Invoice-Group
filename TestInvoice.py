import pytest
from Invoice import Invoice

@pytest.fixture()
def products():
    products = {'Pen': {'qnt': 10, 'unit_price': 3.75, 'discount': 5},
                'Notebook': {'qnt': 5, 'unit_price': 7.5, 'discount': 10}}
    return products

@pytest.fixture()
def invoice():
    invoice = Invoice()
    return invoice

@pytest.fixture()
def sales_tax():
    sales_tax = 0.0475
    return sales_tax

def test_CanCalculateTotalImpurePrice(invoice, products):
    invoice.totalImpurePrice(products)
    assert invoice.totalImpurePrice(products) == 75

def test_CanCalculateTotalDiscount(invoice, products):
    invoice.totalDiscount(products)
    assert invoice.totalDiscount(products) == 5.62

def test_CanCalculateTotalPurePrice(invoice, products):
    invoice.totalPurePrice(products)
    assert invoice.totalPurePrice(products) == 69.38

def test_CanCalculateFinalPrice(invoice, products, sales_tax):
    invoice.finalPrice(products, sales_tax)
    assert invoice.finalPrice(products, sales_tax) == 72.68

def test_CanRemoveProducts(invoice, products):
    newProducts = {'Pen' : {'qnt': 10, 'unit_price' : 3.75, 'discount' : 5},
                'Notebook': {'qnt' : 5, 'unit_price' : 7.5, 'discount' : 10}}
    assert products == newProducts              # Make sure both dictionaries are the same
    invoice.removeProduct('Pen', newProducts)   # Remove item from dictionary using function
    assert products != newProducts              # Ensure new product list is different
