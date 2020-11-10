try:
    result = 11 / 0
    print(result)
except Exception as e:
    print(e)
finally:
    print('Finally I got the error')


try:
    result = 11 / 0
    print(result)
except OSError as e:
    print(e)
finally:
    print('Finally I got the error')

try:
    result = 11 / 0
    print(result)
except ZeroDivisionError as e:
    print(e)
finally:
    print('Finally I got the error')
