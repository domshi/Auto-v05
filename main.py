#just looking at the txt file
def read():
  with open('Vehicles.txt', 'r') as db:
    return db.read()

#looking and adding to the txt file
def write(obj):
  with open('Vehicles.txt', 'a') as db:
    return db.write('\n' + obj)

#deleteing entry ??? to be continued
def delete(obj):
  with open('Vehicles.txt', 'w') as db:
    return db.write(db


while (True):
  print(" ")
  print("********************************")
  print("AutoCountry Vehicle Finder v0.4")
  print("********************************")
  print("Please Enter one of the following numbers below from the following menu:")
  print(" ")
  print('1. PRINT all Authorized Vehicles')
  print('2. SEARCH for Authorized Vehicle')
  print('3. ADD Authorized Vehicle')
  print('4. DELETE Authorized Vehicle')
  print('5. Exit')
  selection = input("Please enter your choice: ")
  print(" ")
  if not selection.isnumeric():
    print("Invalid Choice,Please select a valid choice from the menu")
    continue
  if int(selection) == 1:
    print('The AutoCountry sales manager has authorized the purchase and selling of the following vehicles: ')
    print(read())
    continue
  if int(selection) == 2:
    read()
    vehicleChoice = input('Please Enter the full Vehicle name: ')
    if vehicleChoice in read():
      print((vehicleChoice) + ' is an authorized vehicle')
    if vehicleChoice not in read():
      print((vehicleChoice) + ' is not an authorized vehicle, if you received this in error please check the spelling and try again')
    continue
  if int(selection) == 3:
    read()
    vehicleAdd = input('Please Enter the full Vehicle name you would like to add: ')
    if vehicleAdd in read():
      print((vehicleAdd) + ' is already an authorized vehicle')
    if vehicleAdd not in read():
      write(vehicleAdd)
      print('You have added ' + (vehicleAdd) + ' to the authorized vehicle list')
    continue
  if int(selection) == 4:
    vehicleDelete = input('Please Enter the full Vehicle name you would like to REMOVE: ')
    read()
    if vehicleDelete not in read():
      print((vehicleDelete) + ' is not an authorized vehicle')
    
    
    if vehicleDelete in read():
      confirmDelete = input('Are you sure you want to remove "' + (vehicleDelete) + '" from the Authorized Vehicles List? (Yes/No): ')
      if confirmDelete == 'No':
        continue
      if confirmDelete != 'Yes':
        print('Please enter Yes or No')
      if confirmDelete == 'Yes':
        
        
        delete(vehicleDelete)
        print('You have REMOVED "' + (vehicleDelete) + '" from the Authorized Vehicle List')
    continue
  if int(selection) != 5:
    print("Invalid Choice,Please select a valid choice from the menu")
    continue
  if int(selection) == 5:
    print('Thank you for using the AutoCountry Vehicle Finder, good-bye!')
    break

