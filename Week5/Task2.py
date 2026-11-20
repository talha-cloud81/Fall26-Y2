tasks = ["done", "pending", "done", "pending", "done", "pending"] 
tasks[1::2]=["completed"]*3
tasks[3:3]=["audit"]

print(tasks)