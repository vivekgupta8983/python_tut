"""
Exceptions are errors
"""

def exceptionhandling():
    try:
        a = 10
        b = 20
        c = 10

        d = (a + b) / c
        print(d)
    except:
        print("In the Exception block,")
        raise Exception("There is exceptions")
    else:
        print("Because there was no exception, else is exceuted")
    finally:
        print("it always executed")



exceptionhandling()