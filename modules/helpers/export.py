from pathlib import Path
from modules.helpers.logger import log
import json


def read_json_data(path):
    try:
        with open(path) as json_file:
            return json.load(json_file)
    except:
        return {}


def export_results(new_data, path):
    """This will append the data to the previous results, overriding any old entries with new ones """
    data_path = Path(path)
    past_data = read_json_data(data_path)

    combined = {
        **past_data,
        **new_data,
    }

    with open(data_path, "w") as of:
        json.dump(combined, of)
