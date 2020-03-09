class LanguageStudent:
    
    def __init__(self):
        self.languages = list()
    
    def add_language(self, language):
        self.languages.append(language)
  
class LanguageTeacher(LanguageStudent):
    
    def teach(self, student, language):
        if language in self.languages:
            student.add_language(language)
            return True
        elif language not in self.languages:
            return False

#To see the output, uncomment the lines below:
teacher = LanguageTeacher()
teacher.add_language('English')
student = LanguageStudent()
teacher.teach(student, 'English')
print(student.languages)