@@ -0,0 +1,29 @@
class Person:
    def __init__(self, name, surname, qualification=1):
        self.name = name
        self.surname = surname
        self.qualification = qualification
    def __del__(self):
        print("Данный сотрудник:", self.name, self.surname, "уволен из компании.")
    def info(self):
        return "{} {}, {}".format(self.name, self.surname, self.qualification)
worker = Person("Владимир", "Босов", 10)
helper = Person("Михаил", "Галилов", 7)
maker = Person("Никита", "Хомяков", 2)
print(worker.info())
print(helper.info())
print(maker.info())
if helper.qualification < worker.qualification and helper.qualification < maker.qualification:
    del helper
elif worker.qualification < helper.qualification and worker.qualification < maker.qualification:
    del worker
else:
    del maker
input()
