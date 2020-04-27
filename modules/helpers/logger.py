from datetime import datetime
from colorama import Fore, Back, Style, init, deinit

from GLOBALS import VERBOSITY

# ========== LOGGING ===========
verbosity_to_levels = {
    'none': 0,
    'success': 1,
    'error': 2,
    'warning': 3,
    'info': 4,
    'debug': 5,
    'silly': 6,
}

verbosity_to_color = {
    'none':    'none',
    'success': f'{Fore.GREEN}✔success{Fore.RESET}',
    'error':   f'{Fore.RED}⨯error{Fore.RESET}',
    'warning': f'{Fore.YELLOW}⚠warning{Fore.RESET}',
    'info':    f'{Fore.GREEN}ℹinfo{Fore.RESET}',
    'debug':   f'{Fore.BLUE}•debug{Fore.RESET}',
    'silly':   f'{Fore.MAGENTA}~silly{Fore.RESET}',
    }

def log(message, verbosity):
    if should_log(verbosity):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        verb_color = verbosity_to_color[verbosity]
        print(f'{current_time} [{verb_color}]\t{message}')
        
def should_log(message_verbosity):
    # print(f'verbosity: {message_verbosity}, VERBOSITY: {VERBOSITY}')
    message_level = verbosity_to_levels[message_verbosity]
    global_level = verbosity_to_levels[VERBOSITY]
    
    if message_level <= global_level:
        return True
    return False