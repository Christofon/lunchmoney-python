from pytest import fixture
# to only define a subset of the response to test on
from lunchmoney import Categories

def test_get_all_categories():
    """Tests if a list of all categories associated with the user's account is returned"""

    categories_instance = Categories()
    response = categories_instance.get_all_categories()

    assert isinstance(response, dict)
