class Human:
    def __init__(self, name=None, familyname=None, age=None, gender=None, nationality=None):
        self.__name = name
        self.__familyname = familyname
        self.__age = age
        self.__gender = gender
        self.__nationality = nationality

    def set_name(self, name):
        self.__name = name
        pass

    def set_family(self, familyname):
        self.__familyname = familyname
        pass

    def set_age(self, age):
        self.__age = age
        pass

    def set_gender(self, gender):
        self.__gender = gender
        pass

    def set_nationality(self, nationality):
        self.__nationality = nationality
        pass

    def get_info(self):
        info = dict(name=self.__name, familyname=self.__familyname, age=self.__age, gender=self.__gender,
                    nationality=self.__nationality)
        return info


class Student(Human):
    def __init__(self, name=None, familyname=None, age=None, gender=None, nationality=None, school=None, subjects=None):
        super().__init__(name, familyname, age, gender, nationality)
        self.__school = school
        self.subjects = [] if subjects is None else subjects

    def set_school(self, school):
        self.__school = school
        pass

    def add_subject(self, subject=None):
        self.subjects.append(subject)

    def get_student(self):
        student = self.get_info()
        student["school"] = self.__school
        student["subjects"] = self.subjects
        return student


class Teacher(Human):
    def __init__(self, name=None, familyname=None, age=None, gender=None, nationality=None, school=None, subjects=None):
        super().__init__(name, familyname, age, gender, nationality)
        self.__school = school
        self.subjects = [] if subjects is None else subjects

    def set_school(self, school):
        self.__school = school
        pass

    def add_subject(self, subject=None):
        self.subjects.append(subject)

    def get_teacher(self):
        teacher = self.get_info()
        teacher["school"] = self.__school
        teacher["subjects"] = self.subjects
        return teacher


if __name__ == 'education.users':
    print('Module users is successfully imported')

if __name__ == '__main__':
    classes = [class_name for class_name in dir() if not class_name.startswith("_")]
    methods = dict(Human=[method_name for method_name in dir(Human) if not method_name.startswith("_")],
                   Student=[method_name for method_name in dir(Student) if not method_name.startswith("_")],
                   Teacher=[method_name for method_name in dir(Teacher) if not method_name.startswith("_")])
    print('Module users contains the following classes with its methods:')
    for class_name in classes:
        if class_name in methods:
            print(f'{class_name}: {", ".join(methods[class_name])}')
