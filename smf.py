# -*- coding: utf-8 -*-
from Utils import utils
from Models.Geek import Geek

# TODO: make mail template, command options --mail --text

# Main program
cfg = utils.get_settings()

list_friend_id = cfg['list_friend_id']

# create geek object from id
print "Getting geek info, it may take a while..."
geeks = []
for friend_id in list_friend_id:
    # tab for the player. will be insert into final_tab_mail
    geek = Geek(friend_id)
    geeks.append(geek)

utils.print_in_shell(geeks)

print utils.get_html_template(geeks)
