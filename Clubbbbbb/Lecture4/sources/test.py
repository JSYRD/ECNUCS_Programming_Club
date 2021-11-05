class Human():
    def __init__(self,name,age):
        self.name = name
        self.age = age

Dongdong = Human("Dongdong", 18)
Dongdong.name = "Wangfeng"
print(Dongdong.name)