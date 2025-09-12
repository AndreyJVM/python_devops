''' Устаревший подход - использование os.system() '''
import os
os.system("docker ps")    # ❌ Нет контроля над выводом и ошибками


''' Использование subprocess '''
import subprocess

result = subprocess.run(
    ["docker", "ps"],
    capture_output=True,  # ✅ Перехватываем input/output/error
    text=True,            # ✅ Получаем текст, а не bytes
    check=True            # ✅ Проверяем ошибки
)
# result -> CompletedProcess

''' Можем анализировать вывод! '''
print(result.returncode)
print(result.stdout)
print(result.stderr)