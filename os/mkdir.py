import os

# Где будем хранить логи
path_to_dir = f'{os.getcwd()}/logs/my_app'

# Проверяем, существует ли директория
if not os.path.exists(path_to_dir):
    os.makedirs(path_to_dir)
    print(f'Директория {path_to_dir} успешно создана!')
else:
    print(f'Директория {path_to_dir} уже существует.')