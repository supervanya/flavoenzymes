import pandas as pd
from pathlib import Path

from modules.helpers import logger
from modules.scrapers.kegg import search as search_kegg
from modules.scrapers.brenda import search as search_brenda


def create_fetch_list(prev_list):
    '''prev_list must be set() | returns a set()'''
    whitelist_path = Path('modules/scrapers/whitelist.csv')
    blacklist_path = Path('modules/scrapers/blacklist.csv')
    
    white_list   = set(pd.read_csv(whitelist_path)['ec'])
    black_list   = set(pd.read_csv(blacklist_path)['ec'])
    brenda_list  = search_brenda()
    kegg_list    = search_kegg()
    new_list     = brenda_list|kegg_list # this are all the results that came back from kegg and brenda

    # combining the lists
    master_list = (white_list|new_list)-(prev_list|black_list)
    return master_list