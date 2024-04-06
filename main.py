#list of available vehicles for sale
AllowedVehiclesList = [ 'Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan' ]

#while loop
while True:
  #formatting of prompt
  print("********************************")
  print("AutoCountry Vehicle Finder v0.2")
  print("********************************")
  print("Please Enter the following number below from the following menu:\n")

  #client response options
  userInput = input("1. PRINT all Authorized Vehicles\n2. SEARCH for Authorized Vehicles\n3. Exit\n")

#output
  #if user typed "1" 
  if userInput == '1':
    print("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles: ")
    for model in AllowedVehiclesList:
        print(model)
  #if user typed "2"
  elif userInput == '2':
      query = input("Please Enter the full Vehicle name: ")
      found = False
      for model in AllowedVehiclesList:
          if query.lower() == model.lower():
              print(model, "is an authorized vehicle")
              found = True
              #end loop if match is found
              break  
      if not found:
          print(query, "is not an authorized vehicle, if you received this in error please check the spelling and try again")
  #if user typed "3"
  elif userInput == '3':
      print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
      break
  #if user input blank
  else:
      print("You have failed.  Try again.")
  