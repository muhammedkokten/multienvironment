import subprocess
import os


def create_venv():
    existing_venvs = [f'venv{i}' for i in range(1, 6)]
    new_venv_number = len(existing_venvs) + 1
    new_venv_name = f'venv{new_venv_number}'

    subprocess.run([f'python -m venv {new_venv_name}'], shell=True)


def activate_venv(venv_name):
    subprocess.run(["deactivate"], shell=True)

    venv_path = os.path.join("C:\\Users\\USER\\Desktop\\multienv", venv_name)
    activate_path = os.path.join(venv_path, "Scripts", "activate")

    activate_command = f"cmd /k {activate_path}"
    subprocess.Popen(activate_command, shell=True, text=True)
