import time
start_time = time.time()
print("I'm HIT 14\n" * 20) # tiết mục chính đây ạ . Mấy cái còn lại để so sánh thời gian chạy 
end_time = time.time()
test1 = end_time - start_time
start_time2 = time.time()
for i in range(0,20):
    print("I'm HIT 14")
end_time2 = time.time()
test2 = end_time2 - start_time2
print(test2 - test1)

