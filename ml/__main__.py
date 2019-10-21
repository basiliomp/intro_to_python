from ml.regression import LinearRegression

import sys # A module for making Python talk to the operative system

print(sys.argv) # The 'argv' function returns the file from where we are
				# running the code and the arguments given in the code provided.
print(type(sys.argv)) # This is the resulting list.

square_meters = float(sys.argv[1]) # Second element transformed into float.
print("A house of {}m2".format(square_meters))

model = LinearRegression(square_meters)
model.fit(1, 1)
price = model.predict(square_meters)

print("has a price of {}".format(price))