class Vegetable:
  def __init__(self, name,price,quantity):
    self.name = name
    self.price = price
    self.quantity = quantity


class Store:
  def __init__(self, storeName,vegList):
    self.storeName = storeName
    self.vegList = vegList
  
  def categorizeVegetablesAlphabetically(self):
    vegDict = {}

    for i in self.vegList:
      if i.name[0] not in vegDict:
        vegDict[i.name[0]] = []
      vegDict[i.name[0]].append(i.name)
      for j in sorted(vegDict.keys()):
        print(j)
        for k in sorted(vegDict[j]):
          print(k)

  def filterVegetablesForPriceRange(self, min, max):
    l = []
    for i in self.vegList:
      if i.price >= min and i.price <= max:
        l.append(i.name)
      
      if l:
        for j in sorted(l):
          print(j)
      else:
        print('No Vegetable(s) in the given price range')


if __name__ == '__main__':
  count = int(input())
  vegList = []
  for i in range(count):
    name = input()
    price = float(input())
    quantity = int(input())
    vegList.append(Vegetable(name, price, quantity))

  storeName = input()
  min = float(input())
  max = float(input())

  s = Store(storeName, vegList)
  s.categorizeVegetablesAlphabetically()
  s.filterVegetablesForPriceRange(min, max)
