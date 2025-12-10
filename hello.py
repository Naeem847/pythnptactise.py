# print("wellcome to artificial intelligence Lab:")
# name="Ai student"
# age=22
# marks=[85,90,78]
# student={"name":name,"age":age,"marks":marks}
# print(student)
# for i in range(1,6):
#     if i%2==0:
#         print(i,"is even")
#     else:
#         print("odd")    
# def factorial(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n*factorial(n-1)
# print("factorial of 5:",factorial(5))
# class student:
#     def __init__(self, name, rollno):
#         self.name = name
#         self.rollno = rollno
#     def display(self):
#         print("name:", self.name)
#         print("rollno:", self.rollno)
# s1 = student("ali", 101)
# s1.display()
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


         
         

# queue=[]
# queue.append(10)
# queue.append(20)
# queue.append(30)
# print("queue is:",queue)
# first=queue.pop(0)
# print("after dequed is:",queue)
# print("dequed is:",first)
# first=queue.pop(0)
# print("after dequed is:",queue)
# print("dequed is:",first)
# first=queue.pop(0)
# print("after dequed is:",queue)

# print("dequed is:",first)
# print("after dequed is:",queue)
# from collections import deque
# stack=deque()
# stack.append(10)
# stack.append(20)
# stack.append(30)
# print("stack:",stack)
# removed=stack.pop()
# print("popped:",removed)
# print("after popped:",stack)
# 1111111111111111111111111111111111111111111111
# from collections import deque
# graph={
#     'a':['b','c'],
#     'b':['d'],
#     'c':[],
#     'e':[]
# }
# def bfs(start):
#     visited=set()
#     queue=deque([start])
#     while queue:
#         node=queue.popleft()
#         if node not in visited:
#             print(node,end=" ")
#             visited.add(node)
#             queue.extend(graph[node])
# bfs('a')   
# 11111111111111111111111111111111111         
############################################
# from collections import deque
# def show_bfs_dfs():
#     print("bfs vs dfs data staructure:")
# q=deque()
# q.append("start")
# print("dfs queu:",list(q))
# q.append("next")
# q.popleft()
# print("bfs deque:",list(q))
# stack=[]
# stack.append("start")
# print("dfs stack:",stack)
# stack.append("next")
# stack.pop()
# show_bfs_dfs()
