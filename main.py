import sys
import time
try:
    code = open(sys.argv[1], "r")
except IndexError:
    code = input("Enter file path: ")
    code = open(code, "r")
code = code.read()

code = code.replace("\n", "")
code = code.split(";")

print("From J++ Code>", code)

variables = {

}

def variable_assign(statement):
    if statement.find(" = ") != -1:
        statement.replace(" = ", "=")
        statement = statement.split("=")
        if statement[0].find("$") != -1:
            statement[0] = statement[0].replace("$", "")
            if statement[0].find("\"") != -1:
                statement[0] = statement[0].replace("\"", "")
            variables[statement[0].strip()] = statement[1]
        elif statement[0].find("*") != -1:
            statement[0] = statement[0].replace("*", "")
            statement[1] = int(statement[1])
            variables[statement[0].strip()] = statement[1]
        elif statement[0].find("_") != -1:
            statement[0] = statement[0].replace("_", "")
            if statement[1] == "True":
                statement[1] = True
            elif statement[1] == "False":
                statement[1] = False
            variables[statement[0].strip()] = statement[1]
def write(statement):
    if statement.find("write(") != -1 and statement.find(")") != -1:
        statement = statement.replace("write(", "")
        statement = statement.replace(")", "")
        if statement.find("$") != -1:
            statement = statement.replace("$", "")
            out = statement.replace(statement, variables[statement])
        elif statement.find("*") != -1:
            statement = statement.replace("*", "")
            out = statement.replace(statement, str(variables[statement]))
            out = int(out)
        elif statement.find("_") != -1:
            statement = statement.replace("_", "")
            out = statement.replace(statement, variables[statement])
        else:
            out = statement
        print("From J++ Output>", out)
def py(statement):
    if statement.find("py{") != -1 and statement.find("}") != -1:
        statement = statement.replace("py{", "")
        statement = statement.replace("}", "")
        eval(statement)
for statement in code:
    try:
        variable_assign(statement)
        write(statement)
        py(statement)
    except KeyError:
        print("Error: Variable called without assignment")
    except KeyboardInterrupt:
        print("Program terminated")

time.sleep(999999)