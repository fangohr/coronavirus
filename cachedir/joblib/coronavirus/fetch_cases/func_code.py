# first line: 71
@joblib_memory.cache
def fetch_cases():
    url = os.path.join(base_url, "time_series_covid19_" + "confirmed" + "_global.csv")
    df = pd.read_csv(url, index_col=1)
    report_download(url, df)
    fetch_cases_last_execution()
    return df
