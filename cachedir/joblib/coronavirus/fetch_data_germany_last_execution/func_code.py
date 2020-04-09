# first line: 153
@joblib_memory.cache
def fetch_data_germany_last_execution():
    return datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
