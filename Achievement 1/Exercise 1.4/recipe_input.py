import pickle

def take_recipe():
  print('Enter your recipe: ')
  name = input('Enter the name of your recipe: ')
  cooking_time = int(input('Enter the cooking time: '))
  ingredients = []

  while True:
   ingredient = input('Enter an ingredient or write \'done\' to finish: ')
   if ingredient == 'done':    
    break
   else:
    ingredients.append(ingredient)

# Creating a recipe dictionary with name, cooking time and ingredients
  recipe = {
   'name': name,
   'cooking_time': cooking_time,
   'ingredients': ingredients  
  }

# Calculating the difficulty level of the recipe and adding it to the recipe
  difficulty = calc_difficulty(recipe)
# Add the difficult level element to the recipe dictionary
  recipe['difficulty'] = difficulty
  return recipe


# Calculating the difficulty:
def calc_difficulty(recipe):
  if recipe['cooking_time'] < 10 and len(recipe['ingredients']) < 4:
    difficulty = 'Easy'
  elif recipe['cooking_time'] < 10 and len(recipe['ingredients']) >= 4:
    difficulty = 'Medium'
  elif recipe['cooking_time'] >= 10 and len(recipe['ingredients']) < 4:
    difficulty = 'Intermediate'
  else:
    difficulty = 'Hard'
  return difficulty

# Main Code

file = input('Enter the name of your file: ')
try:
  with open('file', 'rb') as my_file:
   data = pickle.load(my_file)

except FileNotFoundError:
  print('The filename is not found, creating a new dictionary ... ')
  recipes_list = []
  all_ingredients = []
  data = {
    'recipes_list': recipes_list,
    'all_ingredients': all_ingredients
  }

except:
  print('An unexpected error occurred. Creating a new dictionary ...')
  recipes_list = []
  all_ingredients = []
  data = {
    'recipes_list': recipes_list,
    'all_ingredients': all_ingredients
  }

else:
  my_file.close()

finally:
  recipes_list = data['recipes_list']
  all_ingredients = data['all_ingredients']


# Asking the user how many recipes would like to enter
n_recipes = int(input('Enter how many recipes you would like to enter: '))

# Take a recipe and add it to the recipes_list
for i in range(n_recipes):
  recipe = take_recipe()
  

  # Update all_ingredients with new ingredients
  for ingredient in recipe['ingredients']:
    if ingredient not in all_ingredients:
      all_ingredients.append(ingredient)

  # Add the recipe to the recpes_list
  recipes_list.append(recipe)   

# Save the recipes_list and all_ingredients to a dicionary
data = {
  'recipes_list': recipes_list,
  'all_ingredients': all_ingredients
  }

# Save rhe dictionary to a user-specified file
file = input('Enter te filename where you would like to store your recipes: ')
with open('file', 'wb') as my_file:
  pickle.dump(data, my_file)
  print('Recipes saved successfully!')  