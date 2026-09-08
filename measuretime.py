import time
start_time = time.perf_counter()
for i in range(1000) :
    pass
end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f"The time take to execute is {elapsed_time : 1f}")
