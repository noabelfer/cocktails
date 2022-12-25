class CoctailAppError(Exception):
    pass

class InvalidInput(CoctailAppError):
    pass
class PageNotFound(CoctailAppError):
    pass
class EmptyPage(CoctailAppError):
    pass
class NoCocktail(CoctailAppError):
    def __init__(self, ingredients):
        self.ingredients = ingredients