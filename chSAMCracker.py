#!/usr/bin/env python3
#  ____  _____  _    _  ____  ____  ____  ____     ____  _  _     ___  _   _  __  __  ___   ___  _  _ 
# (  _ \(  _  )( \/\/ )( ___)(  _ \( ___)(  _ \   (  _ \( \/ )   / __)( )_( )/. |/  )(__ \ / _ \( \( )
#  )___/ )(_)(  )    (  )__)  )   / )__)  )(_) )   ) _ < \  /   ( (__  ) _ ((_  _))(  / _/( (_) ))  ( 
# (__)  (_____)(__/\__)(____)(_)\_)(____)(____/   (____/ (__)    \___)(_) (_) (_)(__)(____)\___/(_)\_)
#
###############################################################################

#########################################
    #### Charon SAM Database Password Cracker ######
        #### Powered By Ch4120N ####
#########################################

import sys
import os
import subprocess
import argparse
from colorama import Fore, init
from framework.win32.hashdump import dump_file_hashes
from passlib.hash import nthash
from Core.customhelpformatter import CusHelpFormatter
from Core.banner import Banner
from Core.log import logging as log
init(autoreset=True)

class chSAMCracker:
  def __init__(self):
      self.excludeUser = ["Administrator", "Guest", "DefaultUser", "DefaultAccount",
     "WDAGUtilityAccount", "SYSTEM", "LocalService", "NetworkService"]

      parser = argparse.ArgumentParser(add_help=False, usage=self.usage(), exit_on_error=False, formatter_class=CusHelpFormatter)
      parser.add_argument("SYSTEM", type=str)
      parser.add_argument("SAM", type=str)

      parser.error = lambda message: print(self.usage()) or sys.exit(2)

      argv = parser.parse_args()

      self.systemFile = argv.SYSTEM
      self.samFile = argv.SAM

      if not os.path.exists(self.systemFile):
          log.error("The file SYSTEM does not exist")

      # print(f"{Fore.LIGHTBLUE_EX}[{Fore.LIGHTGREEN_EX}+{Fore.LIGHTBLUE_EX}]{Fore.LIGHTGREEN_EX} Get the usernames from SAM database ...")

  
  def usage(self):
      return fr"""{Banner()}{Fore.LIGHTGREEN_EX}
Usage: python chSAMCracker.py <SYSTEM file> <SAM file> [OPTIONS]

Description:
  This script allows you to extract the victim's username and password hash from the SAM database in Windows.
  You can select the victim's username based on the ID, and then choose the cracking method.
  After completing these steps, the script will quickly start cracking the victim's password hash. 
  Note that you must use a Linux system or boot Windows in Safe Mode to access the SAM database file;
  Otherwise, the script won't be able to access the SAM database.


Options:
  -h, --help                  Show this help message and exit
  -l, --list                  List all users
  -n, --no-default-users      Does't show default users like Administrator, DefaultUser, etc ...
  -o, --output OUTPUT_FILE    Save results to a specified output file

Examples:
  python chSAMCracker.py SYSTEM SAM -l
  python chSAMCracker.py SYSTEM SAM -n
  python chSAMCracker.py SYSTEM SAM -l -o results.txt
  python chSAMCracker.py C:\Users\<username>\Desktop\SYSTEM C:\Users\<username>\Desktop\SAM

Visit for more information: https://github.com/Ch4120N/Charon-SAM-Database-Cracker
    """

chSAMCracker()