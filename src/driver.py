from src.services.course_service import CourseService
from src.services.employee_service import EmployeeService

from src.controllers.course_controller import CourseController
from src.controllers.registration_controller import RegistrationController

courseController = CourseController(CourseService(),EmployeeService())
registrationController = RegistrationController(CourseService(), EmployeeService())

class Driver(object):

    def ADDCOURSEOFFERING(self, line):
        parameters = line.split()[1:]
        if len(parameters) != 5:
            return "INPUT_DATA_ERROR"
        courseName, instructorName, date, minEmployees, maxEmployees = parameters
        if (not date.isnumeric()) or (not minEmployees.isnumeric()) or (not maxEmployees.isnumeric()) or len(date)!=8:
            return "INPUT_DATA_ERROR"
            
        
        return courseController.addCourse(courseName, instructorName, date, minEmployees, maxEmployees)


    def REGISTER(self, line):
        parameters = line.split()[1:]
        if len(parameters) != 2:
            return "INPUT_DATA_ERROR"
            
        emailId, courseOfferingId = parameters
        if not emailId.endswith('@GMAIL.COM'):
            return "INPUT_DATA_ERROR"
        return registrationController.register(emailId, courseOfferingId)
        

    def ALLOT(self, line):
        parameters = line.split()[1:]
        if len(parameters) != 1:
            return "INPUT_DATA_ERROR"
            return
        courseOfferingId = parameters[0]
        return courseController.alotCourse(courseOfferingId)

    def CANCEL(self, line):
        parameters = line.split()[1:]
        if len(parameters) != 1:
            return "INPUT_DATA_ERROR"
            
        courseRegistrationId = parameters[0]
        return registrationController.deRegister(courseRegistrationId)

    def runApp(self, lines):
        results = []
        for line in lines:
            result = ""
            command = line.split()[0]
            if command == "ADD-COURSE-OFFERING":
                result = self.ADDCOURSEOFFERING(line)
            elif command == "REGISTER":
                result = self.REGISTER(line)
            elif command == "ALLOT":
                result = self.ALLOT(line)
            elif command == "CANCEL":
                result = self.CANCEL(line)
            else:
                result = "INPUT_DATA_ERROR"

            #check for nested list
            if any(isinstance(val, list) for val in result):
                results.extend(result)
            #check is list or not
            else:
                if not isinstance(result, list):
                    result = [result]
                results.append(result)
        return results

    def startApp(self, lines):
    
        results = self.runApp(lines)
        for result in results:
            print(*result)
