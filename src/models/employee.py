class Employee(object):
    def __init__(self):
        self.emailId = None
        self.courseOfferingId = None
        self.courseRegistrationId = None
    
    def setEmailId(self, emailId):
        self.emailId = emailId
    
    def setCourse(self, courseOfferingId):
        self.courseOfferingId = courseOfferingId
    
    def getEmailId(self):
        return self.emailId
    
    def getCourse(self):
        return self.courseOfferingId
    
    def setCourseRegistrationId(self, courseRegistrationId):
        self.courseRegistrationId = courseRegistrationId
    
    def getCourseRegistrationId(self):
        return self.courseRegistrationId