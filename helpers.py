from GLOBALS import VERBOSITY
from datetime import datetime


# ========== LOGGING ===========
verbosity_to_levels = {
    'none': 0,
    'error': 1,
    'warning': 2,
    'info': 3,
    'debug': 4,
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
        print(f'{current_time} [{verbosity}]: {message}')
        
def should_log(verbosity):
    print(f'verbosity{verbosity}, VERBOSITY{VERBOSITY}')
    message_level = verbosity_to_levels[verbosity]
    global_level = verbosity_to_levels[VERBOSITY]
    
    if message_level <= global_level:
        return True
    return False
