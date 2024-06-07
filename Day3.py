#Dictionary
data = {1:'keer',2:'kiran',4:'harsh'}

print(data)
print(data[2])

print(data.get(1))
print(data.get(2,'NOT FOUND'))
print(data.get(3,'NOT FOUND'))

keys = ['Navin','kiran','harsh']
values = ['python','java','js']

data1 =dict(zip(keys,values)) #zipping combining 2 values and convert to dict
print(data1)
print(data1['kiran'])

data1['monica'] = 'cs'
print(data1)

del data1['harsh']
print(data1)

#trying to put a list inside a value(python) & putting dict inside dictionary(java)
prog = {'js':'atom','cs':'vs','python':['pycharm','sublime'],
        'java':{'jse':'netbeans','jee':'eclipse'}}
print(prog)
print(prog['js'])
print(prog['python'])
print(prog['python'][1])
print(prog['java'])
print(prog['java']['jee'])