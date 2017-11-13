from functools import reduce

english_marks = [31, 20, 44, 49, 50, 33, 45, 21, 3, 17, 40]
math_marks = [26, 25, 30, 50, 41, 29, 19, 26, 38, 35, 42]

print("I have a set of english marks and a set of math marks, both are out of 50.")

def convert_marks_to_percentage(marks):
  result = []
  for mark in marks:
    result.append(mark / 50 * 100)
  
  return result
  
english_marks_percentage = convert_marks_to_percentage(english_marks)
print("The english marks are {}".format(english_marks_percentage))

print("That was pretty long winded, is there a standard way to apply some function to every member in a list?")
print("One google search later...")

math_marks_percentage = list(map((lambda x: x / 50 * 100), math_marks))
print("The math marks are {}".format(math_marks_percentage))

print("Now to get the class average.")

def average(marks):
  total = 0
  for mark in marks:
    total += mark
    
  return total / len(marks)
  
english_average = average(english_marks_percentage)
print("The average is... {:.1f}%, ouch. Let's see if the math marks are any better.".format(english_average))

math_average = reduce((lambda x, y: x + y), math_marks_percentage) / len(math_marks_percentage)
print("The math average is {:.1f}%, wait that's barely an improvement!".format(math_average))

def filter_marks(marks):
  passing = []
  for mark in marks:
    if mark / 50 * 100 > 50:
      passing.append(mark)
  
  return passing

print("Well, time to find the averages of the passing scores.")

passing_english = filter_marks(english_marks)
passing_math = list(filter((lambda x: (x / 50 * 100) > 50), math_marks))

def average_mark(marks):
  return reduce(
    (lambda x, y: x + y), 
      map((lambda x: x / 50 * 100), marks)
    )

print("So the passing grades are {} and {}".format(passing_english, passing_math))

passing_math_average = average_mark(passing_math) / len(passing_math)
passing_english_average = average_mark(passing_english) / len(passing_english)

print("And the passing averages are {:.2f}% and {:.2f}%.".format(passing_math_average, passing_english_average))
print("I guess thats a bit better.")
