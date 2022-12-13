#import PooPometry
class Employee:
  rasise_amount = 1.05
  attack_damage = 5
  health = 1
  def __init__(self,first_name,last_name,job_title,salary,email):
    self.first_name = first_name
    self.last_name = last_name
    self.job_title = job_title
    self.salary = salary
    self.email = email
  def apply_raise_to_employees_salary(self):
    new_salary = self.salary * self.rasise_amount
    self.salary = new_salary
    print(f"congrats poopy head your new salary is {self.salary} lakhs per annum")
  def throw_poop(self):
    print(f"throwing poop minus {self.attack_damage} health")
mason = Employee('mason','delgado','programmer',10,'masonman8787@gmail.com')
mason.apply_raise_to_employees_salary()
class Sales(Employee):
  def __init__(self,first_name,last_name,job_title,salary,email,phone_number):
    super().__init__(first_name,last_name,job_title,salary,email)
    self.phone_number = phone_number
  def follow_up_email(self,customer):
    print(f"Dear {customer},\nThank you for your interest in our product.\nPlease let me know if you have any questions.\nMy email is {self.email} or my phone number is {self.phone_number}.\nThanks, {self.first_name} {self.last_name}")
    pass
class Development(Employee):
  def __init__(self,first_name,last_name,job_title,salary,email):
    super().__init__(first_name,last_name,job_title,salary,email)
    pass
  def code(self):
    print(f"{self.first_name} {self.last_name} is writing code")


s = Sales('Mason','Delgado','programmer',10,'masonman8787@gmail.com','+14025656464')
s.follow_up_email('poopy head')
d = Development('Mason','Delgado','programmer',10,'masonman8787@gmail.com')
d.code()
masond = Sales('Mason','Delgado','programmer',50,'masonman8787@gmail.com','+14025656464')
masond.follow_up_email("Mike O'Neil" )
masond.follow_up_email("Hannah Stern")
masond.apply_raise_to_employees_salary()
poopy_face = Development('poopy','face','poopy king',100,'poopyface@poopytown.com')
poopy_face.code()
poopy_face.apply_raise_to_employees_salary()
poopy_face.throw_poop()
#PooPometry.PoopCircle(7)
#PooPometry.RightAngle(3,4)
class Enemy():
    def __init__(self,type_of_enemy,health,attack_damage,_attack_style):
        self.type_of_enemy = type_of_enemy
        self.health = health
        self.attack_damage = attack_damage
        self._attack_style = _attack_style
    def attack(self):
        print(f"the {self.type_of_enemy} is using {self._attack_style} against you for {self.attack_damage} hearts")
class ToiletPaper(Enemy):
    def __init__(self,type_of_enemy='ToiletPaper',health=100,attack_damage=.25,_attack_style='wipe'):
        super().__init__(type_of_enemy,health,attack_damage,_attack_style)
    def TPhealth(self):
        pass
    pass
class PoopyHero(Enemy):
    def __init__(self,type_of_enemy='Poopy Hero',health=500,attack_damage=25,_attack_style='poop throw'):
        super().__init__(type_of_enemy,health,attack_damage,_attack_style)
    def PHIncomingDamage(self):
        new_health=self.health - .25
        self.health = new_health
        pass
T1=ToiletPaper()
T1.attack()
T1.attack()
T1.attack()
T1.attack()
PH = PoopyHero()
PH.attack()