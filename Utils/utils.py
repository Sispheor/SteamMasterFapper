import json
import requests
from tabulate import tabulate
from datetime import timedelta, datetime
import time
import os


def get_dict_from_geeks_dict(geeks):
    final_table = []
    for geek in geeks:
        table_one_geek = [geek.id, geek.name, geek.played_time_2weeks]
        final_table.append(table_one_geek)
    # sort by bigger time played
    final_table = sorted(final_table, key=lambda row: row[2], reverse=True)
    return final_table


def get_settings():
    import yaml
    with open("settings.yml", 'r') as ymlfile:
        cfg = yaml.load(ymlfile)
    return cfg


def get_steam_url(url):
    cfg = get_settings()
    req = requests.get(url,
                       proxies={"http": cfg['PROXY']})
    return json.loads(req.text)


def print_in_shell(geeks):
    """
    Print in the current shell a table of geek info
    :param geeks: Dict of Geek
    :return: print a Human readable table with info about geek
    """
    # tabulate need a simple table, not an object
    final_table = get_dict_from_geeks_dict(geeks)

    headers = ["id", "Name", "Time played"]
    print tabulate(final_table, headers=headers, numalign="right")


def get_html_template(geeks):
    from django.template import Template, Context
    from django.template.loader import get_template
    from django.conf import settings
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    print BASE_DIR
    settings.configure(
        TEMPLATE_DIRS=(os.path.join(BASE_DIR, 'Template'),),
        TEMPLATE_LOADERS=('django.template.loaders.filesystem.Loader',),
    )
    import django
    django.setup()
    final_table = get_dict_from_geeks_dict(geeks)
    # current date
    cur_week = time.strftime('%d-%m-%Y')
    # date last week
    last_week = datetime.strptime(cur_week, '%d-%m-%Y') - timedelta(days=14)
    last_week = last_week.strftime('%d-%m-%Y')

    # get mail template
    mail_template = get_template('mail.html')
    d = Context({'final_tab_mail': final_table,
                 'cur_week': cur_week,
                 'last_week': last_week})
    return mail_template.render(d)
