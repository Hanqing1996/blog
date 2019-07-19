class Person(object):

    def __init__(self, name, age):
        self._name = name
        self._age = age

    # 访问器 - getter方法
    @property
    def name(self):
        return self._name

    # 访问器 - getter方法
    @property
    def age(self):
        return self._age

    # 修改器 - setter方法
    @age.setter
    def age(self, age):
        self._age=age

def main():
    person=Person('王大锤',20)

    # 访问person的name与age属性
    print(person.name)
    print(person.age)

    # 修改person的age属性
    person.age=22
    # person.name="王小锤" # 报错：AttributeError: can't set attribute

if __name__ == '__main__':
    main()


