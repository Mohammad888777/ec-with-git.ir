a=[{"name":"mohammad","id":1},{"name":"mohammad","id":2},{"name":"mohammad","id":3},{"name":"mohammad","id":4}]
print([{k:d[k] for k in d if d.get('id')!=2 } for d  in a])

print(list(filter(lambda x: x.get("id")!=2 ,a)))