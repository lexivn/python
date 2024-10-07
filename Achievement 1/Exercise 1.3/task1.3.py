recipes_list = []
ingredients_list = []

def take_recipe():
  name = input("Enter the name of the recipe: ")
  cooking_time = int(input("Enter the cooking time: "))
  ingredients = []
  while True:
    ingredient = input("Enter an ingredient name or type \'done'\ if you " \
                       "finish to enter the ingredients: ")
    ingredients.append(ingredient)
    if ingredient == 'done':
      break

  recipe = {
    'name': name,
    'cooking_time': cooking_time,
    'ingredients': ingredients
  }
  return recipe

#
n = int(input("How many recipes you want to enter: "))

#
for i in range(0,n):
  recipe = take_recipe()
  for ingredient in recipe['ingredients']:
    if ingredient not in ingredients_list:
      ingredients_list.append(ingredient)
  recipes_list.append(recipe)
  
#
for recipe in recipes_list:
  if recipe["cooking_time"] < 10 and len(recipe["ingredients"]) < 4:
    recipe["difficulty"] = "Easy"
  elif recipe['cooking_time'] < 10 and len(recipe["ingredients"]) >= 4:
    recipe["difficulty"] = "Medium"
  elif recipe["cooking_time"] >= 10 and len(recipe["ingredients"]) < 4:
    recipe["difficulty"] = "Intermediate"
  else:    
    recipe["difficulty"] = "Hard"
  
print(ingredients_list)