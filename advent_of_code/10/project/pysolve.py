def connection_test():
    return 1

myDict = {
    1 : {
        "position" : (2,3),
        "direction" : (1,2)
    },
    2 : {
        "position" : (1,3),
        "direction" : (1,2)
    }
}

print(myDict[1]["position"])


input = "position=< 21188,  31669> velocity=<-2, -3>"
def transform_input(input):
    print(dictionary = eval(input.replace("position=< ", "'{position' : (").replace("velocity=<", "'velocity' : (" ).replace(">", "),", 1).replace(">", ")},")))


transform_input(input)