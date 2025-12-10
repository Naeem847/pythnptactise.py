#Task 1:
print("wellcome to artificial intelligence Lab:")
name="Ai student"
age=22
marks=[85,90,78]
student={"name":name,"age":age,"marks":marks}
print(student)
#Task 2:
for i in range(1,6):
    if i%2==0:
        print(i,"is even")
    else:
        print("odd") 
#Task 3:   
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
print("factorial of 5:",factorial(5))
#Task 4:
class student:
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
    def display(self):
        print("name:", self.name)
        print("rollno:", self.rollno)
s1 = student("ali", 101)
s1.display()


         
         

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
