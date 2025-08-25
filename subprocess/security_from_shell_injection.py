user_input = "malicious; rm -rf /"

''' Опасный подход - передача пользовательского ввода '''
import os

os.system(f"echo {user_input}")  		# ❌ Опасность!
# $echo malicious;
# $rm -rf /


''' C subprocess - исключаем shell injection '''
import subprocess
subprocess.run(["echo", user_input]) 	# ✅ Безопасно
# $echo "malicious; rm -rf /"