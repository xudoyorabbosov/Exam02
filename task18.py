numbers =[{'value': 2}, {'value': 3}, {'value': 4}]
squares = list(map(lambda x : {'value': x['value']**2}, numbers))
print(squares)