import click
import hr


@click.group(chain=True)
def cli():
    pass


@cli.command('printall', help="print data")
def cli_printall():
    hr.printall()


@cli.command('sr', help="print")
@click.option('--id', prompt='chose id', help="id")
def cli_printid(id):
    hr.printid(id)


@cli.command('edit status', help="edit status")
@click.option('--id', prompt='chose id', help="id")
@click.option('--select', prompt='chose the new status of this candidate', type=click.Choice(['0', '1', '2', '3']),
              help="edit status")
def cli_editstatus(id, select):
    hr.editstatus()


@cli.command('edit status', help="edit status")
@click.option('--id', prompt='chose id', help="id")
@click.option('--select', prompt='candidate notes', help="edit notes")
def cli_editnotes(id, select):
    hr.editnotes(id, select)


@cli.command('searchpro', help="search professional")
@click.option('--pro', prompt='professional', help="search professional")
def cli_searchpro(pro):
    hr.searchpro(pro)





""""@cli.command('idmenu', help="id menu")
@click.option('--person')
@click.option('--select',prompt='chose what to do with this person',type=click.Choice(['edit status', 'edit notes']),help="id menu")
def idmenu(person,select):
    if select=="edit status":
        editstatus(person)
    elif select=="edit notes":
        search()"""
