"""
Exception are errors
we should handle exception in a code
to make sure the cpde is working in a way we want  and is handling all unwanted issues
Try, Except, Else, Finally

"""

def exceptionhandling():
    try:
        a = 10
        b = "String"
        c = 0

        d = (a + b) / c
        print(d)
    except ZeroDivisionError:
        print("this is zero division error")
    except TypeError:
        print("Can't add string to integers")


exceptionhandling()