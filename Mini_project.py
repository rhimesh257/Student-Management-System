class Person:
  def __init__(self,name,age):
    self.name = name
    self.age = age

class Student(Person):
  def __init__(self,name,age,student_id,course,marks):
    super().__init__(name,age)
    self.student_id = student_id
    self.course = course
    self.marks = marks

  def display(self):
    print("-" * 40)
    print(f"Name: {self.name}")
    print(f"Age: {self.age}")
    print(f"Student ID: {self.student_id}")
    print(f"Course: {self.course}")
    print(f"Marks: {self.marks}")
    print("-" * 40)

  def total(self):
   return sum(self.marks)

  def average(self):
    return self.total()/len(self.marks)

  def grade(self):
    avg = self.average()

    if avg >= 90:
      return "B"

    elif avg >= 75:
      return "B"
    elif avg >= 60:
      return "C"
    else:
     return "Fail"


students = []
def add_student():
 student_id = int(input("Enter student ID: "))
 name = input("Enter student Name: ")
 age = input("Enter Age: ")
 course = input("Enter Course: ")
 marks = []
 for i in range(3):
     mark = int(input(f"Enter subject {i+1} Marks: "))
     marks.append(mark)
 student = Student(name, age, student_id, course, marks)
 students.append(student)
 print("Student added succesfully")

def viewStudents():
  if len(students) == 0:
    print("No Students Available")
  else:
     for students in students:
         Student.display()

def searchstudent():
    sid = int(input("Enter Student ID: "))

    for student in students:
      if student.student_id == sid:
        print("Student Found")
        student.display()
        break
      else:
          print("Student not found")

def updateMarks():
        sid = int(input("Enter Student ID: "))
        for student in students:
          if student.student_id == sid:

            new_marks = []

            for i in range(3):
              mark = int(input(f"Enter New Subject {i+1} Marks: "))
              new_marks.append(mark)

              student.marks = new_marks
              print("Marks Updated Successfully")
              break
        else:
                print("Student not Found")

def delete_Student():
            sid = int(input("Enter Student ID: "))

            for student in students:
              if student.student_id == sid:
                students.remove(student)
                print("Student Deleted Successfully")
                break
              else:
                   print("Student Not Found")
def calculate_result():
              sid = int(input("Enter Student ID: "))

              for student in students:
                if student.student_id == sid:
                  print("\nStudent Result")
                  print(f"Name: {student.name}")
                  print(f"Total Marks: {student.totsl()}")
                  print(f"Average Marks: {student.average()}")
                  print(f"Grade: {student.grade()}")
                  break
                else:
                    print("Student Not FOund")
def displayTopper():
                if len(students) == 0:
                  print("NO Toppers")
                  return
                topper = students[0]

                for student in students:
                  if student.average() > topper.average():
                    topper = student
                print("\nClass Topper")
                print(f"Name: {topper.name}")
                print(f"Average: {topper.average()}")

def displayFailedstudents():
            if len(students) == 0:
                print("NO failures available")
                return
                found = False
            for student in students:
              if student.average() < 60:
                  print(student.name)
                  found = True
                  break
                  if not found:
                    print("N0 Failed Students")
def totalstudentcount():
                 print(f"Total Students Count: {len(students)}")
while True:
                print("\n")
                print("="*40)
                print("Student Management System")
                print("="*40)

                print("1. Add Student")
                print("2. View All Students")
                print("3. Search Student")
                print("4. Update Marks")
                print("5. Delete Student")
                print("6.Calculate Result")
                print("7. Display Topper")
                print("8. Display Failed Students")
                print("9. Total Student Count")
                print("10. Exit")

                choice = int(input("Enter Your Choice: "))

                if choice == 1:
                  add_student()
                elif choice == 2:
                  viewStudents()
                elif choice == 3:
                  searchstudent()
                elif choice == 4:
                  updateMarks()
                elif choice == 5:
                  delete_Student()
                elif choice == 6:
                  calculate_result()
                elif choice == 7:
                  displayTopper()
                elif choice == 8:
                  displayFailedstudents()
                elif choice == 9:
                  totalstudentcount()
                elif choice == 10:
                  print("Thank You")
                  break
                else:
                  print("Invalid Choice")
