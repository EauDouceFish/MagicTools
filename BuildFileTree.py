import os
import sys

def generate_tree(start_path, prefix='', only_dirs=False):
    entries = sorted(os.listdir(start_path))
    tree_str = ''
    for index, entry in enumerate(entries):
        path = os.path.join(start_path, entry)
        if only_dirs and not os.path.isdir(path):
            continue
        connector = '└── ' if index == len(entries) - 1 else '├── '
        tree_str += prefix + connector + entry + '\n'
        if os.path.isdir(path):
            extension = '    ' if index == len(entries) - 1 else '│   '
            tree_str += generate_tree(path, prefix + extension, only_dirs)
    return tree_str

def main():
    args = [arg.lower() for arg in sys.argv[1:]]

    if '-s' in args:
        only_dirs = True
    elif '-c' in args:
        only_dirs = False
    else:
        # 没有参数时提示用户输入
        mode = input("选择模式：(C)omplete 完整模式 / (S)implified 只显示文件夹：").strip().lower()
        only_dirs = (mode == 's')

    output_file = "directory_structure.txt"
    root_dir = os.getcwd()

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f"Directory structure of: {root_dir} (mode: {'Simplified' if only_dirs else 'Complete'})\n\n")
        f.write(generate_tree(root_dir, only_dirs=only_dirs))

    print(f"目录结构已导出到 {output_file}")

if __name__ == "__main__":
    main()
