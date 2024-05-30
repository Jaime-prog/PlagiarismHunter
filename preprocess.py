import os
import json
import javalang

def collect_java_files(base_path):
    """Recopila todos los archivos Java en el directorio base y sus subdirectorios."""
    java_files = []
    for root, _, files in os.walk(base_path):
        for file in files:
            if file.endswith(".java"):
                java_files.append(os.path.join(root, file))
    return java_files

def generate_ast(java_file_path):
    """Genera un Árbol de Sintaxis Abstracta (AST) a partir de un archivo Java."""
    with open(java_file_path, 'r') as file:
        java_code = file.read()
    tokens = javalang.tokenizer.tokenize(java_code)
    parser = javalang.parser.Parser(tokens)
    return parser.parse()

def ast_to_dict(node):
    """Convierte un AST a un diccionario."""
    if isinstance(node, javalang.ast.Node):
        return {
            'type': type(node).__name__,
            'attributes': {key: ast_to_dict(value) for key, value in node.attrs.items() if value is not None},
            'children': [ast_to_dict(child) for child in node.children if child is not None]
        }
    elif isinstance(node, list):
        return [ast_to_dict(child) for child in node]
    else:
        return node

def save_ast(ast, output_path):
    """Guarda un AST en formato JSON."""
    ast_dict = ast_to_dict(ast)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w') as file:
        json.dump(ast_dict, file, indent=2)

def preprocess_dataset(base_path, output_dir):
    """Preprocesa el dataset convirtiendo archivos Java en ASTs y guardándolos en formato JSON."""
    java_files = collect_java_files(base_path)
    for java_file in java_files:
        try:
            ast = generate_ast(java_file)
            relative_path = os.path.relpath(java_file, base_path)
            output_path = os.path.join(output_dir, f"{relative_path}.json")
            save_ast(ast, output_path)
            print(f"Procesado: {java_file}")
        except Exception as e:
            print(f"Error procesando {java_file}: {e}")

if __name__ == "__main__":
    base_path = './Versions/version 2'
    output_dir = './Preprocessed_files/'
    preprocess_dataset(base_path, output_dir)
