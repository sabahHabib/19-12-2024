car={"brand":"Toyota",
     "model":"corolla",
     "year":"2023",
     "colors":["red","white","blue"]}
print(car["model"])
print(len(car))
print(type(car))
thisdict=dict(name="john",age="30",country="norway")
x= thisdict.get("name")
print(x)
x=thisdict.keys()
print(x)
x=thisdict.values()
print(x)
x=thisdict.items()
print(x)
if "model" in car:
     print("yes model is in this dictionary")
else:
     print("model is not present")
thisdict.update({"name":"sara"})
print(thisdict)
