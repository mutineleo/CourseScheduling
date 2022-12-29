from src.utils.course_utils import CourseUtils


class EmployeeUtils(object):
    GMAIL_DELIMITER = '@'
    ACCEPTED = "ACCEPTED"
    CANCEL_ACCEPTED = "CANCEL_ACCEPTED"
    CANCEL_REJECTED = "CANCEL_REJECTED"
    courseUtils = CourseUtils()


    
    def getCourseNameFromCourseRegistrationId(self, courseRegistrationId):
        return courseRegistrationId[courseRegistrationId.rindex('-')+1:]

    def getEmployeeNameFromCourseRegistrationId(self, courseRegistrationId):
        return courseRegistrationId[courseRegistrationId.index('-')+1:courseRegistrationId.rindex('-')]
    
    def getEmployeeNameFromEmail(self, emailId):
        return emailId[:emailId.index(self.GMAIL_DELIMITER)]

    def getCourseRegistrationId(self, emailId, courseOfferingId):
        employeeName = self.getEmployeeNameFromEmail(emailId)
        courseName = self.courseUtils.getCourseNameFromCourseOfferingId(courseOfferingId)
        return "REG-COURSE-" + employeeName + "-" + courseName
    