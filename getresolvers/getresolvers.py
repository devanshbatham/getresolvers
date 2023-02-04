# -*- coding: utf-8 -*-


import logging
import requests


#              ,----------------,              ,---------,
#         ,-----------------------,          ,"        ,"|
#       ,"                      ,"|        ,"        ,"  |
#      +-----------------------+  |      ,"        ,"    |
#      |  .-----------------.  |  |     +---------+      |
#      |  |                 |  |  |     | -==----'|      |
#      |  |  Sybil Scan!    |  |  |     |         |      |
#      |  |                 |  |  |/----|`---=    |      |
#      |  |  C:\>_          |  |  |   ,/|==== ooo |      ;
#      |  |                 |  |  |  // |(((( [33]|    ,"
#      |  `-----------------'  |," .;'| |((((     |  ,"
#      +-----------------------+  ;;  | |         |,"    
#         /_)______________(_/  //'   | +---------+
#    ___________________________/___  `,
#   /  oooooooooooooooo  .o.  oooo /,   \,"-----------
#  / ==ooooooooooooooo==.o.  ooo= //   ,`\--{)B     ,"
# /_==__==========__==_ooo__ooo=_/'   /___________,"
# `-----------------------------'



def main():
    logging.basicConfig(format='%(message)s', level=logging.INFO)
    logging.info("""\u001b[33;1m
            __                   __               
  ___ ____ / /________ ___ ___  / /  _____ _______
 / _ `/ -_) __/ __/ -_|_-</ _ \/ / |/ / -_) __(_-<
 \_, /\__/\__/_/  \__/___/\___/_/|___/\__/_/ /___/
/___/                                             
                                               
                \u001b[36;1m - by Sybil Scan Research <research@sybilscan.com>\u001b[0m 
    """)
    logging.info("🔍 Fetching resolvers\n")
    resolvers_source = "https://raw.githubusercontent.com/Sybil-Scan/getresolvers/main/resolvers.txt"
    try:
        response = requests.get(resolvers_source)
    except: 
        logging.error("❌ Error occured while fetching resolvers [use VPN if raw.githubusercontent.com is blocked via ISP]")
    with open('resolvers.txt', 'w') as f:
        f.write(response.text)

    resolvers_list = open('resolvers.txt').read().splitlines()
    for resolver in resolvers_list:
        print(resolver)


    logging.info(f"\n✅ Resolvers found : {len(resolvers_list)}")
    logging.info(f"✅ Output saved in resolvers.txt")