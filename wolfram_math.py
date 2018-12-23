import wolframalpha

def fun_math(string_):
    try:
        app_id = ""
        client = wolframalpha.Client(app_id)
        res = client.query(string_)
        answer = next(res.results).text
        print(answer)
    except AttributeError:
        print("Some error occured")

    except ZeroDivisionError:
        print("Division by zero is non-determinate")
    except ArithmeticError:
        print ("Arithmetic error occured")
    except AssertionError:
        print('Assertion error occured')

def wolfram_math_api():
    query = input("Enter the mathematical query: ")
    fun_math(query)

