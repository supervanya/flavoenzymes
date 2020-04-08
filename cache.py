# caching impolementation for the API requests
import requests
import json
import zeep
import bioservices

# local imports
from GLOBALS import USE_CACHING 
from helpers import log 
from helpers import should_log 

# local instantiations
k = bioservices.kegg.KEGG()
chebi_con = bioservices.ChEBI()
map_kegg_chebi = k.conv("chebi", "compound")


# <----- CACHING TO FILE ----->
CACHE_FNAME = 'export/cache.json'

def cache_init():
    try:
        cache_file = open(CACHE_FNAME, 'r')
        cache_contents = cache_file.read()
        CACHE_DICTION = json.loads(cache_contents)
        cache_file.close()
        log("found JSON cache",'debug')
        return CACHE_DICTION

    # if there was no file, no worries. There will be soon!
    except:
        CACHE_DICTION = {}
        return CACHE_DICTION

    # A helper function that accepts 2 parameters
    # and returns a string that uniquely represents the request
    # that could be made with this info (url + params)



def params_unique_combination(baseurl, params):
    if not params:
        return baseurl
    
    alphabetized_keys = sorted(params.keys())
    res = []
    for k in alphabetized_keys:
        k.replace(" ","+")
        res.append("{}={}".format(k, params[k]))
    return baseurl + "?" + "&".join(res)

# The main cache function: it will always return the result for this
# url+params combo. However, it will first look to see if we have already
# cached the result and, if so, return the result from cache.
# If we haven't cached the result, it will get a new one (and cache it)
def cached_reqest(baseurl, params=None, auth=None, headers=None, useCaching=USE_CACHING):
    unique_ident = params_unique_combination(baseurl, params)

    # first, look in the cache to see if we already have this data
    if unique_ident in CACHE_DICTION and useCaching:
        log(f"Getting cached data...\n{unique_ident}",'debug')
        return CACHE_DICTION[unique_ident]

    # if not, fetch the data afresh, add it to the cache,
    # then write the cache to file
    else:
        # Make the request and cache the new data
        if auth == None:
            resp = requests.get(baseurl, params, headers=headers)
        else:
            resp = requests.get(baseurl, params=params, auth=auth, headers=headers)
        
        log(f"Making a request for new data...\n{resp.url}",'debug')
        
        CACHE_DICTION[unique_ident] = resp.text
        dumped_json_cache = json.dumps(CACHE_DICTION)
        fw = open(CACHE_FNAME, "w")
        fw.write(dumped_json_cache)
        fw.close()  # Close the open file
        return CACHE_DICTION[unique_ident]

def brenda_cached_reqest(request_name, params, request_fn, useCaching=USE_CACHING):
    unique_ident = params_unique_combination(baseurl=request_name, params={ p:p for p in params[2:] })
    
    # first, look in the cache to see if we already have this data
    if unique_ident in CACHE_DICTION and useCaching:
        log(f"Getting cached data...\n{unique_ident}",'debug')
        return CACHE_DICTION[unique_ident]
    
    # if not, fetch it
    log(f"Making a request for new data...\n{request_name}, params: {json.dumps(params)}",'debug')
        
    if (type(params) == str):
        resp = request_fn(params)
    elif (type(params) == dict):
        resp = request_fn(**params)
    elif (type(params) == tuple):
        resp = request_fn(*params)
    else:
        log(f'not sure how to hande parameters of type: {type(params)}','error')
        
    resp_serialized = zeep.helpers.serialize_object(resp)
    
    # add it to the cache
    CACHE_DICTION[unique_ident] = resp_serialized
    
    # TODO: currently can not serialize zeep types
    # need to pickle it
    # UPDATE: found a way using `zeep.helpers.serialize_object`
    dumped_json_cache = json.dumps(CACHE_DICTION)
    fw = open(CACHE_FNAME, "w")
    fw.write(dumped_json_cache)
    
    # Close the open file
    fw.close()
    
    return CACHE_DICTION[unique_ident]


def kegg_cached_reqest(request_name, ec, request_fn, useCaching=USE_CACHING):
    unique_ident = params_unique_combination(baseurl=request_name, params={'ec':ec})
    
    # first, look in the cache to see if we already have this data
    if unique_ident in CACHE_DICTION and useCaching:
        log(f"Getting cached data...\n{unique_ident}",'debug')
        return CACHE_DICTION[unique_ident]
    
    # if not, fetch it
    log(f"Making a request for new data...\n{request_name}, ec: {ec}",'debug')
            
            
    resp = request_fn(ec)
    
    # add it to the cache
    CACHE_DICTION[unique_ident] = resp
    
    # TODO: currently can not serialize zeep types
    # need to pickle it
    # UPDATE: found a way using `zeep.helpers.serialize_object`
    dumped_json_cache = json.dumps(CACHE_DICTION)
    fw = open(CACHE_FNAME, "w")
    fw.write(dumped_json_cache)
    
    # Close the open file
    fw.close()
    
    return CACHE_DICTION[unique_ident]


def get_smile_string(compound_id, useCaching=USE_CACHING):
    ChEBI_id = map_kegg_chebi.get(compound_id)
    unique_ident = params_unique_combination(baseurl="smile_string", params={'cpd':compound_id})

    if ChEBI_id:
        if unique_ident in CACHE_DICTION and useCaching:
            log(f"Getting cached data...\n{unique_ident}",'debug')
            return CACHE_DICTION[unique_ident]
        
        # if not, fetch it
        log(f"Making a request for new data...\ncompound_request, cpd: {compound_id}",'debug')
        
        try:
            ChEBI_id = ChEBI_id.upper()
            ChEBI_resp = chebi_con.getCompleteEntity(ChEBI_id)
            smiles_string = str(ChEBI_resp.smiles)
        except AttributeError as e:
            raise Exception(f'ChEBI_id: {ChEBI_id} does not have a SMILES string. Original Error {e}')
        except WebFault as e:
            raise Exception(f'ChEBI_id: {ChEBI_id} not found. Original Error {e}')
            
        
        CACHE_DICTION[unique_ident] = smiles_string

        # writing the file out
        dumped_json_cache = json.dumps(CACHE_DICTION)
        fw = open(CACHE_FNAME, "w")
        fw.write(dumped_json_cache)

        # Close the open file
        fw.close()
        
        return CACHE_DICTION[unique_ident]
    else:
        return None



CACHE_DICTION = cache_init()