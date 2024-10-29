from abc import ABC, abstractmethod
class Absclass(ABC):
    def print(self, x):
        print("passed value : ", x)
    @abstractmethod
    def task(self):
        print("we are inside the abs task")
class testclass(Absclass):
   def task(self):
       print("we are inside testclass task")
testobj = testclass()
testobj.task()
testobj.print(100)