import subprocess

# Выполним 'ls -la' и получим результат
result = subprocess.run(['ls', '-la'], capture_output=True, text=True)

# Команда выполнена? (код возврата 0 обычно означает успех)
print('Return code:', result.returncode)

# Что команда вывела в stdout?
print('Output:', result.stdout)

# Были ошибки? (stderr)
if result.stderr:
    print('Errors:', result.stderr)