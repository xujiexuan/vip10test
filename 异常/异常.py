num = 1
f = open("test.txt")
f.close()
try:
    print(num)
except Exception as msg:
    print(msg)
