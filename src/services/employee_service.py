from src.models.employee import Employee
from src.services.employee_service_interface import EmployeeServiceInterface
from src.utils.course_utils import CourseUtils
from src.utils.employee_utils import EmployeeUtils

class EmployeeService(EmployeeServiceInterface):
    employeeDetails = {}
    employeeUtils = EmployeeUtils()
    def addCourse(self, emailId, courseOfferingId):
        employee = Employee()
        employee.setEmailId(emailId)
        employee.setCourse(courseOfferingId)
        employee.setCourseRegistrationId(self.employeeUtils.getCourseRegistrationId(emailId, courseOfferingId))
        self.__class__.employeeDetails[employee.getCourseRegistrationId()] = employee
        return employee.getCourseRegistrationId()

    def removeCourse(self, courseRegistrationId):
        self.__class__.employeeDetails.pop(courseRegistrationId)
    
    def getEmailId(self, courseRegistrationId):
        return self.__class__.employeeDetails[courseRegistrationId].getEmailId()

    def getCourseOfferingId(self, courseRegistrationId):
        return self.__class__.employeeDetails[courseRegistrationId].getCourse()