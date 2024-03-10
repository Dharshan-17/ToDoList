l=[]
def add():
    print("enter task")
    new=input()
    l.append(new)
    print("Added Task: ",l)
    
def edit():
    print("Edit task number: ")
    rmv=int(input())
    l.pop(rmv)
    new=input("new task: ")
    l.insert(rmv, new)
    print("Edited Task: ", l)

def delete():
    dele= int(input("Delete task at which position: "))
    l.pop(dele)
    
print("1.Add a task\n2.Edit task\n3.Delete task")

add()
add()
add()
edit()
delete()
print("final tasks: ", l)
