import click
import os
from subprocess import call
import json

@click.group(chain=True)
def cli():
    pass

#login menu for HR or Candidate according to username
#hr ---> HR, cn---> Candidate
@cli.command('log',help="login")
@click.option('--username',prompt='username',help='username')
@click.option('--password',prompt='password',help="password")
def login(username,password):
    if(username[0:2]=='hr'and password=="123"):
        call(["python", "cli_hr.py"])
    elif(username[0:2]=='cn'):
        call(["python", "cli_cn.py"])
    else:
        print ('no such user maybe you want to reg?')

if __name__=='__main__':
   login()