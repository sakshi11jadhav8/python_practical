# Define a class person (attributes:\tname, department, date Of Birth).
# Derive two classes employee(attributes:\temployee id, sal) and
# student(attributes:\tPRN, year, CGPA) from person class.
# Derive two classes lab_assistant(attributes:\tlabs) and
# faculty(attributes:\tsubject, number of research papers, qualification).
# i) Create objects for lab assistant, faculties, and students.
# ii) Display the data.
# iii) Delete a data
# iv) Find the total sal of all employees.
# v) Find average CGPA of students department wise.

class person:
    def __init__(self, name, dep, dob):
        self.name = name
        self.dep = dep
        self.dob = dob

    def __str__(self):
        print('Name:\t', self.name)
        print('Department:\t', self.dep)
        print('Date of birth:\t', self.dob)
        print("")

    def delete(self):
        print("Data deleted for", self.name)
        del self
        print()


class employee(person):
    total_sal = 0

    def __init__(self, name, dep, dob, id, sal):
        super().__init__(name, dep, dob)
        self.id = id
        self.sal = sal
        employee.total_sal += sal

    def totalsal():
        print("Total salary of all employees: Rs.", employee.total_sal)
        print("")

    def display(self):
        print(self.id, '\t', self.name, '\t',
              self.dep, '\t', self.dob, '\t', self.sal)

    def __str__(self):
        print('Name:\t', self.name)
        print('Department:\t', self.dep)
        print('Date of birth:\t', self.dob)
        print('Employee ID:\t', self.id)
        print('Salary:\tRs.', self.sal)
        print("")


class lab_assistant(employee):
    def __init__(self, name, dep, dob, id, sal, labs):
        super().__init__(name, dep, dob, id, sal)
        self.labs = labs

    def display(self):
        print(self.id, '\t', self.name, '\t', self.dep, '\t',
              self.dob, '\tRs.', self.sal, '\t', self.labs)

    def __str__(self):
        print('Faculty name:\t', self.name)
        print('Department:\t', self.dep)
        print('Date of birth:\t', self.dob)
        print('Employee ID:\t', self.id)
        print('Salary:\t\tRs.', self.sal)
        print('Labs:\t', self.labs)


class faculty(employee):
    def __init__(self, name, dep, dob, id, sal, sub, no_rp, qual):
        super().__init__(name, dep, dob, id, sal)
        self.sub = sub
        self.no_rp = no_rp
        self.qual = qual

    def display(self):
        print(self.id, '\t', self.name, '\t', self.dep, '\t', self.dob, '\tRs.',
              self.sal, '\t', self.sub, '\t\t', self.no_rp, '\t\t\t', self.qual)

    def __str__(self):
        print('Faculty name:\t', self.name)
        print('Department:\t', self.dep)
        print('Date of birth:\t', self.dob)
        print('Employee ID:\t', self.id)
        print('Salary:\t\tRs.', self.sal)
        print('Subject:\t', self.sub)
        print('No. of research papers:\t', self.no_rp)
        print('Qualifications:\t', self.qual)
        print()


class student(person):
    comp_cgpa, it_cgpa, mech_cgpa = 0, 0, 0
    comp, it, mech = 0, 0, 0

    def __init__(self, name, dep, dob, prn, yr, cgpa):
        super().__init__(name, dep, dob)
        self.prn = prn
        self.yr = yr
        self.cgpa = cgpa
        if dep == "Computer":
            student.comp_cgpa += cgpa
            student.comp += 1
        elif dep.strip() == "IT":
            student.it_cgpa += cgpa
            student.it += 1
        elif dep == "Mechanical":
            student.mech_cgpa += cgpa
            student.mech += 1

    def avg_cgpa():
        print("Average CGPA of students department-wise:")
        print("Computer:\t", student.comp_cgpa/student.comp)
        print("IT:\t\t", student.it_cgpa/student.it)
        print("Mechanical:\t", student.mech_cgpa/student.mech)
        print()

    def display(self):
        print(self.prn, '\t', self.name, '\t', self.dep, '\t',
              self.dob, '\t', self.yr, '\t\t', self.cgpa)

    def __str__(self):
        print('Student name:\t', self.name)
        print('Department:\t', self.dep)
        print('Date of birth:\t', self.dob)
        print('PRN:\t', self.prn)
        print('Year:\t', self.yr)
        print('CGPA:\t', self.cgpa)
        print()

# i) Create objects for lab assistant, faculties, and students.


l1 = lab_assistant("Arpit Sharma", "Computer",
                   "23/3/1992", "3265", 20000, "OS")
l2 = lab_assistant("Kushal Mane", "Computer",
                   "14/6/1987", "3532", 18000, "Python")
l3 = lab_assistant("Pushpa Patel", "Computer",
                   "20/12/1985", "5624", 19000, "DAA")

lab = [l1, l2, l3]

f1 = faculty("Kailash Vora", "Computer", "23/1/1978",
             "5411", 90000, "OS\t", 5, "PhD")
f2 = faculty("Pranab Singh", "Computer", "17/4/1981",
             "2465", 70000, "Python", 4, "M.Tech")
f3 = faculty("Kalyani Ghosh", "Computer", "6/11/1988",
             "1254", 60000, "DAA\t", 3, "M.Tech")

fac = [f1, f2, f3]

s1 = student("Ruchi Panchal", "Computer", "7/2/2003",
             "2130331245000", "1st", 8.77)
s2 = student("Sapna Shroff", "Computer", "26/3/2002",
             "2030331245034", "2nd", 9.67)
s3 = student("Aruna Dhar", "Computer", "15/4/2001",
             "1930331245076", "3rd", 7.72)
s4 = student("Krishna Arora", "Computer", "12/5/1999",
             "1830331245011", "4th", 8.23)
s5 = student("Raj Rao", "IT\t", "25/6/2003",
             "2130331245021", "1st", 9.27)
s6 = student("Namita Kaul", "IT\t", "15/8/2002",
             "2030331245021", "2nd", 8.26)
s7 = student("Ram Bose", "Mechanical", "18/4/2001",
             "1930331245089", "3rd", 7.22)
s8 = student("Ritika Chand", "Mechanical", "2/7/1999",
             "1830331245045", "4th", 9.13)

students = [s1, s2, s3, s4, s5, s6, s7, s8]


# ii) Display the data.
print("Employees:")
print("Lab assistants:")
print('ID\t', 'Name\t\t', 'Department\t',
      'Date of birth\t', 'Salary\t\t', 'Labs\t')
for i in lab:
    i.display()
print()


print("Faculty:")
print('ID\t', 'Name\t\t', 'Department\t', 'Date of birth\t', 'Salary\t\t',
      'Subject\t', 'No. of research papers\t', 'Qualification')
for i in fac:
    i.display()
print()


print("Students:")
print('PRN\t\t', 'Name\t\t', 'Department\t',
      'Date of birth\t', 'Year\t\t', 'CGPA\t')
for i in students:
    i.display()
print()


# iii) Delete a data
s1.delete()
f2.delete()


# iv) Find the total sal of all employees.
print(employee.totalsal())


# v) Find average CGPA of students department wise.
print(student.avg_cgpa())
