import random  
# Importing the random module for generating random numbers

def Welcome():

    Name = (input('**Welcome to the mathematics quiz!** \n \n please state your name '))  # Prompting user to enter their name

    print('\n Nice to meet you.', Name)  
    # Greeting the user by their name

    questionCount()  
    # Calling the function to start the quiz after welcoming the user

def questionCount():
  # Input Validation Loop
  while True:
      try:
          QuestionCount = int(input('\nHow many questions would you like to be asked?'))  # Prompt user for number of questions
          break
      except ValueError:
          print('You must enter an integer number')  
          # Error message for non-integer input

  if QuestionCount >= 1:
      score = 0  # Initialize score counter
      history = []  # Initialize list to store question history

      # Game Loop
      for x in range(QuestionCount):
          num1 = random.randint(1, 12)  # Generate random number 1
          num2 = random.randint(1, 12)  # Generate random number 2
          answer = num1 + num2  # Calculate correct answer

          # Ask user for answer with input validation
          while True:
              try:
                  question = int(input(f"What is {num1} + {num2}: "))                     # Prompt user with addition question
                  break
              except ValueError:
                  print('You must enter an integer number') 
                  # Error message for non-integer input

          CorrectList = ["Great job!", "Well done", "Your awesome!",]  # Positive feedback options

          IncorrectList = ["Remember to add correctly", "You may need to check or use an addition chart"]  # Negative feedback options

          CorrectFeedback = random.choice(CorrectList) 
          # Randomly select positive feedback

          IncorrectFeedback = random.choice(IncorrectList) 
          # Randomly select negative feedback

          # Check user answer and provide feedback
          if question == answer:
              print(f"Correct {CorrectFeedback}") 
              # Print correct message

              score += 1  # Increment score
              print('Score:', score,)  # Print current score

              history.append(f"What is {num1} + {num2}? you put: {question} and the answer was {answer} which is correct") 
              # Record correct question in history
          else:
              print(f"Incorrect {IncorrectFeedback}") 
              # Print incorrect message
              print('Score:', score,)  # Print current score

              history.append(f"What is {num1} + {num2}? you put: {question} and the answer was {answer} which is incorrect")  
      # Record incorrect question in history

      # End of Game
      print(f"Your score is {score} out of {QuestionCount}") 
      # Print final score

      print ('Your total score was', score,)
      # Print total score again

      percentage = (score / QuestionCount) * 100  
      # Calculate percentage score

      print('Percentage: {:.2f}%'.format(percentage))  
      # Print percentage score

      while True:
          SeeHistory = input('\nWould you like to see your history? (Yes/No)')  
          # Ask if user wants to see history
          if SeeHistory in ["yes", "Yes", "y","Y"]:
            print('\nQuestion History:\n')  
            # Print header for question history
            for i in range(0,len (history)):
                print(history[i], "\n")  
            # Print each question's history
            break
          elif SeeHistory in ["No","no","N","n"]:
              break
          else:
              print("Please enter an answer being Yes or No")

      while True:
          replay = input('Do you wish to replay?: (Yes/No)') 
          # Ask if user wants to replay
          if replay in ["yes", "Yes", "y", "Y"]:
            print("replaying...")  
            # Print message indicating replaying
            questionCount()  
            # Recursively call function to start new game
          elif replay in ["No","no","N","n"]:
            break 
          else:
              print("type a proper answer being Yes or No")
            # Print farewell message if user doesn't want to replay

Welcome()