def print_params (a =1,b = "String", c = True):
    print(a,b,c)

print_params()
print_params(a = 3, b = 4)
print_params(c = "Hello")
print_params(b = 25)
print_params(c = [1,2,3])
values_list = ["Stroka", 100, False]
value_dict = {"a": 45.32, "b": False , "c": "Привет!"}
print_params(*values_list)
print_params(**value_dict)
values_list_2 = [1, 5.1]
print_params(*values_list_2, 42)