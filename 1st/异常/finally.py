num = 1
try:
    print(num)
except Exception as msg:
    print(msg)
else:
    print('我是else，是没有异常的时候执⾏的代码')
finally:
    print('睡觉')