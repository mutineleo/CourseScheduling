import abc
class CourseServiceInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def addCourse(self, title, instructor, date, minEmployee, maxEmployee):
        pass

    @abc.abstractmethod
    def alotCourse(self, title):
        pass

    @abc.abstractmethod
    def register(self, name, title):
        pass

    @abc.abstractmethod
    def deRegister(self, name, title):
        pass

