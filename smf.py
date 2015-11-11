# -*- coding: utf-8 -*-
from Utils import utils
from Models.Geek import Geek
import argparse

# Main program
if __name__ == '__main__':
    # create arguments
    parser = argparse.ArgumentParser(description='Steam Master Fapper')
    parser.add_argument('--text', action="store_true", help='Show the report in the shell')
    parser.add_argument('--mail', action="store_true", help='Send the report by mail')
    # parse arguments from script parameters
    args = parser.parse_args()

    # get settings
    cfg = utils.get_settings()
    list_friend = cfg['list_friend']

    # create geek object from id
    print "Getting geek info, it may take a while..."
    geeks = []
    for friend in list_friend:
        # tab for the player. will be insert into final_tab_mail
        geek = Geek(friend['steam_id'])
        geek.mail = friend['mail']
        geeks.append(geek)

    # Create messages
    message_text = utils.print_in_shell(geeks)
    message_html = utils.get_html_template(geeks)

    if args.mail:
        # Send mails
        for geek in geeks:
            utils.send_mail(message_text, message_html, geek.mail)
        for mail in cfg['list_mail_to_send_report']:
            utils.send_mail(message_text, message_html, mail)

    if args.text:
        # Print the table in the current shell
        print message_text
