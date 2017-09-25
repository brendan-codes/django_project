from system.core.controller import *

class Courses(Controller):
    def __init__(self, action):
        super(Courses, self).__init__(action)
        self.load_model('CoursesModel')
    def index(self):
        courses = self.models['CoursesModel'].getAllCourses()
        # print "passing to index", courses
        return self.load_view('index.html', courses=courses)
    def addCourse(self):
        # print request.form
        courseDetails = {
            "name": request.form['name'],
            "description": request.form['description']
        }
        # print courseDetails
        test = self.models['CoursesModel'].addCourse(courseDetails)
        session['user_id'] = test
        return redirect('/')
    def delete(self, id):
        print "returning id: ", id
        deleted_course = self.models['CoursesModel'].destroy(id)
        print "course delete: ", deleted_course
        return redirect('/')
