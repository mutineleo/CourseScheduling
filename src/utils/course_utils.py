class CourseUtils(object):
    COURSE_FULL_ERROR = "COURSE_FULL_ERROR"
    COURSE_CONFIRMED = "CONFIRMED"
    COURSE_CANCELED = "COURSE_CANCELED"
    

    def getCourseNameFromCourseOfferingId(self, courseOfferingId):
        return courseOfferingId[courseOfferingId.index('-')+1:courseOfferingId.rindex('-')]
    
    def getInstructorNameFromCourseOfferingId(self, courseOfferingId):
        return courseOfferingId[courseOfferingId.rindex('-')+1:]
    
    def getCourseOfferingId(self, title, instructor):
        return "OFFERING" + "-" + title + "-" + instructor