# -*- coding: utf-8 -*-

import click

@click.command()
def main(args=None):
    """Console script for python_boilerplate"""
    click.echo("Replace this message by putting your code into "
                "thws.cli.main")
    click.echo("See click documentation at http://click.pocoo.org/")


if __name__ == "__main__":
    main()