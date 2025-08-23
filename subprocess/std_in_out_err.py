import subprocess

# Чтение вывода построчно в реальном времени
process = subprocess.Popen(
    ["tail", "-f", "/var/log/app.log"],
    stdout=subprocess.PIPE,
    text=True
)

for line in process.stdout:
    print(f"LOG: {line.strip()}")
    # ✅ Обработка в реальном времени, не дожидаясь завершения