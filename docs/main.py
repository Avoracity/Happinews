import random

questions = ['True/False: August 5th, Alex Jones was ordered to pay over $45 million in punitive damages to the parents of 6-year-old Jesse Lewis',
            'True/False: Since the pandemic, the economy has now recovered all 22 million jobs that were lost in March and April 2020',
            'True/False: In July, US employers added over 600,000 jobs',
            'True/False: The current rate of inflation in the United States is 9.1%',
            'True/False: Vehicles running on batteries account for 5.6% of new car sales in the past 4 months',
            'True/False: As of August 6th, the average price of gasoline nationwide is now $6.08',
            'True/False: Monkeypox is spread by calling an infected person over the telephone, or by messaging them on Facebook or Instagram',
            'True/False: City issues violation to indoor amusement park on Staten Island after ceiling tiles allegedly fall on campers on a field trip',
            'True/False: As of Saturday, Aug 6, 2022 the New York Yankees have the best record in major league baseball for the 2022 season',
            'True/False: Governor Informs Of World Taekwondo Championship 2022 In Yankee Doodle Land']

answers = ['True',
          'True',
          'False',
          'True',
          'True',
          'False',
          'False',
          'True',
          'False',
          'False']
          
asked = list()

score = 0

for i in range(10):
  # come up with random question from list of questions
  q = random.randint(0, len(questions)-1)
  # check to see if the question was already asked
  while q in asked:
      # if it was, generate a fresh question
      q = random.randint(0, len(questions)-1)
  # if not, ask it
  asked.append(q)
  print(questions[q])
  ans = input("Please enter your answer:")
  if (ans == answers[q] or ans == answers[q].lower() or ans == answers[q].upper()):
    print("Correct! You get 1 point!")
    score += 1
  else:
    print("Incorrect. Better luck next time.")

score = str(score * 10) + "%"

# display the user's score in terms of percentage
print("Game Over!\n"+"Your score is:", score)