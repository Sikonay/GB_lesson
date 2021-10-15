from reguests import get, utils


def currency_rates(cur):
    api_url = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encod = utils.get_encoding_headers(api_url.headers)
    cur_date = api_url.headers['Set-Cookie'].split(',')[1]
    print(f'Дата {cur_date}')

    content = api_url.content.decode(encoding=encod)

    words = ['Nominal', 'Name', 'Value']

