import pandas as pd
import requests
from io import StringIO

from modules.helpers.logger import log


def brenda_request(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
    }
    log(f"Making a request: {url}", "debug")
    response = requests.get(url, headers=headers)
    return response.text


def search_ligands_brenda(term):
    columns = ["Ligand", "EC Number", "Role", "Id", "Structure", "Discard"]
    url = f"https://www.brenda-enzymes.org/result_download.php?a=13&RN=&RNV=1&os=1&pt=&FNV=1&tt=&SYN=&Textmining=&T[0]=2&T[1]=2&V[1]=1&V[2]=2&W[3]={term}&T[3]=2&nolimit=1"
    response = brenda_request(url)
    df = pd.read_csv(StringIO(response), sep="\t", names=columns)
    if len(df) < 2:
        return None
    return set(df["EC Number"])


def search_enzymes_brenda(term):
    columns = ["EC Number", "Recommended Name", "Synonyms", "Commentary", "Discard"]
    url = f"https://www.brenda-enzymes.org/result_download.php?a=9&RN=&RNV=1&os=1&pt=&FNV=&tt=&SYN=&Textmining=&T[0]=2&T[1]=2&W[2]={term}&T[2]=2&nolimit=1"
    response = brenda_request(url)
    df = pd.read_csv(StringIO(response), sep="\t", names=columns)
    if len(df) < 2:
        return None
    return set(df["EC Number"])


def brenda_get_enzyme_data(id):
    link = f"https://www.brenda-enzymes.info/enzyme.php?ecno={id}#NATURAL%20SUBSTRATE"
    response = brenda_request(link)
    return response


def search_all_terms(terms, search_fn, db="enzymes"):
    master_list = set()

    for term in terms:
        log(f'Fetching enzymes for "{term}" on Brenda {db}-DB', "info")
        search_set = search_fn(term)
        if not search_set:
            log(f"skipping search for '{term}' on {db}-DB | no results", "warning")
            continue
        else:
            master_list = master_list | search_set

    return master_list


def brenda_search(keywords):
    enzyme_set = search_all_terms(keywords, search_enzymes_brenda, db="enzymes")
    ligand_set = search_all_terms(keywords, search_ligands_brenda, db="ligands")

    ec_set = enzyme_set | ligand_set
    ec_set = {("ec:" + ec) for ec in ec_set}
    log(f"total ecs found: {len(ec_set)}", "info")

    return ec_set
