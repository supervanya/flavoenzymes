import bioservices
from modules.helpers.logger import log

k = bioservices.kegg.KEGG()
parser = bioservices.kegg.KEGGParser()

def get_ids(keyword):
    log(f'fetching enzymes for {keyword}','info')
    results = k.find(database='enzyme', query=keyword)
    results_array = results.split('\n')
    ids_array = [i.split('\t')[0] for i in results_array if (i)]
    return set(ids_array)

def get_ids_for_keywords(keywords):
    all_ids_set = set()
    for keyword in keywords:
        kw_ids = get_ids(keyword)
        all_ids_set = all_ids_set | kw_ids
    return all_ids_set

def kegg_search(keywords):
    # Getting IDs of all entries that are matching keywords
    new_ids = get_ids_for_keywords(keywords)
    return new_ids