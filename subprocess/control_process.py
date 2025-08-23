# Плохой подход - использование os.system()
# import os
# os.system("docker ps")  # ❌ Нет контроля над выводом и ошибками

# использование subprocess
import subprocess

result = subprocess.run(
    ["docker", "ps"],
    capture_output=True,
    text=True,
    check=True
)
print(result.stdout)