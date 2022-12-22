import Exceptions


def print_menu_nicely(menu):
    for drink_tuple in menu:
        print (f"{drink_tuple[0]}. {drink_tuple[1]}")

def print_recipe_nicely(recipe):
    print(f"Ingredients:\n")
    for ingredient in recipe[1]:
        print(f"{ingredient[0]}: {ingredient[1]}")
    print(f"Instructions:\n"
          f"{recipe[0]}")

def cocktail_num_to_name(cocktail_num, cocktail_menu):
    cocktail_num = int(cocktail_num)
    if cocktail_num not in range(len(cocktail_menu)):
        raise Exceptions.InvalidInput
    cocktail = cocktail_menu[cocktail_num][1]
    return cocktail
