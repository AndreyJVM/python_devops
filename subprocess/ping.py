import subprocess

host = "vk.com"

# Выполняем ping (параметр -c 4 для Linux/Mac, для Windows используй -n 4)
result = subprocess.run(
    ['ping', '-c', '4', host],
    capture_output=True,
    text=True
)

if result.returncode == 0:
    print(f"✅ Хост {host} доступен!")
    # Можно распарсить result.stdout и вывести среднее время, например
else:
    print(f"❌ Хост {host} не отвечает.")
    print(result.stderr)