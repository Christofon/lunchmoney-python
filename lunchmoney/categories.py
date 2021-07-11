from . import session

class Categories(object):
    def __init__(self):
        pass

    @staticmethod
    def get_all_categories() -> dict:
        """get a list of all categories associated with the user's account"""
        path = 'https://dev.lunchmoney.app/v1/categories'
        response = session.get(path)
        return response.json()
