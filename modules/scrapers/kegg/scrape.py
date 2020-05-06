import re
import bioservices

from modules.helpers.logger import log
from modules.helpers.logger import should_log
from modules.helpers.progress_bar import print_percent_done
from modules.helpers.export import export_results
from modules.helpers import cache

parser = bioservices.kegg.KEGGParser()


def kegg_request(id):
    resp = cache.kegg_cached_reqest(request_name=f"kegg_ec_request", ec=id)
    ec_parse = parser.parse(resp)
    if "SUBSTRATE" in ec_parse.keys():
        ec_parse["SUBSTRATE"] = get_compounds_with_smiles(ec_parse["SUBSTRATE"])
        ec_parse["PRODUCT"] = get_compounds_with_smiles(ec_parse["PRODUCT"])
    return ec_parse


def get_compounds_with_smiles(list_of_compounds):
    new_compounds = {}
    pattern = "(.+) \[CPD:(.+)\]"

    for compound in list_of_compounds:
        compound = compound.replace(";", "")  # this will be the full name
        name = compound  # this will be the short name
        smiles_str = None
        cpd_number = None

        if "CPD" in compound:
            # this breaks the strings like "4-hydroxybenzoate [CPD:C00156];"
            # into an array of tuples like this: [('4-hydroxybenzoate', 'C00156')]
            match = re.findall(pattern, name)[0]

            # constructing the cpd number, it must be like "cpd:C00156"
            name = match[0]
            cpd_number = "cpd:" + match[1]
            try:
                smiles_str = cache.get_smile_string(cpd_number)
                log(
                    f"compound:{name}, cpd_number:{cpd_number},name:{name},smiles: {smiles_str}",
                    "debug",
                )
                if not smiles_str:
                    raise Exception(
                        f"Compound: {cpd_number} does not have a SMILES string."
                    )
            except Exception as e:
                log(f"{e}", "debug")
                continue
        else:
            name = compound
            log(f'⚠️ Compound "{compound}" is missing a CPD number', "debug")

        new_compounds[name] = {
            "name": name,
            "smiles": smiles_str,
            "kegg_name": compound,
            "kegg_id": cpd_number,
        }
    return new_compounds


def get_all_data(fetch_list):
    data_dict = {}

    log(f"Getting data for following IDs - {fetch_list}", "debug")
    for index, id in enumerate(fetch_list):
        try:
            ec_data = kegg_request(id)
        except Exception as e:
            log(f"Kegg. Can't fetch {id} ", "warning")
            log(f"Error: {e}", "debug")
            continue

        # if sysname not found, will use ec_number
        name = ec_data.get("SYSNAME", id)
        ec_number = id.replace("ec:", "")

        ec_data["KEGG_ID"] = id
        ec_data["EC_NUMBER"] = ec_number
        data_dict[id] = ec_data

        log(f"Scraping data for - {ec_number}", "debug")
        log(f"Getting following data - {data_dict[id]}", "silly")
        # progress bar
        print_percent_done(
            index=index, total=len(fetch_list), title="Scraping Kegg, please wait..."
        )

    return data_dict


def kegg_scrape(fetch_list):
    log(f"Kegg scraping script started...", "info")

    # If new ids have been found, fetch the data
    if len(fetch_list) > 0:
        log(f"Following potential flavins are missing from past results:", "info")
        [log(f"\t{ec}", "info") for ec in fetch_list]

        # Scraping the data
        log(f"Scraping the data", "info")
        flavins = get_all_data(fetch_list)
        log(f"Successfully scraped {len(fetch_list)} enzymes from Kegg", "success")

        # Writing out the results to the file
        export_results(flavins, "export/kegg.json")
        return flavins
    else:
        log(
            "Doesn't look like there are any new flavins to fetch from KEGG!", "success"
        )
        return {}
