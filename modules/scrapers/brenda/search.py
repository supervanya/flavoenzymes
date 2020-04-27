import pandas as pd
import requests
from io import StringIO

from modules.helpers.logger import log

def brenda_request(url):
    headers = {
      "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
      "X-Requested-With": "XMLHttpRequest"
    }
    log(f'Making a request: {url}','debug')
    response = requests.get(url, headers=headers)
    return response.text
    

def search_ligands_brenda(term):
    columns = ['Ligand','EC Number', 'Role', 'Id', 'Structure', 'Discard']
    url = f'https://www.brenda-enzymes.org/result_download.php?a=13&RN=&RNV=1&os=1&pt=&FNV=1&tt=&SYN=&Textmining=&T[0]=2&T[1]=2&V[1]=1&V[2]=2&W[3]={term}&T[3]=2&nolimit=1'
    response = brenda_request(url)
    df = pd.read_csv(StringIO(response), sep='\t', names=columns)
    return df


def search_enzymes_brenda(term):
    columns = ['EC Number', 'Recommended Name', 'Synonyms', 'Commentary', 'Discard']
    url = f'https://www.brenda-enzymes.org/result_download.php?a=9&RN=&RNV=1&os=1&pt=&FNV=&tt=&SYN=&Textmining=&T[0]=2&T[1]=2&W[2]={term}&T[2]=2&nolimit=1'    
    response = brenda_request(url)
    df = pd.read_csv(StringIO(response), sep='\t', names=columns)
    return df


def brenda_get_enzyme_data(id):
    link = f'https://www.brenda-enzymes.info/enzyme.php?ecno={id}#NATURAL%20SUBSTRATE'
    response = brenda_request(link)
    return response


def search_all_terms(terms, search_fn):
    all_dfs = []

    for term in terms:
        df = search_fn(term)
        if (len(df) < 2):
            print(f'[!] skipping search for {term} since nothing was found')
            continue
        else:
            all_dfs.append(df)
    return pd.concat(all_dfs)


def brenda_search(keywords):
    enzymes_list = set(search_all_terms(keywords,search_enzymes_brenda)['EC Number'])
    ligands_list = set(search_all_terms(keywords,search_ligands_brenda)['EC Number'])

    ec_set = enzymes_list | ligands_list
    log(f'total ecs found: {len(ec_set)}','info')

    return ec_set