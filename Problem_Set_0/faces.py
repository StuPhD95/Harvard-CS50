def convert(string):
    string = string.replace(":)", "🙂")
    string = string.replace(":(", "🙁")
    return string

def main(string):
    string = convert(string)
    print(string)
    
main(str(input()))