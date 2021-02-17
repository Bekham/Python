# Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
# до минуты: <s> сек;
# до часа: <m> мин <s> сек;
# до суток: <h> час <m> мин <s> сек;
# *до месяца, до года, больше года: по аналогии.
months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # массив количества дней в каждом месяце в течение года

time_sec = int(input('Please, input time period in seconds: '))
time_min = time_sec // 60
time_hour = time_sec // (60 * 60)
time_day = time_sec // (24 * 60 * 60)
time_year = time_sec // (365 * 24 * 60 * 60)
time_month_in_days = time_year * 365
time_month = time_year * 12

stop = 0
while stop == 0:  # цикл вычисления количества целых месяцев и дней, входящих в эти месяцы в течении указанного периода
    for m_d in months:
        time_month_in_days += m_d
        time_month += 1
        if time_month_in_days > time_day:
            time_month_in_days -= m_d
            time_month -= 1
            stop = 1

if time_year > 0:  # формирование итоговой строки заданного периода с делением на год-месяц-день-час-минута-секунда
    time_text = str(time_year) + ' year(s) '
else:
    time_text = ''
if time_month > 0:
    time_text += str(time_month - time_year * 12) + ' month(s) '
if time_day > 0:
    time_text += str(time_day - time_month_in_days) + ' day(s) '
if time_hour > 0:
    time_text += str(time_hour - time_day * 24) + ' hour(s) '
if time_min > 0:
    time_text += str(time_min - time_hour * 60) + ' minute(s) '
    time_text += str(time_sec - time_min * 60) + ' second(s) '
else:
    time_text = str(time_sec) + ' second(s) '
print('duration =', time_sec)
print(time_text)
