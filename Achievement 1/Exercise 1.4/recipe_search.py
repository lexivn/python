import pickle

# Function to display a recipe's arguments
def display_recipe(recipe):  
  print('Recipe Name: ', recipe['name'])
  print('Cooking Time: ', recipe['cooking_time'])
  print('Ingredients: ', recipe['ingredients'])
  print('Difficulty: ', recipe['difficulty'])

# Function to search for an ingredient in the given data
def search_ingredient(data):

  #Show the user all the available ingredients contained in data
  available_ingredients = list(enumerate(data['all_ingredients']))
  print('The available ingredients are: ', available_ingredients)

  try:
    n = int(input('Pick a number from the list of ingredients available: '))
    ingredient_searched = available_ingredients[n][1]
  except ValueError:
    print('Input not found')  
  else:
    # Search for recipes containing the ingredient choosen
    recipes_found =[]
    for recipe in data['recipes_list']:
      if ingredient_searched in recipe['ingredients']:
        recipes_found.append(recipe)
    
    # Display the recipe's arguments
    print('Displaying all the recipes containing the ingredient: ', ingredient_searched)
    for recipe in recipes_found:
      display_recipe(recipe)


# Main code

# Ask the user for the name of the file that contains your recipe data
file = input('Enter the filename where you stored your recipes: ')

try:
  my_file = open('file', 'rb')
  data = pickle.load(my_file)

except FileNotFoundError:
  print('The file hasn\'nt been found')

else:
  search_ingredient(data)

finally:
  print('Success!')
  my_file.close()



