print("Ai chatbot: Hello!BSCS6C i am your virtual assistant.")
print("type'bye' to end the chat.\n")
while True:
    user_input=input("you:").lower()
    if"hello"in user_input or "hi" in user_input:
         print("chatbot:hello! how can i help you today?")
    elif "how are you"in user_input:
         print("chatbot:i am just a computer program,but i am here to assist you!")
    elif"what is your name" in user_input:
         print("chatbot:i don't have a name.i'm just a program.")
    elif"what can you do"in user_input:
         print("chatbot:i can answer question provide information, and  conversation")
    elif"how old are you"in user_input:
         print("Chatbot:i don't age.i am a program designed to assist you.")
    elif"tell a joke"in user_input: 
         print("Chatbot:why don't scientists trust atoms?because they make up everything!")
    elif"what is the capital of pakistan"in user_input: 
         print("Chatbot:the capital of pakistan is islamabad")  
    elif"your name"in user_input: 
         print("Chatbot:i'm an AI chatbot created for this job.")
    elif"ai"in user_input:
         print("Chatbot:AI stand for Artificial Intelligence-simulating human thinking.")
    elif"creator"in user_input:
         print("Chatbot:i was created by Muhammad Naeem for BSCS6C student of FUUAST")
    elif"bye"in user_input:
         print("Chatbot:Goodbye!Hava a great day!")
         break
    else:
         print("Chatbot:Sory i didn't understand that.")
