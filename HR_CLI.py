import click
import json

@click.group(chain=True)
def cli():
    pass

@cli.command('log', help="login to the system")
@click.option('--username', help="the username")
@click.option('--password', help="the password")
def login(username, password):
    file_open = json.load(open("hr_json.json"))
    user1=file_open[0]["username"]
    pass1=file_open[0]["password"]
    if user1==username and pass1==password:
        click.echo("welcome")
    else:
        click.echo("your username or password are inccorect")





@cli.command('status_change', help="change the status of the CV")
@click.option('--id', help="the id of which you want to change")
@click.option('--status', help="accepted/regected/underreview/postpone")
def change_status(id, status):
    file_open = json.load(open("DATA.json"))
    for i in file_open:
        if i["ID"]==id:
            i["status"]=status
    return




@cli.command('edit_note', help="edit notes to a CV")
@click.option('--id', help="the id of which you want to change")
@click.option('note',help="enter your note")
def edit_notes(id,note):
    file_open = json.load(open("DATA.json"))
    for i in file_open:
        if i["ID"] == id:
            i["notes"]=note
    return




if __name__=='__main__':
    cli()