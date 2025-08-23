import subprocess

try:
    result = subprocess.run(
        ["slow-command"],
        timeout=30,  # ✅ Автоматическое прерывание
        capture_output=True
    )
except subprocess.TimeoutExpired:
    print("Команда превысила лимит времени")
    # ✅ Можно убить процесс при необходимости