import re
import bioservices

from modules.helpers.logger import log 
from modules.helpers.logger import should_log 
from modules.helpers.progress_bar import print_percent_done
from modules.helpers import cache

parser = bioservices.kegg.KEGGParser()

def kegg_request(id):
    resp = cache.kegg_cached_reqest(request_name=f'kegg_ec_request', ec=id)
    ec_parse = parser.parse(resp)
    if 'SUBSTRATE' in ec_parse.keys():
        ec_parse['SUBSTRATE'] = get_compounds_with_smiles(ec_parse['SUBSTRATE'])
        ec_parse['PRODUCT'] = get_compounds_with_smiles(ec_parse['PRODUCT'])
    return ec_parse


def get_compounds_with_smiles(list_of_compounds):
    new_compounds = {}
    pattern = '(.+) \[CPD:(.+)\]'

    for compound in list_of_compounds:
        compound = compound.replace(';','') # this will be the full name
        name = compound # this will be the short name
        smiles_str = None
        cpd_number = None
        
        if 'CPD' in compound:
            # this breaks the strings like "4-hydroxybenzoate [CPD:C00156];" 
            # into an array of tuples like this: [('4-hydroxybenzoate', 'C00156')]
            match = re.findall(pattern, name)[0]
            
            # constructing the cpd number, it must be like "cpd:C00156"
            name = match[0]
            cpd_number = 'cpd:' + match[1]
            try:
                smiles_str = cache.get_smile_string(cpd_number)
                log(f"compound:{name}, cpd_number:{cpd_number},name:{name},smiles: {smiles_str}\n\n", 'debug')
                if not smiles_str:
                    raise Exception(f'Compound: {cpd_number} does not have a SMILES string.')
            except Exception as e:
                log(f"{e}", 'debug')
                continue
        else:
            name = compound
            log(f'⚠️ Compound "{compound}" is missing a CPD number', 'debug')
            
        new_compounds[name] = {
                'name': name,
                'smiles': smiles_str,
                'kegg_name': compound,
                'kegg_id': cpd_number
            }
    return new_compounds


def get_all_data(ids, verbose=False):    
    data_dict = {}
    
    log(f'Getting data for following IDs - {ids}', 'debug')
    for index,id in enumerate(ids):
        ec_data = kegg_request(id)
        name = ec_data.get('SYSNAME', id) # if sysname not found, will use ec_number
        ec_number = id.replace('ec:','')
        
        ec_data['KEGG_ID'] = id
        ec_data['EC_NUMBER'] = ec_number
        data_dict[ec_number] = ec_data
        
        log(f'Getting following data - {data_dict[ec_number]}', 'silly')
        if should_log(message_verbosity='info'):
            print_percent_done(index=index, total=len(ids), title="Scraping Kegg, please wait")
            
    return data_dict


def kegg_scrape(fetch_list):
    log(f'1. Kegg scraping script started...','info')

    all_ids = fetch_list
                
    # If new ids have been found, fetch the data
    if len(all_ids) > 0:
        log(f'2. Following potential flavins are missing from past results:','info')
        if should_log('info'):
            [print(f'- {ec}') for ec in all_ids]
    
        # Scraping the data
        log(f'\n3. Fetching the data','info')
        flavins = get_all_data(all_ids, verbose=True)
        
        log(f'\nSuccessfully fetched {len(all_ids)} enzymes from Kegg','success')
        return flavins

        # Writing out the results to the file
        # with open(export_file, 'w') as outfile:
        #     json.dump(flavins, outfile)
    else:
        log("Doesn't look like there are any new flavins to fetch from KEGG!",'info')
