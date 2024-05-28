import javalang

def parse_java_code(code):
    try:
        tree = javalang.parse.parse(code)
        return tree
    except javalang.parser.JavaSyntaxError as e:
        print("JavaSyntaxError: ", e)
        return None

# Get java code from directory
def get_java_code():
    with open('test.java', 'r') as file:
        code = file.read()
    return code

codigo = get_java_code()
parseado = parse_java_code(codigo)

print(parseado)