# Create a class called ShoppingList
class ShoppingList:
  def __init__(self, list_name):
    self.list_name = list_name
    self.shopping_list = []

  def add_item(self, item):
    if item not in self.shopping_list:
      self.shopping_list.append(item)

  def remove_item(self, item):
    if item in self.shopping_list:
      self.shopping_list.remove(item)

  def view_list(self):
    print("\nItems in " + str(self.list_name) + '\n' + 30*'-')
    for item in self.shopping_list:
      print(str(item))

  def merge_lists(self, obj):
    
    #Creating a name for our new, merged shopping list
    merged_lists_name = 'Merged List - ' + str(self.list_name) + '+' + str(obj.list_name) 


    # Creating an empty ShoppingList object (**)
    merged_lists_obj = ShoppingList(merged_lists_name)

    # Adding the first shopping list's items to our new list
    merged_lists_obj.shopping_list = self.shopping_list.copy()

    # Adding the second shopping list's items to our new list
    # we're doing this so that there won't be any repeated items
    # in the final list, if both source lists contain common
    # items between each other
    for item in obj.shopping_list:
      merged_lists_obj.shopping_list.append(item)

    # Returning our new, merged object
    return merged_lists_obj

      
# Create an object pet_store_list, and initilize its name
pet_store_list = ShoppingList('Pet Store Shopping List')
grocery_store_list = ShoppingList('Grocery Store List')

# Add the items to the shopping lists
for item in ['dog food', 'frisbee', 'bowl', 'flea collars' ]:
  pet_store_list.add_item(item)

for item in ['fruits' ,'vegetables', 'bowl', 'ice cream']:
  grocery_store_list.add_item(item)

# Remove 'flea collars' using remove_item()
pet_store_list.remove_item('flea collars')

# Add frisbee again using add_item()
pet_store_list.add_item('frisbee')

# Display the entire shopping list through the view_list()
pet_store_list.view_list()

## Testing the merged_lists() method
pet_store_list.merge_lists(grocery_store_list)
## or
grocery_store_list.merge_lists(pet_store_list)

# The second way is from the class itself
merged_list = ShoppingList.merge_lists(pet_store_list, grocery_store_list)

# To check if the your new object is as expected, call the view_list() method
merged_list.view_list()


