class FoodItem:

  def __init__(self, item_id, item_name, item_category, item_price):
    self.item_id = item_id
    self.item_name = item_name
    self.item_category = item_category
    self.item_price = item_price

  def provideDiscount(self, percentDiscount):
    return (self.item_price - ((self.item_price*percentDiscount)/100)

class Restaurant:

  def __init__(self, restaurant_name, fooditem_list):
    self.restaurant_name = restaurant_name
    self.fooditem_list = fooditem_list

  def retrieveUpdatedPrice(self, updatedPercent, item_id):
    
    itemFound = False
    if updatePercent > 0:
      for i in self.fooditem_list:
        if i.item_id == item_id:
          itemFound = True
          updatedPrice = i.provideDiscount(updatedPercent)
          print(i.item_name + '-' + str(updatedPrice))
    else:
      for i in self.fooditem_list:
        if i.item_id == item_id:
          itemFound = True
          print(item_name + '-' + str(item_price))
    if itemFound == False:
      print('Item not found')

if __name__ == '__main__':

  foodnumber = int(input())
  fooditem_list = []
  for i in range(foodnumber):
    item_id = int(input())
    item_name = input()
    item_category = input()
    item_price = int(input())

    fooditem_list.append(FoodItem(item_id, item_name, item_category, item_price))

  res = Restaurant('GuruKripa', fooditem_list)
  item_id = int(input())
  updatedPercent = int(input())
  res.retrieveUpdatedPrice(item_id, updatedPercent)
