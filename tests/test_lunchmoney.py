import vcr
# to only define a subset of the response to test on
from pytest import fixture

from lunchmoney import Categories, Tags


@fixture
def categories_keys():
    return ['id', 'exclude_from_budget', 'is_income']


@vcr.use_cassette('tests/records/categories.yml', filter_query_parameters=['access_token'])
def test_get_all_categories(categories_keys):
    """Tests if a list of all categories associated with the user's account is returned."""
    categories_instance = Categories()
    response = categories_instance.get_all_categories()

    assert isinstance(response, dict)
    assert set(categories_keys).issubset(
        dict(response['categories'][0]).keys())


@vcr.use_cassette('tests/records/create_categorie.yml', filter_query_parameters=['access_token'])
def test_create_categorie():
    """Test if a test categorie is created."""
    categories_instance = Categories()
    response = categories_instance.create_categorie({'name': 'Test'})

    assert response['category_id']


@vcr.use_cassette('tests/records/tags.yml', filter_query_parameters=['access_token'])
def test_get_all_tags():
    """Test if a list of tags gets returned."""
    tags_instance = Tags()
    response = tags_instance.get_all_tags()

    assert set(['id', 'name']).issubset(response[0])
