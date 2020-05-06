import zeep
import json
import hashlib
from pathlib import Path

# from zeep import Client

from modules.helpers import cache
from modules.helpers.logger import log
from modules.helpers.logger import should_log
from modules.helpers.progress_bar import print_percent_done
from modules.helpers.export import export_results

email = "si485@dispostable.com"
password = "si485@dispostable"

wsdl = "https://www.brenda-enzymes.org/soap/brenda_zeep.wsdl"
password = hashlib.sha256(password.encode("utf-8")).hexdigest()
client = zeep.Client(wsdl)


def brendaSOAP(parameters, fn_name):
    fn = client.service[fn_name]
    client.settings.strict = True
    return cache.brenda_cached_reqest(
        request_name=f"brenda_{fn_name}", params=parameters, request_fn=fn
    )


def getSynonyms(ecNumber):
    parameters = (
        email,
        password,
        f"ecNumber*{ecNumber}",
        "organism*",
        "synonyms*",
        "commentary*",
        "literature*",
    )
    resp = brendaSOAP(parameters, "getSynonyms")
    return sorted({synonym["synonyms"] for synonym in resp})


def getReactions(ecNumber):
    parameters = (
        email,
        password,
        f"ecNumber*{ecNumber}",
        "reaction*",
        "commentary*",
        "literature*",
        "organism*",
    )
    resp = brendaSOAP(parameters, "getReaction")
    return sorted({reaction["reaction"] for reaction in resp})


def getSystematicName(ecNumber):
    parameters = (
        email,
        password,
        f"ecNumber*{ecNumber}",
        "organism*",
        "systematicName*",
    )
    resp = brendaSOAP(parameters, "getSystematicName")
    # there should be only one sysname per entry
    return resp[0]["systematicName"]


def getSubstrate(ecNumber):
    parameters = (
        email,
        password,
        f"ecNumber*{ecNumber}",
        "organism*",
        "substrate*",
        "reactionPartners*",
        "ligandStructureId*",
    )
    resp = brendaSOAP(parameters, "getSubstrate")
    return sorted({substrate["substrate"] for substrate in resp if substrate != "more"})


def getProduct(ecNumber):
    parameters = (
        email,
        password,
        f"ecNumber*{ecNumber}",
        "organism*",
        "product*",
        "reactionPartners*",
        "ligandStructureId*",
    )
    resp = brendaSOAP(parameters, "getProduct")
    return sorted({product["product"] for product in resp if product != "?"})


def getPdb(ecNumber):
    parameters = (email, password, f"ecNumber*{ecNumber}", "organism*", "pdb*")
    resp = brendaSOAP(parameters, "getPdb")
    return sorted({pdb["pdb"] for pdb in resp})


def validate_ec(ecNumber):
    """removing ec: from the string as brenda doesn't accept it"""
    if "B" in ecNumber:
        return None
    elif "ec:" in ecNumber:
        return ecNumber.replace("ec:", "")
    else:
        return ecNumber


def create_brenda_ec_entry(ec):
    return {
        "SYSNAME": getSystematicName(ec),
        "REACTIONS": getReactions(ec),
        "SYNONYMS": getSynonyms(ec),
        "SUBSTRATE": getSubstrate(ec),
        "PRODUCT": getProduct(ec),
        "PDB": getPdb(ec),
        "EC_NUMBER": ec,
    }


def get_all_data(fetch_list):
    data_dict = {}
    for index, ec in enumerate(fetch_list):
        # formatting the ec number correctly and skipping if it has letter B in it
        ec = validate_ec(ec)

        if not ec:
            continue

        log(f"Scraping data for {ec} ...", verbosity="debug")
        try:
            # getting the data for ec number
            entry = create_brenda_ec_entry(ec)
            id = "ec:" + ec
            data_dict[id] = entry
        except Exception as e:
            log(f"couldn't scrape info for {ec}", "warning")
            log(f"Error: {e}", "debug")
            continue

        # progress bar
        print_percent_done(
            index=index, total=len(fetch_list), title="Scraping Brenda, please wait...",
        )

    log(f"Successfully scraped {len(data_dict)} enzymes from Brenda", "success")
    return data_dict


def brenda_scrape(fetch_list):
    if len(fetch_list) > 0:
        new_data = get_all_data(fetch_list)

        # Writing out the results to the file
        export_results(new_data, path="export/brenda.json")

        # returning new data
        return new_data
    else:
        log(
            "Doesn't look like there are any new flavins to fetch from Brenda!",
            "success",
        )
        return {}
