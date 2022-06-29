"""Markdown Calendar Generator"""
import calendar
from datetime import datetime
import sys
import os


def create_calendar(year, month, with_isoweek=False, start_from_Sun=False, lang="en", write_md_days=False):
    firstweekday = 6 if start_from_Sun else 0

    cal = calendar.Calendar(firstweekday=firstweekday)

    mdstr = ""
    dic = get_dict(lang)

    colnames = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    if start_from_Sun:
        colnames = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    if with_isoweek:
        colnames.insert(0, "Week")
    colnames = [dic[col] for col in colnames]

    mdstr += '|' + '|'.join(colnames) + '|' + '\n'
    mdstr += '|' + '|'.join([':-:' for _ in range(len(colnames))]) + '|' + '\n'

    for days in cal.monthdatescalendar(year, month):
        if with_isoweek:
            isoweek = days[0].isocalendar()[1]
            mdstr += '|' + str(isoweek) + '|' + \
                '|'.join([str(d.day) for d in days]) + '|' + '\n'
        else:
            mdstr += '|' + '|'.join(['[' + str(d.day) + '](./calendar/' + str(d.year) + '/' + str(d.month) + '/' + str(d.day) + '.md)' for d in days]) + '|' + '\n'

            if write_md_days:
                for day in days:
                    path = f'{os.getcwd()}/calendar/{day.year}/{day.month}'
                    if not os.path.exists(path):
                        os.makedirs(path)
                    filename = f'{day.day}.md'
                    with open(os.path.join(path, filename), 'wb') as temp_file:
                            file_str = '---\n\n'
                            file_str += f'title: \'{calendar.month_name[day.month]} {day.day} {day.year}\'\n\n\n'
                            file_str += f'date: \'{day.day} / {day.month} / {day.year}\'\n\n\n'
                            file_str += '---\n'
                            file_str += ''
                            temp_file.write(file_str.encode())

    return mdstr


def print_calendar(year, month, with_isoweek=False, start_from_Sun=False, lang="en"):
    print('{}/{}\n'.format(year, month))
    print(create_calendar(year, month, with_isoweek, start_from_Sun, lang, write_md_days=True))


def get_dict(lang='en'):
    dic = {}
    colnames = ['Week', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    colnames_ja = ['週', '月', '火', '水', '木', '金', '土', '日']
    colnames_it = ['Settimana', 'Lunedì', 'Martedì', 'Mercoledì', 'Giovedì', 'Venerdì', 'Sabato', 'Domenica']

    if lang == 'en':
        for col in colnames:
            dic[col] = col
    elif lang == 'ja':
        for col, colja in zip(colnames, colnames_ja):
            dic[col] = colja
    elif lang == 'it':
        for col, colit in zip(colnames, colnames_it):
            dic[col] = colit
    else:
        for col in colnames:
            dic[col] = col
    return dic


if __name__ == "__main__":
    argv = sys.argv
    if len(argv) == 1:
        today = datetime.now()
        print_calendar(today.year, today.month)
    elif len(argv) == 2:
        year = int(argv[1])
        for month in range(1, 13):
            print_calendar(year, month, with_isoweek=True)
    elif len(argv) == 3:
        year, month = [int(a) for a in argv[1:3]]
        print_calendar(year, month)
    else:
        print('Usage: python mdcal.py [year] [month]')
