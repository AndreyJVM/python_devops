with open('output.log', 'w') as log_file:
    result = subprocess.run(
        ['some_script.sh'],
        stdout=log_file,  # stdout уйдет в файл
        stderr=subprocess.PIPE,  # stderr мы захватим отдельно
        text=True
    )
    print('Errors during execution:', result.stderr)