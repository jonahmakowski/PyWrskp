class Student:
    role = "learn"
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
class Teacher:
    role = "teach"
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

class School:
    roster = []
    def __init__(self, school_name):
        self.school_name = school_name
    
    def add_members(self):
        name = input('What is their name  ')
        is_student = input('Are they a student? (y/n)')
        if is_student == 'y':
            grade = input('What grade are they in?  ')
            new_member = Student(name, grade)
        else:
            subject = input('What do they teach?  ')
            new_member = Teacher(name, subject)
        self.roster.append(new_member)
        if input('Add another member? (y/n)  ') == 'y':
            self.add_members()
    def show_roster(self):
        for member in self.roster:
            if isinstance(member, Teacher):
                print('{} is a teacher, they teach {}'.format(member.name, member.subject))
            elif isinstance(member, Student):
                print('{} is a student, they are in grade {}'.format(member.name, member.grade))
class School_board:
    schools = []
    def __init__(self, loc, board_name):
        self.loc = loc
        self.board_name = board_name
    def add_schools(self, school_v, other_schools):
        school_name = input('Is ' + school_v.school_name + ' the school you want to add? (y/n)')
        if school_name == 'y':
            school_name = school_v.school_name
        elif school_name == 'n':
            name = input('What school would you like?')
            for i in range (len(other_schools)):
                if name == other_schools[i]:
                    school_name = other_schools[i]
                    break
        self.schools.append(school_name)
        new = input('Would you like to add a new school? (y/n)')
        if new == 'y':
            self.add_schools(school_v, other_schools)
    def show_schools(self):
        for i in self.schools:
            print(i)


brookdale = School('brookdale')

pine_grove = School('pine_grove')

schools = [brookdale, pine_grove]

halton = School_board('Halton', 'Halton school board (HDSB)')
brookdale.add_members()
pine_grove.add_members()
halton.add_schools(brookdale, schools)