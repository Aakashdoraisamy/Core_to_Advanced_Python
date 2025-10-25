"""

### Inheritance

    one class can inherit the properties and methods from the parent class

## Types of Inheritance:-
    - single level inheritance
    - multi level inheritance
    - multilevel inheritance
    - hyierarical inheritance
    - hybrid inheritance
    
# single level inheritance :-

    one parent and one child
    
    Syntax :
            
            parent
              |
              |
              |
            child (child can inherit from parent)
            
    class Parent:
        pass
    class chile(Parent)
        pass


class trainer: # parent
    
    def __init__(self):
        self.trainer_name = 'Trainer'
        self.syllabus = 'python'
        self.programs = 'pattern'
        
    def practical(self):
        print(f'Syllabus : {self.syllabus}\nProgramms : {self.programs}')
        
class student(trainer): # child
    
    def class_details(self):
        print(self.syllabus) # inherting the properties from parent
        print(self.programs)
        
        
s1 = student() # should give parent object
s1.class_details()
s1.practical()


class Teamleader:
    
    def __init__(self):
        self.company = 'Wayne Enterprises'
        self.domain = 'Data Science'
        self.project = 'Brain Tumor detection'
        
    def details(self):
        print(f'Company Name : {self.company}\nDepartment : {self.domain}')
        # print(self) <__main__.Employee object at 0x00000216DD1DE7B0>
        
class Employee(Teamleader):
    
    def team_details(self):
        print(self.company)
        print(self.domain)
        print(self.project)
        # print(self) <__main__.Employee object at 0x00000216DD1DE7B0>
        
e1 = Employee()
e1.team_details()
e1.details()


## Constructor chaining : -

    super()

## syntax :

class parent:
    
    def __init__(self,p_name,p_age):
        self.p_name = p_name
        self.p_age = p_age
        
class child(parent):
    
    def __init__(self,c_name,c_age,p_name,p_age):
        super().__init__(p_name, p_age) # only by super we can access constructor
        self.c_name = c_name
        self.c_age = c_age
        
c1 = child('child1',2,'parent1',55)
print(c1.p_name,c1.p_age)

# Multi level inheritance :

can access multiple child class from single parent

class grandparent:
    pass
class parent:
    pass
class child:
    pass


class Manger:

    def __init__(self):
        self.m_name = 'Batman'
        self.id = 1
        self.m_sal = 'trillions'
        self.project = 'to protect the world'
        
    def m_details(self):
        print(self.tl_name) # we can access from child also
        print('manager here!!')
        print('# ------------------------------- $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ ---------------------------- #')

class TL(Manger):
    
    def __init__(self):
        super().__init__()
        self.tl_name = 'Superman'
        self.tl_id = 2
        self.tl_sal = 'secret'
        self.domain = 'krypton'
        self.head = self.m_name
        self.work = self.project
        
    def display_tl_details(self):
        print(f'Team Leader Name : {self.tl_name}\nTeam Leader ID : {self.tl_id}\nTeam Leader Salary : {self.tl_sal}\nDomain : {self.domain}\nHead for Team Leader : {self.m_name}\nAssigned Work : {self.project}')
        print('# ------------------------------- $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ ---------------------------- #')

class EMP(TL):
    
    def __init__(self):
        super().__init__()
        self.emp_name = 'Grenn lantern(hal Jordan)'
        self.emp_id = 3
        self.emp_sal = '10000$'
        self.assined_work = 'Portect laterns and world'
        self.assigned_by = self.tl_name
        self.p_manger = self.m_name
        
    def display(self):
        print(f'Employee Name : {self.emp_name}\nEmployee ID : {self.emp_id}\nEmployee Salary : {self.emp_sal}\nAssigned Work : {self.assined_work}\nWork Assigned By : {self.assigned_by}\nManager for EMployee : {self.m_name}')
        print('# ------------------------------- $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ ---------------------------- #')
        
emp1 = EMP()
emp1.m_details()
# emp1.display()
# emp1.display_tl_details()
  
## Multiple inheritance :

syntax :

class t_python:
    pass
class t_sql:
    pass
class suman(t_python,t_sql):
    pass

## Hierarical inheritance :

        parent
           |
           |
           |
    -----------------
    |               |
    |               |
    |               |
    |               |
  child 1         child 2
  
syntax :

class parent:
    statement
class child(parent):
    statement
class child(parent):
    statement

## Example :
 
class py_trainer:

    def subjects(self):
        print("Python core", "Python advance", "numpy", "panndas", "ML")

    def experience(self):
        print("2+years")

class mohan(py_trainer):

    def course_details(self):
        print("Premium Python DA")

    def skills3(self):
        print('DA')

class suman(py_trainer):

    def course_details(self):
        print("Premium Python DA")

    def skills2(self):
        print('Python')

class reena(py_trainer):

    def course_details(self):
        print("Premium Python DA")

    def skills1(self):
        print('SQL')

obj = reena()
obj.skills1()
# if we want access a child we need to access particular child to common parent if we give other class method to another child it through error
obj1 = suman()
obj1.skills2()
 
## Hybrid Inheritance : 

    - follows mro
    - hybrid inheritance a child can access different types of inheritance 

class A:
    pass
class B:
    pass
class C:
    pass
class D(A,B,C):
    pass
obj = D()
# print(obj)
print(D.mro())
 
 
## IS - a - Relationship
## HAS - a - Relationship

# IS - a - Relationship

# Inheritance is the best example for is-a-relationship

class Mobile:
    
    def os(self):
        print('Andriod..')
        
class Vivo(Mobile):
    
    def spec(self):
        print('8GB RAM 128GB storage')

obj = Vivo()
obj.spec()
obj.os()

# HAS - a - Relationship

# without using inheritance by creating object we can access the properties of parent class 

# Two types
    # - Composition
    # - Aggregation
    
class Mobile:
    
    def os(self):
        print('Andriod..')
class Vivo():
    
    def spec(self):
        print('8GB RAM 128GB storage')
        self.mob = Mobile() # mob was an object for Mobile class
        print(self.mob) # address for Mobile ## <__main__.Mobile object at 0x000002BB983BEA80>
        print(self) # address for Vivo ## <__main__.Vivo object at 0x000002BB983BE9F0>
        self.mob.os() # accessing Mobile class

obj = Vivo()
obj.spec()


## Aggregation

class Mobile:   # Class Mobile represents a container for mobile objects
    def __init__(self):
        # Two empty lists to store mobile addresses (objects) and names
        self.address = []  
        self.mob_names = []
        
    def os(self, add):
        # Here 'add' is expected to be a Realme object
        self.address.append(add)   # store the whole object
        print('------Inside---------')
        print(add.model)           # prints the model of the mobile
        self.mob_names.append(add.model)  # store just the model name

class Realme:   # Another class that represents Realme mobiles
    def __init__(self, model, RAM):
        self.model = model
        self.RAM = RAM

# Create two Realme objects
mob1 = Realme('Realme 9','4GB')
mob2 = Realme('Realme 10','8GB')      

# Printing their values directly
# print(mob1.model, mob1.RAM)   # Output: Realme 9 4GB
# print(mob2.model, mob2.RAM)   # Output: Realme 10 8GB

print('-----outside------')
print(mob1.model)  # Realme 9
print(mob2.model)  # Realme 10

# Create Mobile object
mobile = Mobile()

# Call os() method with mob1 and mob2
mobile.os(mob1)  # Stores mob1 object + mob1.model
mobile.os(mob2)  # Stores mob2 object + mob2.model

print("Address list (objects):", mobile.address)
print("Mobile names list:", mobile.mob_names)


## Composition

class Mobile:
    def __init__(self):
        # Mobile is directly creating Realme objects inside
        self.address = []
        self.mob_names = []

    def add_realme(self, model, RAM):
        # Creating Realme object INSIDE Mobile (composition)
        new_mobile = Realme(model, RAM)
        self.address.append(new_mobile)
        self.mob_names.append(new_mobile.model)
        print(f"Added {new_mobile.model} with {new_mobile.RAM}")


class Realme:
    def __init__(self, model, RAM):
        self.model = model
        self.RAM = RAM


# ✅ Example usage
mobile = Mobile()

# Here we don't create Realme objects outside.
# Instead, Mobile itself creates them.
mobile.add_realme("Realme 9", "4GB")
mobile.add_realme("Realme 10", "8GB")

print("-----Final Results (Composition)-----")
print("Stored objects:", mobile.address)
print("Stored models:", mobile.mob_names)

# Access RAM from objects created inside Mobile
for obj in mobile.address:
    print(f"{obj.model} → {obj.RAM}")
 
"""

