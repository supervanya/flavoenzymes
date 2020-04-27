import pandas as pd
from pathlib import Path

from modules.helpers import logger
from modules.scrapers.kegg.search import kegg_search 
from modules.scrapers.brenda.search import brenda_search


def create_fetch_list(prev_list, kegg_keywords, brenda_keywords):
    '''prev_list must be set() | returns a set()'''
    whitelist_path = Path('modules/scrapers/whitelist.csv')
    blacklist_path = Path('modules/scrapers/blacklist.csv')
    
    white_list   = set(pd.read_csv(whitelist_path)['ec'])
    black_list   = set(pd.read_csv(blacklist_path)['ec'])
    brenda_list  = brenda_search(brenda_keywords)
    kegg_list    = kegg_search(kegg_keywords)
    new_list     = brenda_list|kegg_list # this are all the results that came back from kegg and brenda

    # combining the lists
    master_list = (white_list|new_list)-(prev_list|black_list)
    return master_list