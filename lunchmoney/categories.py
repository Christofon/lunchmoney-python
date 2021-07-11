from . import session


class Categories(object):
    
    @staticmethod
    def get_all_categories() -> dict:
        """Get a list of all categories associated with the user's account."""
        path = 'https://dev.lunchmoney.app/v1/categories'
        response = session.get(path)
        return response.json()

    def create_categorie(self, categorie_dict: dict) -> dict:
        """
        Create a single category.

        Parameters
        ----------
        categories_dict : dict
            name : str
                [required] - Name of category. Must be between 1 and 40 characters.
            description : str
                Description of category. Must be less than 140 categories.
            is_income : boolean
                Whether or not transactions in this category should be treated as income.
            exclude_from_budget : boolean
                Whether or not transactions in this category should be excluded from budgets.
            exclude_from_totals : boolean
                Whether or not transactions in this category should be excluded from calculated totals.
        """
        path = 'https://dev.lunchmoney.app/v1/categories'
        response = session.post(path, categorie_dict)
        return response.json()
