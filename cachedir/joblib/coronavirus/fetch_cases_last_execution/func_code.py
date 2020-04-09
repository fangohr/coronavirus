# first line: 57
@joblib_memory.cache
def fetch_cases_last_execution():
    return datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
