import pandas as pd
from pathlib import Path
import json

from modules.helpers.logger import log
from modules.scrapers.kegg.search import kegg_search
from modules.scrapers.brenda.search import brenda_search

from modules.scrapers.kegg.scrape import kegg_scrape
from modules.scrapers.brenda.scrape import brenda_scrape
from modules.helpers.export import export_results
from GLOBALS import SCRAPE_OUTPUT_PATH


def read_json_data(path):
    try:
        with open(path) as json_file:
            return json.load(json_file)
    except:
        return {}


def write_out(new_data):
    export_results(new_data, SCRAPE_OUTPUT_PATH)
    log(
        f"{len(new_data)} enzymes have been written out to {Path(SCRAPE_OUTPUT_PATH).absolute()}",
        "success",
    )


def list_past_results():
    prev_export_path = Path(SCRAPE_OUTPUT_PATH)
    past_data = read_json_data(prev_export_path)
    past_ecs_set = set(past_data.keys())
    return past_ecs_set


def combine_data(kegg_data, brenda_data):
    # combinging two dictionaries, this will override any enzymes with kegg
    combined = {
        **brenda_data,
        **kegg_data,
    }

    # adding brenda data back in
    for enzyme_name in brenda_data.keys():
        kegg_e = kegg_data.get(enzyme_name, {})
        brenda_e = brenda_data.get(enzyme_name, {})
        combined[enzyme_name] = {**brenda_e, **kegg_e}

    if not combined:
        return {}
    return combined


def create_missing_list(kegg_keywords, brenda_keywords):
    """kegg_keywords and brenda_keywords must be a list | returns a set()"""
    whitelist_path = Path("modules/scrapers/whitelist.csv")
    blacklist_path = Path("modules/scrapers/blacklist.csv")

    # makeing the sets of ECs
    white_list = set(pd.read_csv(whitelist_path)["ec"])
    black_list = set(pd.read_csv(blacklist_path)["ec"])
    brenda_list = brenda_search(brenda_keywords)
    kegg_list = kegg_search(kegg_keywords)
    prev_list = list_past_results()
    new_list = brenda_list | kegg_list

    # combining the lists
    # note: the parentecies are crucial here for order of operations
    master_list = (new_list | white_list) - (prev_list | black_list)

    # Logging the lists for debugging purposes
    log(f"white_list len: {len(white_list)}", "debug")
    log(f"black_list len: {len(black_list)}", "debug")
    log(f"prev_list len: {len(prev_list)}", "debug")
    log(f"brenda_list len: {len(brenda_list)}", "debug")
    log(f"kegg_list len: {len(kegg_list)}", "debug")
    log(f"new_list len: {len(new_list)} will be used", "debug")
    log(f"master_list len: {len(master_list)}", "debug")
    return master_list


def scrape_all(list_of_ecs):
    kegg_data = kegg_scrape(list_of_ecs)
    brenda_data = brenda_scrape(list_of_ecs)
    combined_data = combine_data(kegg_data, brenda_data)
    return combined_data
