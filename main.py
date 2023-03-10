import frontend
import Exceptions

if __name__ == '__main__':
    try:
        #welcome
        print(f"Welcome!\n"
              f"This app allows you to find cocktail recipes based on the ingredients you have at home.")

        #input
        ingredients = input("Please type in what ingredients you have at home: ")

        cheers = frontend.create_instance(ingredients)

        #output- list of cocktails for user to choose from
        print("Here is a menu of cocktails for you to choose from: ")
        print(frontend.present_menu(cheers))

        #input
        cocktail_num = input("Please type in the serial number of the chosen cocktail: ")

        #output- recipe
        print(frontend.present_recipe(cocktail_num, cheers))

    except Exceptions.InvalidInput:
        print("invalid input")
    except Exceptions.PageNotFound:
        print("Page not found")
    except Exceptions.NoCocktail as e:
        print(f"No coctail found for your ingredients: {e.ingredients}")
    except Exceptions.CoctailAppError:
        print("unexpected error in Coctails app")
    except Exception:
        print("Unexpected error")