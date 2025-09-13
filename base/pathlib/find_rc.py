import os
import pathlib # pathlib позволяет представлять пути в виде объектов, а не строк.


def find_rc(rc_name=".exemplerc"):

    # Check environ
    var_name = "EXAMPLERC_DIR"
    example_dir = os.environ.get(var_name)
    if example_dir:
        dir_path = pathlib.Path(example_dir)
        config_path = dir_path / rc_name
        print(f"Checking {config_path}")
        if config_path.exists():
            return config_path.as_posix()

    # Ищем в текущем рабочем каталоге
    config_path = pathlib.Path.cwd() / rc_name    
    print(f"Checking {config_path}")
    if config_path.exists():
        return config_path.as_posix()
    
    # Ищем в домашнем каталоге пользователя
    config_path = pathlib.Path.home() / rc_name    
    print(f"Checking {config_path}")
    if config_path.exists():
        return config_path.as_posix()
    
    # Ищем в каталоге выполняемого файла
    file_path = pathlib.Path(__file__).resolve()
    parent_path = file_path.parent
    config_path = parent_path / rc_name 
    print(f"Checking {config_path}")
    if config_path.exists():
        return config_path.as_posix()
    
    print(f"File {rc_name} has not been found")