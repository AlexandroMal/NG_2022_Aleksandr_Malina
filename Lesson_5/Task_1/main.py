from flask import Flask, render_template, request

app = Flask("Calculator")

def operationAddition (NumberFirst, NumberSecond):
    return NumberFirst + NumberSecond

def operationSubtraction (NumberFirst, NumberSecond):
    return NumberFirst - NumberSecond

def operationMultiplication (NumberFirst, NumberSecond):
    return NumberFirst * NumberSecond

def operationDivision (NumberFirst, NumberSecond):
    return NumberFirst / NumberSecond


def calculate(NumberFirst,NumberSecond,operation):
    match operation:
        case "+":
            result = str(operationAddition(NumberFirst, NumberSecond))
        case "-":
            result = str(operationSubtraction(NumberFirst, NumberSecond))
        case "*":
            result = str(operationMultiplication(NumberFirst, NumberSecond))
        case "/":
            result = str(operationDivision(NumberFirst, NumberSecond))
        case _:
            result = ("Woops!")
    return result

@app.route('/')
def main():
    try: 
        NumberFirst = int(request.args.get("first_num"))
        NumberSecond = int(request.args.get("second_num"))
        operation = request.args.get("select_operation")
        result = calculate(NumberFirst,NumberSecond,operation) 
        return render_template("index.html", result=result)
    except:
        NumberFirst = 0
        NumberSecond = 0
        operation = "+"
        return render_template("index.html")



app.run(host="0.0.0.0", port=8080)