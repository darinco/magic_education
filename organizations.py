import csv


class School:
    def __init__(self, name=None, address=None, phone=None, email=None, num_stud=None, num_teachers=None):
        self.__name = name
        self.__address = address
        self.__phone = phone
        self.__email = email
        self.students = []
        self.teachers = []
        self.__num_stud = len(self.students)
        self.__num_teachers = len(self.teachers)

    def set_name(self, name):
        self.__name = name
        pass

    def set_address(self, address):
        self.__address = address
        pass

    def set_phone(self, phone):
        self.__phone = phone
        pass

    def set_email(self, email):
        self.__email = email
        pass

    def set_num_stud(self, num_stud):
        self.__num_stud = num_stud
        pass

    def set_num_teachers(self, num_teachers):
        self.__num_teachers = num_teachers
        pass

    def add_student(self, student):
        self.students.append(student)
        self.__num_stud += 1

    def add_teacher(self, teacher):
        self.teachers.append(teacher)
        self.__num_teachers += 1

    def get_info(self):
        return dict(name=self.__name, address=self.__address, phone=self.__phone, email=self.__email,
                    num_stud=self.__num_stud, num_teachers=self.__num_teachers)

    def get_report(self):
        with open(str(self.__name) + '_report.csv', 'w', newline='') as file:
            writer = csv.writer(file)

            writer.writerow(["SCHOOL INFORMATION", ])
            data = self.get_info()
            csv.DictWriter(file, data).writeheader()
            writer.writerow([data['name'], data['address'], data['phone'], data['email'], data['num_stud'], data['num_teachers']])

            writer.writerow(["TEACHERS", ])
            head = ['name', 'familyname', 'age', 'gender', 'nationality', 'school', 'subjects']
            csv.DictWriter(file, head).writeheader()
            for row in self.teachers:
                writer.writerow([row['name'], row['familyname'], row['age'], row['gender'], row['nationality'],
                                row['school'], row['subjects']])

            writer.writerow(["LIST OF STUDENTS", ])
            csv.DictWriter(file, head).writeheader()
            for row in self.students:
                writer.writerow([row['name'], row['familyname'], row['age'], row['gender'], row['nationality'],
                                row['school'], row['subjects']])


if __name__ == 'education.organizations':
    print('Module organizations is successfully imported')

if __name__ == '__main__':
    classes = [class_name for class_name in dir() if not class_name.startswith("_")]
    methods = dict(School=[method_name for method_name in dir(School) if not method_name.startswith("_")])
    print('Module organizations contains the following classes with methods:')
    for class_name in classes:
        if class_name in methods:
            print(f'{class_name}: {", ".join(methods[class_name])}')
