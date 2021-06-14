import requests

url_vaccine_completed = 'https://raw.githubusercontent.com/ccodwg/Covid19Canada/master/timeseries_prov/vaccine_completion_timeseries_prov.csv'
url_vaccine_administered = 'https://raw.githubusercontent.com/ccodwg/Covid19Canada/master/timeseries_prov/vaccine_administration_timeseries_prov.csv'
url_cases='https://raw.githubusercontent.com/ccodwg/Covid19Canada/master/timeseries_prov/cases_timeseries_prov.csv'
url_active='https://raw.githubusercontent.com/ccodwg/Covid19Canada/master/timeseries_prov/active_timeseries_prov.csv'
url_mortality='https://raw.githubusercontent.com/ccodwg/Covid19Canada/master/timeseries_prov/mortality_timeseries_prov.csv'
url_recovered='https://raw.githubusercontent.com/ccodwg/Covid19Canada/master/timeseries_prov/recovered_timeseries_prov.csv'
url_testing='https://raw.githubusercontent.com/ccodwg/Covid19Canada/master/timeseries_prov/testing_timeseries_prov.csv'

url_vaccine_alberta='https://www.alberta.ca/data/stats/lga-coverage.csv'
url_cases_alberta_lha='https://www.alberta.ca/data/stats/covid-19-alberta-statistics-map-data.csv'
url_cases_alberta='https://www.alberta.ca/data/stats/covid-19-alberta-statistics-data.csv'

url_calgary_weather='https://calgary.weatherstats.ca/download.html/'

url_dict={'active_cases':url_active, 'daily_cases':url_cases, 'death_cases':url_mortality, 'recovered_cases': url_recovered,
          'testing_cases': url_testing, 'vaccine_administered':url_vaccine_administered, 'vaccine_completed': url_vaccine_completed,
          'vaccine_alberta':url_vaccine_alberta, 'cases_alberta_lha': url_cases_alberta_lha, 'calgary_weather': url_calgary_weather}

print('=====> start downloading <=====')
for url_name, url in url_dict.items():
    r = requests.get(url, allow_redirects=True)
    open(url_name, 'wb').write(r.content)
    print('{} is downloaded'.format(url_name))
