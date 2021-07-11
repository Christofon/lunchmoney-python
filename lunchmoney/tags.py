from . import session


class Tags():

    @staticmethod
    def get_all_tags() -> dict:
        """Get a list of all tags associated with the user's account."""
        path = 'https://dev.lunchmoney.app/v1/tags'
        response = session.get(path)
        return response.json()
