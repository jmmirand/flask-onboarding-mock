#!/usr/bin/env python3
"""Add or modify a Employee in who is who database."""

import click
from loguru import logger
from pony.orm import db_session




@db_session
@click.command()
@click.option("--name", "-n", help="Name")
@click.option("--mail", "-m", help="Mail", required=True, prompt=True)
@click.option("--phone", "-p", help="Phone")
@click.option("--team", "-t", help="Team User")
@click.option("--comment", "-c", help="Interesting Comment")
def main(name, mail, phone, team, comment):
    """Who Is Who Add/Modify People."""

    logger.info(f"wiw-add {mail},{team},{phone},{team},{comment}")
#    wiw = whoiswho()
#    wiw.addEmployee(mail, name, phone, team)
#    if comment != "":
#        wiw.addBullet(mail=mail, bullet=comment)


if __name__ == "__main__":
    main()
