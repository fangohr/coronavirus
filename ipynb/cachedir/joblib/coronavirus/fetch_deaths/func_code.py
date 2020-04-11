# first line: 62
@joblib_memory.cache
def fetch_deaths():
    url = os.path.join(base_url, "time_series_covid19_" + "deaths" + "_global.csv")
    df = pd.read_csv(url, index_col=1)
    report_download(url, df)
    fetch_deaths_last_execution()
    return df
