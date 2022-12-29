from src.utils.course_utils import CourseUtils
from src.utils.employee_utils import EmployeeUtils

class RegistrationController(object):
    def __init__(self, courseService, employeeService):
        self.courseService = courseService
        self.employeeService = employeeService

    def register(self, emailId, courseOfferingId):
        
        isRegistered = self.courseService.register(emailId, courseOfferingId)
        if not isRegistered:
            return CourseUtils.COURSE_FULL_ERROR
        else :
            return [self.employeeService.addCourse(emailId, courseOfferingId), EmployeeUtils.ACCEPTED]

    
    def deRegister(self, courseRegistrationId):
        
        courseOfferingId = self.employeeService.getCourseOfferingId(courseRegistrationId)
        isRegistrationCancelled =  self.courseService.deRegister(courseRegistrationId, courseOfferingId)
        if isRegistrationCancelled:
            self.employeeService.removeCourse(courseRegistrationId)
            return [courseRegistrationId, EmployeeUtils.CANCEL_ACCEPTED]
        else:
            return [courseRegistrationId, EmployeeUtils.CANCEL_REJECTED]

