# こちら使用不要、update_markdown.pyに移行

from . import file_operation
from . import split_file
from . import update_markdown
from . import update_file


def main():

    target_files_Path = file_operation.process_files_Path()
    backup_dir_path = str(file_operation.backup_dir_Path())

    file_operation.reset_dir(backup_dir_path)

    for file_Path in target_files_Path:
        if not file_Path.is_file():
            continue

        file_path = str(file_Path)

        header, mermeid, footer = split_file.split_file(file_path)

        new_lines = update_markdown.add_link(header, mermeid, footer)

        update_file(new_lines, file_path, backup_dir_path)


if __name__ == "__main__":
    main()