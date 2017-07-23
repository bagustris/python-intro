from random import randint

# f = open('sort_this.txt', 'w')
# for k in range(10):
#     f.write(str(randint(0,100)) + str('\n'))
# f.close()

with open ('sort_this.txt', 'w') as f:
    for k in range(10):
        f.write(str(randint(0,100)) + str('\n'))

a=[]
with open ('sort_this.txt', 'r') as f:
    for line in f:
        a.append(int(line))

print(a)
