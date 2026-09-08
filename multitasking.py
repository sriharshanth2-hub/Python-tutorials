import time
import threading

def watch_brocode() :
    time.sleep(6)
    print("completed watching brocode")

def solve_leetcode() :
    time.sleep(3)
    print("completed solving a problem")

def start_ngl() :
    time.sleep(5)
    print("Started andrew ngl course")

task_1 = threading.Thread(target=watch_brocode)
task_1.start() 
task_2 = threading.Thread(target=solve_leetcode)
task_2.start() 
task_3 = threading.Thread(target=start_ngl)
task_3.start() 

task_1.join()
task_2.join()
task_3.join()

print("all tasks completed!!")