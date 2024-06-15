import pickle
tea_recipe = {
  'Ingredient Name': 'Tea',
  'Ingredients': ['Tea Leaves', 'Water', 'Sugar'],
  'Cooking Time': 5,
  'Difficulty': 'Easy'}

with open('recipe_binary.bin', 'wb') as my_bfile:
   pickle.dump(tea_recipe, my_bfile)
  
with open('recipe_binary.bin', 'rb') as mybloadFile:
   loaded_tea_recipe = pickle.load(mybloadFile)

print('Tea Recipe Details - ')
print('Ingredient Name: '+ loaded_tea_recipe['Ingredient Name'])
print('Ingredients: ', loaded_tea_recipe['Ingredients'])
print('Cooking Time: ' + str(loaded_tea_recipe['Cooking Time']))
print('Difficulty: ' + loaded_tea_recipe['Difficulty'])