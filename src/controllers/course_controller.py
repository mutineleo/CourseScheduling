
from src.models import employee
from src.utils.course_utils import CourseUtils


class CourseController(object):
    def __init__(self, courseService, employeeService):
        self.courseService = courseService
        self.employeeService = employeeService
    
    def addCourse(self, title, instructor, date, minEmployee, maxEmployee):
        return self.courseService.addCourse(title, instructor, date, minEmployee, maxEmployee)
    
    def alotCourse(self, courseOfferingId):
        
        isAlloted, course =  self.courseService.alotCourse(courseOfferingId)
        allotStatus = ""
        if isAlloted:
            allotStatus = CourseUtils.COURSE_CONFIRMED
        else:
            allotStatus = CourseUtils.COURSE_CANCELED
        course_name = course.getTitle()
        instructor = course.getInstructor()
        date = course.getDate()
        employeeList = course.getEmployees()
        employeeList.sort()
        employeeCourseDetails = []
        for registrationId in employeeList:
            emailId = self.employeeService.getEmailId(registrationId)
            employeeCourseDetails.append([registrationId, emailId, courseOfferingId, course_name, instructor, date, allotStatus])
        return employeeCourseDetails


    