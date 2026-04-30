try:
    marks=25
    results=25/0
    print(result)
except ZeroDivisionError:
    print("A number cannot be divide by zero")

try:
    list=[1,2,3,4,5]
    print(list[7])
except IndexError:
    print("Index is out of range")

try:
    import cse13

except ModuleNotFoundError:
    print("Module not found")

finally:
    print("code runs succesfully")
