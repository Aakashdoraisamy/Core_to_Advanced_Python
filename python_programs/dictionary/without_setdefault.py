d = {'name':['Batman','Captain America'],'Marks':[99,99]}
new_key = 'name'
new_value = ['Batman','Captain America','Spiderman']
if new_key not in d:
    d[new_key] = new_value
print(d) 
# dictionary not changed when there is existing