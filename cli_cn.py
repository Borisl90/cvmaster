import cn_function
import click

@click.group(chain=True)
def cli():
    pass

##############################################
## all the function are from cn_function    ##
##############################################

#login for cv:
@cli.command('login', help='Login function for CV(cn)')
@click.option('--username', help='the user cn username')
@click.option('--password', help='the user cn password')
def cli_login(username,password):
    cn_function.login(username, password)

#registration for cv:
@cli.command('reg', help='Registration function for a new cn(candidate)')
@click.argument('filename', help='the CV info from a .JSON file')
def cli_register(filename):
    cn_function.register(filename)

#delete a candidate from the database
@cli.command('del', help='delete a candidate from the DATA file')
@click.option('--id', help='the id of the candidate we want to delete')
def cli_deletecv(id):
    cn_function.delete_cv(id)

@cli.command('change email', help='change the email of the candidate')
@click.option('--id', help='the id of the candidate we want to change email')
@click.option('--new_mail', help='the new email')
def cli_changemail(id, new_mail):
    cn_function.change_mail(id, new_mail)

@cli.command('change mobile', help='change the mobile of the candidate')
@click.option('--id', help='the id of the candidate we want to change mobile')
@click.option('--new_mail', help='the new mobile')
def cli_changemail(id, new_mobile):
    cn_function.change_mobile(id, new_mobile)

if __name__=='__main__':
    cli()