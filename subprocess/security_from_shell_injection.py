import os
import subprocess

# Опасный подход - передача пользовательского ввода
user_input = "malicious; rm -rf /"
os.system(f"echo {user_input}")  # ❌ Опасность!

# C subprocess
subprocess.run(["echo", user_input]) # ✅ Безопасно