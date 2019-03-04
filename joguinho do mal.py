import shlex, subprocess

# Exit string options, parsed to lower
exits = (option.lower() for option in ("Exit", "0", "Sair"))

# Initialize the subprocess list
running_subprocess_list = list()

while True:
    # Get users command
    cmd = input("Digite o comando que você deseja executar:\n")
    
    # Verify if it isn't a exit command
    if cmd.lower() in exits:
        # Verify if exists subprocess alive
        for running_subprocess in running_subprocess_list:
            if running_subprocess and running_subprocess.pull() is None:
                # If subprocess is alive, terminate the subprocess
                running_subprocess.kill()
        break
    # Parse the command
    cmd = shlex.split(cmd)
    try:
        # Try to execute the command
        # This part needs more love to find programs that aren't in the PATH
        running_subprocess = subprocess.Popen(cmd)
        # Add the command to subprocess list
        running_subprocess_list.append(running_subprocess)
    except:
        print("Comando inválido")
