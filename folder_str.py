from pathlib import Path

def generate_tree_structure(start_path, indent=''):
    start_path = Path(start_path)
    if not start_path.is_dir():
        print(f"{start_path} is not a directory or doesn't exist.")
        return

    def recurse(path, level):
        indent = ' ' * 4 * level
        print(f"{indent}{path.name}/")
        for child in path.iterdir():
            if child.is_dir():
                recurse(child, level + 1)
            else:
                print(f"{indent}    {child.name}")

    recurse(start_path, 0)

# Example usage
start_path = r"\\wsl$\Ubuntu-24.04\home\yoe\simple-app-lambdas"
generate_tree_structure(start_path)