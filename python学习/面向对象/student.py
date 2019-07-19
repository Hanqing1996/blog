class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course_name):
        print('%s正在学习%s.' % (self.name, course_name))

    def watch_movie(self):
        if self.age < 18:
            print('%s只能看《熊出没》.' % self.name)
        else:
            print('%s在看《二人转》.' % self.name)

 def main():
    stu1 = Student('无忌', 45)
    stu1.study('python程序设计')
    stu1.watch_movie()

 if __name__ == '__main__':
     main()



