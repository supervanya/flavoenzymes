# caching impolementation for the API requests
import requests
import json
import zeep

# trurn this off to remove debugginf print statements
DEBUG = True
CACHING = True


# <----- CACHING TO FILE ----->
CACHE_FNAME = 'export/cache.json'

def cache_init():
    try:
        cache_file = open(CACHE_FNAME, 'r')
        cache_contents = cache_file.read()
        CACHE_DICTION = json.loads(cache_contents)
        cache_file.close()
        if DEBUG == True:
            print("found JSON cache")
        return CACHE_DICTION

    # if there was no file, no worries. There will be soon!
    except:
        CACHE_DICTION = {}
        return CACHE_DICTION

    # A helper function that accepts 2 parameters
    # and returns a string that uniquely represents the request
    # that could be made with this info (url + params)

CACHE_DICTION = cache_init()



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
def cached_reqest(baseurl, params=None, auth=None, headers=None):
    unique_ident = params_unique_combination(baseurl, params)
#     print(unique_ident)
#     print(CACHE_DICTION)

    # first, look in the cache to see if we already have this data
    if unique_ident in CACHE_DICTION and CACHING:
        if DEBUG == True:
            print("Getting cached data...")
            print(unique_ident)
        return CACHE_DICTION[unique_ident]

    # if not, fetch the data afresh, add it to the cache,
    # then write the cache to file
    else:
        # Make the request and cache the new data
        if auth == None:
            resp = requests.get(baseurl, params, headers=headers)
        else:
            resp = requests.get(baseurl, params=params, auth=auth, headers=headers)

        if DEBUG == True:
            print("Making a request for new data...")
            print(resp.url)
        CACHE_DICTION[unique_ident] = resp.text
        dumped_json_cache = json.dumps(CACHE_DICTION)
        fw = open(CACHE_FNAME, "w")
        fw.write(dumped_json_cache)
        fw.close()  # Close the open file
        return CACHE_DICTION[unique_ident]

def generic_cached_reqest(request_name, params, request_fn):
    unique_ident = params_unique_combination(baseurl=request_name, params={ p:p for p in params })
    
    # first, look in the cache to see if we already have this data
    if unique_ident in CACHE_DICTION and CACHING:
        if DEBUG == True:
            print("Getting cached data...")
            print(unique_ident)
        return CACHE_DICTION[unique_ident]
    
    # if not, fetch it
    if DEBUG == True:
            print("Making a request for new data...")
            print(f'{request_name}, params: {json.dumps(params)}') 
    resp = request_fn(*params)
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


