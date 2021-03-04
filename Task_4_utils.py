from requests import get, utils
import datetime


def currency_rates(args):
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    course = content.split('<Valute')
    course_dict = {}
    answer = {}
    date = course[0][
           course[0].find('Date="') + len('Date="'):course[0].find('Date="') + len('Date="') + len('xx.xx.xxxx')]
    date_list = date.split('.')
    for money in course:
        currency_ind = (money.find('<CharCode>'))
        if currency_ind != -1:
            rub_course = money[money.find('<Value>') + len('<Value>'):money.find('</Value>')]
            rub = float(rub_course[0:rub_course.find(',')] + '.' + rub_course[rub_course.find(',') + 1:])
            course_dict[money[currency_ind + len('<CharCode>'):money.find('</CharCode>')]] = rub
    answer['Date'] = str(datetime.date(int(date_list[-1]), int(date_list[-2]), int(date_list[-3])))
    for currency in args:
        if currency.upper() in course_dict:
            answer[currency.upper()] = course_dict[currency.upper()]
        else:
            answer[currency.upper()] = 'None'
    return answer


if __name__ == '__main__':
    val = input('Введите аббревиатуры валют: ')
    print(currency_rates(val.split()))
