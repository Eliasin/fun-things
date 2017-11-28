import os
#Variable Names

#Good

total_jelly_beans = 6
selected_character = "Jim"
index = 0
current_hp = 300

#Bad/Worse

jbTotal = 6
selChr = "Jim"
i = 0
c_hp = 300

#NEVER

a = 6
b = "Jim"
c = 0
d = 300

#Function Names

#Good
def add_and_double(x: int, y: int) -> int:
  return (x + y) * 2

#Bad/Worse
def addanddouble(x: int, y: int) -> int:
  return (x + y) * 2

def AddAndDouble(x: int, y: int) -> int:
  return (x + y) * 2

def Add_And_Double(x: int, y: int) -> int:
  return (x + y) * 2

def ADDANDDOUBLE(x: int, y: int) -> int:
  return (x + y) * 2

#Comments

cost = 500
tax = 1.13
#Calculate total cost by adding tax
total_cost = cost * tax

#=====

player_dead = True
def remove_player():
  pass

#Remove player if they are dead
if player_dead:
  remove_player()
  
#=====

line_ending = "\n"

#Windows uses carriage returns in its line endings
if (os.name == "Windows"):
  line_ending = "\r\n"

#Magic Numbers

#Good

max_name_length = 15
def good_name_verification(name: str) -> bool:
  return name <= max_name_length
  
#Bad

def bad_name_verification(name: str) -> bool:
  return name <= 15
