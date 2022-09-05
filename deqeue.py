from collections import deque

q = deque()


q.append('Aman')
q.append('Dhruv')
q.append('Darshan')

print("All the queue")
print(q)

print('\nPop element from the queue')
print(q.pop())
print(q.popleft())

print('\nQueue after pop')
print(q)