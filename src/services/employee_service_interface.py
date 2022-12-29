import abc
class EmployeeServiceInterface(metaclass = abc.ABCMeta):
    @abc.abstractmethod
    def addCourse(self, emailId, courseOfferingId):
        pass

    @abc.abstractmethod
    def removeCourse(self, courseRegistrationId):
        pass
