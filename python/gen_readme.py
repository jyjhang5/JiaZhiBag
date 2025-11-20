import os


TARGET_DIRS = ["python"]


def list_dir_tree(root_dir, prefix=""):
    """
    recursive function to list directory tree
    """
    if not os.path.exists(root_dir):
        print(f"{root_dir} not found.")
        return

    entries = sorted(os.listdir(root_dir))
    for i, entry in enumerate(entries):
        path = os.path.join(root_dir, entry)
        connector = "└── " if i == len(entries)-1 else "├── "
        print(prefix + connector + entry)
        if os.path.isdir(path):
            extension = "    " if i == len(entries)-1 else "│   "
            list_dir_tree(path, prefix + extension)


if __name__ == "__main__":
    project_root = os.getcwd()
    print(f"Project Root: {project_root}\n")
    
    for dir_name in TARGET_DIRS:
        dir_path = os.path.join(project_root, dir_name)
        print(dir_name + "/")
        list_dir_tree(dir_path, "│   ")
        print()  # blank line between directories

