import random

class QA:
  def __init__(self, question, correctAnswer, otherAnswers):
    self.question = question
    self.corrAnsw = correctAnswer
    self.otherAnsw = otherAnswers

qaList = [QA("What is output of −33 == 33.0?", "True", ["False", "33","None of the above"]),
QA("Which of the following is false statement in python?", "int(144)==144", ["int('144')==144", "Both of Them", "None of the above"]),
QA("How can we check whether the object is instance of class or not. Let us consider an object O which is instance of class B.", "isinstance(O,B)", ["B.isinstance(O)", "isinstance(B,O)", "isinstance(O)"]),
QA("Which among them is used to create an object?", "A constructor", ["A method", "A class","A function"]),
QA("For tuples and list which is correct?", "List is mutable whereas tuples are immutable.", ["List and tuples both are mutable.", "List and tuples both are immutable.", " List is immutable whereas tuples are mutable."])]

corrCount = 0
random.shuffle(qaList)
for qaItem in qaList:
  print(qaItem.question)
  print("Possible answers are:")
  possible = qaItem.otherAnsw + [qaItem.corrAnsw] 
  random.shuffle(possible)
  count = 0 
  while count < len(possible):
    print(str(count+1) + ": " + possible[count])
    count += 1
  print("Please enter the number of your answer:")
  userAnsw = input()
  while not userAnsw.isdigit():
    print("That was not a number. Please enter the number of your answer:")
    userAnsw = input()
  userAnsw = int(userAnsw)
  while not (userAnsw > 0 and userAnsw <= len(possible)):
    print("That number doesn't correspond to any answer. Please enter the number of your answer:")
    userAnsw = input()
  if possible[userAnsw-1] == qaItem.corrAnsw:
    print("Your answer was correct.")
    corrCount += 1
  else:
    print("Your answer was wrong.")
    print("Correct answer was: " + qaItem.corrAnsw)
  print("")

print("You answered " + str(corrCount) + " of " + str(len(qaList)) + " questions correctly.")
      
