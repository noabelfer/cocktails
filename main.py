import frontend
import backend
import Exceptions

if __name__ == '__main__':
    try:
        #welcome
        print(f"Welcome!\n"
              f"This app allows you to find cocktail recipes based on the ingredients you have at home.")

        #input
        ingredients = input("Please type in what ingredients you have at home: ")

        #output- list of cocktails for user to choose from
        print("Here is a menu of cocktails for you to choose from: ")

        cocktail_menu = backend.create_cocktail_menu(ingredients) #save for use later

        print(frontend.print_menu_nicely(cocktail_menu))

        #input
        cocktail_num = input("Please type in the serial number of the chosen cocktail: ")

        #output- recipe
        cocktail = frontend.cocktail_num_to_name(cocktail_num, cocktail_menu)
        recipe = backend.get_recipe(cocktail)
        print(frontend.print_recipe_nicely(recipe))

    except Exceptions.InvalidInput:
        print("invalid input")
    except Exceptions.PageNotFound:
        print("Page not found")