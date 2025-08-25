import subprocess

''' ✅ Чтение вывода построчно в реальном времени '''
process = subprocess.Popen(
    ["tail", "-f", "/var/log/app.log"],
    stdout=subprocess.PIPE,
    text=True
)

''' ✅ Обработка в реальном времени, не дожидаясь завершения '''
for line in process.stdout:
    print(f"LOG: {line.strip()}")

''' ⚠️ ВНИМАНИЕ: Бесконечный цикл. try/finally блок '''