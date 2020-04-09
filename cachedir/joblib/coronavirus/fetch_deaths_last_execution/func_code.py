# first line: 51
@joblib_memory.cache
def fetch_deaths_last_execution():
    """Use to remember at what time and date the last set of deaths was downloaded"""
    return datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
