import datetime
import random

# Chatbot introduction
print("=" * 50)
print("AI CHATBOT - BSCS6C")
print("Created by Muhammad Naeem")
print("=" * 50)

print("Chatbot: Hello! I am your virtual assistant.")
print("Chatbot: Type 'help' to see my features.")
print("Chatbot: Type 'bye' to end the chat.\n")

# Variables
user_name = ""
message_count = 0

# Lists of jokes and motivational quotes
jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "Why did the computer go to the doctor? Because it had a virus!",
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "Why was the math book sad? Because it had too many problems!"
]

quotes = [
    "Believe in yourself and never give up!",
    "Every expert was once a beginner.",
    "Success comes from hard work and consistency.",
    "Your future depends on what you do today.",
    "Keep learning, keep growing!"
]

# Main chatbot loop
while True:

    user_input = input("You: ").strip().lower()

    # Ignore empty messages
    if not user_input:
        print("Chatbot: Please enter a message.")
        continue

    message_count += 1

    # Exit commands
    if user_input in ["bye", "exit", "quit"]:
        print("Chatbot: Goodbye! Have a great day!")
        print(f"Chatbot: You sent {message_count} messages.")
        break

    # Help command
    elif user_input == "help":
        print("""
Chatbot: Here are my available features:

1. Say hello or hi
2. Ask how are you
3. Ask my name
4. Ask what I can do
5. Tell me your name
6. Ask for the current time
7. Ask for today's date
8. Ask me to calculate
9. Ask about Python
10. Ask about AI
11. Ask about Pakistan
12. Ask for a joke
13. Ask for a motivational quote
14. Ask for a random number
15. Type 'bye' to exit

Example commands:
- hello
- my name is Naeem
- what time is it
- what is today's date
- calculate
- tell me a joke
- give me a quote
""")

    # Greetings
    elif any(word in user_input.split() for word in
             ["hello", "hi", "hey"]):
        print("Chatbot: Hello! How can I help you today?")

    elif "good morning" in user_input:
        print("Chatbot: Good morning! Have a wonderful day!")

    elif "good evening" in user_input:
        print("Chatbot: Good evening! How can I help you?")

    # User's name
    elif user_input.startswith("my name is "):
        user_name = user_input.replace("my name is ", "", 1).strip().title()

        if user_name:
            print(f"Chatbot: Nice to meet you, {user_name}!")

        else:
            print("Chatbot: Please tell me your name.")

    elif "what is my name" in user_input:
        if user_name:
            print(f"Chatbot: Your name is {user_name}.")
        else:
            print("Chatbot: You haven't told me your name yet.")

    # Chatbot information
    elif "how are you" in user_input:
        print("Chatbot: I am doing well! I am ready to assist you.")

    elif "what is your name" in user_input:
        print("Chatbot: I am an AI chatbot created by Muhammad Naeem.")

    elif "what can you do" in user_input:
        print("Chatbot: I can tell jokes, show time and date, "
              "calculate numbers, and answer basic questions.")

    elif "how old are you" in user_input:
        print("Chatbot: I don't age because I am a computer program.")

    elif "creator" in user_input or "who created you" in user_input:
        print("Chatbot: I was created by Muhammad Naeem "
              "for BSCS6C students at FUUAST.")

    # Time
    elif "time" in user_input:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        print(f"Chatbot: The current time is {current_time}.")

    # Date
    elif "date" in user_input or "today" in user_input:
        current_date = datetime.datetime.now().strftime("%d %B %Y")
        print(f"Chatbot: Today's date is {current_date}.")

    # AI information
    elif user_input == "ai" or "what is ai" in user_input:
        print("Chatbot: AI stands for Artificial Intelligence. "
              "It enables computers to perform tasks that usually "
              "require human intelligence.")

    # Python information
    elif "python" in user_input:
        print("Chatbot: Python is a popular programming language "
              "used in AI, Machine Learning, web development, "
              "automation, and data science.")

    # Pakistan information
    elif "capital of pakistan" in user_input:
        print("Chatbot: The capital of Pakistan is Islamabad.")

    elif "national language of pakistan" in user_input:
        print("Chatbot: The national language of Pakistan is Urdu.")

    # Jokes
    elif "joke" in user_input:
        print("Chatbot:", random.choice(jokes))

    # Motivational quotes
    elif "quote" in user_input or "motivate me" in user_input:
        print("Chatbot:", random.choice(quotes))

    # Random number
    elif "random number" in user_input:
        number = random.randint(1, 100)
        print(f"Chatbot: Your random number is {number}.")

    # Calculator
    elif "calculate" in user_input or "calculator" in user_input:
        try:
            num1 = float(input("Enter the first number: "))
            operator = input("Enter operator (+, -, *, /): ").strip()
            num2 = float(input("Enter the second number: "))

            if operator == "+":
                result = num1 + num2

            elif operator == "-":
                result = num1 - num2

            elif operator == "*":
                result = num1 * num2

            elif operator == "/":
                if num2 == 0:
                    print("Chatbot: You cannot divide by zero.")
                    continue
                result = num1 / num2

            else:
                print("Chatbot: Invalid operator.")
                continue

            print(f"Chatbot: Result = {result:g}")

        except ValueError:
            print("Chatbot: Please enter valid numbers.")

    # Conversation counter
    elif "how many messages" in user_input:
        print(f"Chatbot: You have sent {message_count} messages.")

    # Unknown question
    else:
        print("Chatbot: Sorry, I didn't understand that.")
        print("Chatbot: Type 'help' to see what I can do.")