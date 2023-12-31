from api.api import get_data
from datetime import datetime

TABLE_NAME = "sv_arret_p"

def load_sv_arret_p(start_date = None):
    query_params = { }
    
    if start_date is not None:
        query_params["backintime"] = start_date.strftime("%Y-%m-%dT%H:%M:%SZ")

    result = get_data(TABLE_NAME, query_params)
    return result
