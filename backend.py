import requests
import Exceptions

def create_cocktail_menu(ingredients):
    cocktail_menu = []
    l_ingredients = [ingredient for ingredient in ingredients.split(",")]
    if len(l_ingredients) == 1:
        ingredient_str = l_ingredients[0]
    elif len(l_ingredients) > 1:
        ingredient_str = "&".join(l_ingredients)
    elif len(l_ingredients) == 0:
        raise Exceptions.InvalidInput

    response = requests.get(f"https://www.thecocktaildb.com/api/json/v1/1/filter.php?i={ingredient_str}")

    if response.status_code >= 400:
        raise Exceptions.PageNotFound

    cocktail_dict = response.json()
    cocktail_list = [cocktail_dict['drinks'][i]['strDrink'] for i in range(len(cocktail_dict['drinks']))]
    for i, v in enumerate(cocktail_list):
        cocktail_menu.append((i, v))
    return cocktail_menu

# no need for this
# def create_collated_menu(ingredients : list[str]):
#     list_of_menus = [create_cocktail_menu(ingredient) for ingredient in ingredients]
#     collated_menu = []
#     for i in range(len(list_of_menus)-1):
#         for drink in list_of_menus[i]:
#             if drink in list_of_menus[i+1]:
#                 collated_menu.append(drink)
#     return collated_menu

def get_recipe(cocktail):
    response = requests.get(f"https://www.thecocktaildb.com/api/json/v1/1/search.php?s={cocktail}")

    if response.status_code >= 400:
        raise Exceptions.PageNotFound

    drinks_dict = response.json()['drinks'][0]
    instructions = drinks_dict["strInstructions"]
    ingredients = [drinks_dict[f"strIngredient{i}"] for i in range(1,16) if drinks_dict[f"strIngredient{i}"]]
    amounts = [drinks_dict[f"strMeasure{i}"] for i in range(1, len(ingredients))]
    ingredients_and_amounts = [(ingredients[h], amounts[h]) for h in range(0,len(amounts))]
    return instructions, ingredients_and_amounts
