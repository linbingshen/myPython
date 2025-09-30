
# 传递列表
def greeta_user(names):
    for name in names:
        msg = f"hello ,{name.title()}!"
        print(msg)

usernames = ["hannah","ty","margot"]
# greeta_user(usernames)

#传递任意数量的实参
def print_infors(*element):
    print(element)

print_infors(423,2432242,"niahia","n奶好")

#函数的参数同时有位置实参和任意数量实参时
#必须要把任意数量实参放在后面
def text02(el,*el2):
    print(el)
    print(el2)

text02('text',32,"aa","啊啊")