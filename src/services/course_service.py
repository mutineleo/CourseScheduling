from src.models.course import Course
from src.services.course_service_interface import CourseServiceInterface
from src.utils.course_utils import CourseUtils
from src.utils.employee_utils import EmployeeUtils

class CourseService(CourseServiceInterface):
    courseDetails = {}
    employeeUtils = EmployeeUtils()
    courseUtils = CourseUtils()
    def addCourse(self, title, instructor, date, minEmployee, maxEmployee):
        course = Course()
        course.setTitle(title)
        course.setInstructor(instructor)
        course.setDate(date)
        course.setMinEmployee(minEmployee)
        course.setMaxEmployee(maxEmployee)
        course.setCourseOfferingId(self.courseUtils.getCourseOfferingId(title, instructor))
        self.__class__.courseDetails[course.getCourseOfferingId()] = course
        return course.getCourseOfferingId()

    def alotCourse(self, courseOfferingId):
        course = self.__class__.courseDetails[courseOfferingId]
        course.setAlloted()
        if course.getNoOfEmployees() < course.getMinEmployee():
            self.__class__.courseDetails[courseOfferingId] = course
            return False, course
        else:
            self.__class__.courseDetails[courseOfferingId] = course
            return True, course
    
    def register(self, emailId, courseOfferingId):
        course = self.__class__.courseDetails[courseOfferingId]
        if course.getNoOfEmployees() == course.getMaxEmployee():
            return False
        else:
            courseRegistrationId = self.employeeUtils.getCourseRegistrationId(emailId, courseOfferingId)
            course.addEmployee(courseRegistrationId)
            self.__class__.courseDetails[courseOfferingId] = course
            return True
    
    def deRegister(self, courseRegistrationId, courseOfferingId):
        if self.__class__.courseDetails[courseOfferingId].getAlloted() == True:
            return False
        else:
            self.__class__.courseDetails[courseOfferingId].removeEmployee(courseRegistrationId)
            return True
    