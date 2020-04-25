'''

'''
import os
from os import path
import platform
import subprocess

# def activate_venv(venv_path):
#     print('activating virtualenv')
#     activate_this_file = f'{venv_path}/bin/activate_this.py'
#     exec(compile(open(activate_this_file, 'rb').read(), activate_this_file, 'exec'), dict(__file__=activate_this_file))
#     print('virtualenv activated')

def execute_system_command(command, show_command=True, show_output=True):
    if show_command:
        print(command)

    output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)

    # Convert from bytes to string
    output = str(output, 'utf-8')
    output = output.strip()

    if show_output:
        print(output)

    return output


def print_os_info():
    print(os.name)
    print(f'{platform.system()}\t{platform.release()}')


def create_venv(venv_path):
    '''
    venv_path: this must be a path, don't screw this up, yo!
    '''
    execute_system_command(f'python3 -m venv {venv_path}')
    # execute_system_command(f'virtualenv {venv_path}')
    # execute_system_command(f'source {venv_path}/bin/activate')



def check_for_virtual_env(venv_dir_name='flavo_venv'):
    # https://stackoverflow.com/a/58026969/872328
    running_in_virtualenv = "VIRTUAL_ENV" in os.environ
    print(f'Currently running in venv? {running_in_virtualenv}')

    # alternative ways to write this, also supporting the case where
    # the variable is set but contains an empty string to indicate
    # 'not in a virtual environment':
    # running_in_virtualenv = bool(os.environ.get("VIRTUAL_ENV"))
    # running_in_virtualenv = bool(os.getenv("VIRTUAL_ENV"))

    cwd = os.getcwd()
    print(cwd)
    
    # venv_dir_name = 'ENV'
    venv_path = path.join(cwd, venv_dir_name)
    print(f'Checking {venv_path}')
    venv_path_exists = path.exists(venv_path)
    if venv_path_exists:
        print(f'Virtual environment path does exist! 🎉')
    else:
        print(f'Virtual environment path does not exist! ❌')

    return venv_path_exists, venv_path


def main():
    print_os_info()
    venv_path_exists, venv_path = check_for_virtual_env('flavo_env3')
    if not venv_path_exists:
        create_venv(venv_path)
        check_for_virtual_env(venv_path)

    # if Windows

    # If posix
    print(f'Now run "source {}"')

    # activate_venv(venv_path)
    # requirements_file_path = 'requirements.txt'
    # execute_system_command(f'pip3 install -r {requirements_file_path}')

    # activate
    # install
    

if __name__ == '__main__':
    print('This script should ensure you have a functioning Python environment to run FLAVOENZYME SCRAPER')
    main()