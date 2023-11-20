element1={"Foundation","Columns","Walls","Beams"}
element2={"Concrete-Slab","Parapet","Door-Frame","Foundation"}
print(element1)
print(element2)
element1.add("Window-frame")
print(element1)
#Set methods
print(element1|element2)
print(element1&element2)
print(element1-element2)
print(element2-element1)
#Dictionary methods
building={
  "Cement-Brand":"RAMCO",
  "Brick-Type":"Burnt-claybricks",
  "Beam-Company":"AGNI-Steels"
}
building.update({"BrickType":"Sand-Lime Bricks"})
print(building)
x = building.items()
print(x)
x = building.keys()
print(x)

"""
{'Columns', 'Beams', 'Walls', 'Foundation'}
{'Parapet', 'Door-Frame', 'Concrete-Slab', 'Foundation'}
{'Beams', 'Walls', 'Window-frame', 'Columns', 'Foundation'}
{'Parapet', 'Beams', 'Walls', 'Door-Frame', 'Window-frame', 'Columns', 'Foundation', 'Concrete-Slab'}
{'Foundation'}
{'Window-frame', 'Columns', 'Beams', 'Walls'}
{'Parapet', 'Door-Frame', 'Concrete-Slab'}
{'Cement-Brand': 'RAMCO', 'Brick-Type': 'Burnt-claybricks', 'Beam-Company': 'AGNI-Steels', 'BrickType': 'Sand-Lime Bricks'}
dict_items([('Cement-Brand', 'RAMCO'), ('Brick-Type', 'Burnt-claybricks'), ('Beam-Company', 'AGNI-Steels'), ('BrickType', 'Sand-Lime Bricks')])
dict_keys(['Cement-Brand', 'Brick-Type', 'Beam-Company', 'BrickType'])
"""
