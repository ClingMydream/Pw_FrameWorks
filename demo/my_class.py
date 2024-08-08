
# 定义一个类,类的名称必须是大写
class Human:
    # 构造方法
    def __init__(self, name, sex, age):
        # 实例
        self.name = name
        self.sex  = sex
        self.age = age
        self.birthday = 2024-age
    def run(self):
        print(f"{self.name} is running")
    def join(self):
        if self.age < 345:
            print(f"{self.name}还能找到工作")
        else:
            print(f"{self.name}已经不好找工作了")


# 类得继承
class Tester(Human):
    # 构造方法
    def __init__(self,name, sex, age,tech):
        super().__init__(name, sex, age)
        self.tech = tech
    def skiing(self):
        print(f"{self.name}会{self.tech}")

#使用 if __name__ == '__main__': 可以使模块既可以作为可重用的库，也能作为独立的程序执行。
if __name__ == '__main__':
    # 实例化
    zhangsan = Human("张三","男",28)
    zhangsan.run()
    zhangsan.join()

    liubawang = Tester("六八王","女",16,"永劫无间")
    liubawang.run()
    liubawang.join()
    liubawang.skiing()