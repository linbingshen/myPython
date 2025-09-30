dict1 = {"age":20,"sex":"男","地址":"河南"}
#添加元素
dict1["学号"] = 10086
# print(dict1)
dict1["age"] = 30
# print(dict1)
del dict1["学号"]
# print(dict1)
val1 = dict1.get("age","找不到这个键")
val2 = dict1.get("num","找不到这个键")
print(val1)
print(val2)