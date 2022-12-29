class Course(object):
    def __init__(self):
        self.title = None
        self.instructor = None
        self.date = None
        self.minEmployee = 0
        self.maxEmployee = 0
        self.employees = list()
        self.noOfEmployees = 0
        self.courseOfferingId = None
        self.alloted = False

    def setTitle(self,title):
        self.title = title
    
    def getTitle(self):
        return self.title
    
    def setInstructor(self, instructor):
        self.instructor = instructor
    
    def getInstructor(self):
        return self.instructor
    
    def setDate(self, date):
        self.date = date
    
    def getDate(self):
        return self.date
    
    def setMinEmployee(self, minEmployee):
        self.minEmployee = int(minEmployee)
    
    def getMinEmployee(self):
        return self.minEmployee
    
    def setMaxEmployee(self, maxEmployee):
        self.maxEmployee = int(maxEmployee)
    
    def getMaxEmployee(self):
        return self.maxEmployee

    def addEmployee(self, courseRegistrationId):
            self.noOfEmployees += 1
            self.employees.append(courseRegistrationId)
    
    def removeEmployee(self, courseRegistrationId):
        self.noOfEmployees -= 1
        self.employees.remove(courseRegistrationId)
    
    def getNoOfEmployees(self):
        return self.noOfEmployees
    
    def getEmployees(self):
        return self.employees
    
    def setCourseOfferingId(self, courseOfferingId):
        self.courseOfferingId = courseOfferingId
    
    def getCourseOfferingId(self):
        return self.courseOfferingId
    
    def setAlloted(self):
        self.alloted = True
    
    def getAlloted(self):
        return self.alloted
    