component1={"Engine","Chasis","Radiator","Silencer"}
component2={"Silencer","Petrol Tank","Steering"}
print(component1)
print(component2)
component1.add("Mirror")
print(component1)
#Set methods
print(component1|component2)
print(component1&component2)
print(component1-component2)
print(component2-component1)
#Dictionary methods
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.update({"color": "White"})
print(car)
x = car.items()
print(x)
x = car.keys()
print(x)

"""
{'Chasis', 'Radiator', 'Silencer', 'Engine'}
{'Petrol Tank', 'Steering', 'Silencer'}
{'Chasis', 'Radiator', 'Mirror', 'Silencer', 'Engine'}
{'Steering', 'Mirror', 'Petrol Tank', 'Chasis', 'Radiator', 'Silencer', 'Engine'}
{'Silencer'}
{'Chasis', 'Radiator', 'Mirror', 'Engine'}
{'Petrol Tank', 'Steering'}
{'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'White'}
dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964), ('color', 'White')])
dict_keys(['brand', 'model', 'year', 'color'])
"""
