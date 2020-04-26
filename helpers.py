from GLOBALS import VERBOSITY
from datetime import datetime
from colorama import Fore, Back, Style, init, deinit


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
    'success': f'{Fore.GREEN}✔ SUCCESS{Fore.RESET}',
    'error':   f'{Fore.RED}⨯ ERROR{Fore.RESET}',
    'warning': f'{Fore.YELLOW}⚠ WARNING{Fore.RESET}',
    'info':    f'{Fore.GREEN}ℹ INFO{Fore.RESET}',
    'debug':   f'{Fore.BLUE}• DEBUG{Fore.RESET}',
    'silly':   f'SILLY'
    }

def print_percent_done(index, length):
    percent_done = round((index+1)/length*100)
    done = (percent_done/10)
    done_str = '█'*int(done)
    togo = (10-(percent_done/10))
    togo_str = '░'*int(togo)
    print(f'\n\n----> Progress: {done_str}{togo_str} \t{percent_done}% done')


def log(message, verbosity):
    if should_log(verbosity):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        verb_color = verbosity_to_color[verbosity]
        print(f'{current_time} [{verb_color}]:\t{message}')
        
def should_log(message_verbosity):
    # print(f'verbosity: {message_verbosity}, VERBOSITY: {VERBOSITY}')
    message_level = verbosity_to_levels[message_verbosity]
    global_level = verbosity_to_levels[VERBOSITY]
    
    if message_level <= global_level:
        return True
    return False
