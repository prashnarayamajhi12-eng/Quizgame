

question1={
    "question": "If you have a clock that takes 5 seconds to strike 6 times,how long will it take to strike 12 times?",
    "options": ["A) 10 seconds", "B) 11seconds", "C) 12 seconds", "D) 15 seconds"],
    "answer": "D) 15 seconds"
}
question2={
    "question": "A family has 4 daughters.Each daughter has one brother.How many children does the woman have?",      
"options": ["A) 4", "B) 5", "C) 8", "D) 12"],
    "answer": "B) 5"
}
question3={
    "question": "What is the chemical symbol for water?",
    "options": ["A) H2O", "B) CO2", "C) NaCl", "D) O2"],
    "answer": "A) H2O"
}
question4={
    "question": "Who wrote the play 'Romeo and Juliet'?",
    "options": ["A) William Shakespeare", "B) Charles Dickens", "C) Mark Twain", "D) Jane Austen"],
    "answer": "A) William Shakespeare"
}
question5= {
    "question": "What is the speed of light?",
    "options": ["A) 3 x 10^8 m/s", "B) 1.5 x 10^8 m/s", "C) 3 x 10^6 m/s", "D) 1 x 10^7 m/s"],
    "answer": "A) 3 x 10^8 m/s"
}
questions= [
    question1,
    question2,
    question3,
    question4,
    question5
]
print("Welcome to the Quiz!")
print("You will be asked 5 questions. Please select the correct option (A, B, C, or D).")
print("Let's begin!\n")
score = 0
for i, question in enumerate(questions):
    print(f"Question {i+1}: {question['question']}")
    for option in question['options']:
        print(option)
    answer = input("Your answer: ")
    if answer.upper() == question['answer'][0]:
        print("Correct!\n")
        score += 1
    else:
        print(f"Wrong! The correct answer is: {question['answer']}\n")
        print("Quiz completed!")
print(f"Your final score is {score}/5")
if score == 5:
    print("🎉 Congratulations! Perfect score! You got all questions correct!")
elif score >= 3:
    print("👏 Congratulations! Good job! You did well!")
else:
    print("💪 Good effort! Keep practicing and you'll improve!")