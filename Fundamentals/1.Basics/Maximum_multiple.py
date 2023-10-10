div = int(input())
limit = int(input())
max_dev=0
for i in range(0,limit+1):
    
    if i%div==0:
        max_dev=i
print(max_dev)
