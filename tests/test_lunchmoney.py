from pytest import fixture
# to only define a subset of the response to test on
from lunchmoney import Categories


@fixture
def categories_keys():
    return ['id', 'exclude_from_budget', 'is_income']


def test_get_all_categories(categories_keys):
    """Tests if a list of all categories associated with the user's account is returned"""

    categories_instance = Categories()
    response = categories_instance.get_all_categories()

    assert isinstance(response, dict)
    assert set(categories_keys).issubset(
        dict(response['categories'][0]).keys())
