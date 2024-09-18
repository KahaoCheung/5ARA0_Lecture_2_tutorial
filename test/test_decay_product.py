from pytest_bdd import scenario, given, when, then


# @scenario('decay_product.feature', 'Discount product quality over time')
# def test_discount_product_quality():
#     pass


@given("a product")
def given_product(product):
    pass


@when("time passes")
def when_time_passes(product):
    product.tick()


@then("product quality should deteriorate")
def then_quality_should_deteriorate(product):
    assert product.days_remaining == 1
    assert product.quality == 1