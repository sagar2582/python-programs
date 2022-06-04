test_str = 'Gfg is best . Geeks are good and Geeks like Gfg'

res = {key: test_str.count(key) for key in test_str.split()}
print(res)