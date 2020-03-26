def print_percent_done(index, length):
    percent_done = round((index+1)/length*100)
    done = (percent_done/10)
    done_str = '█'*int(done)
    togo = (10-(percent_done/10))
    togo_str = '░'*int(togo)
    print(f'\n\n----> Progress: {done_str}{togo_str} \t{percent_done}% done')
