"""Modulo que getiona Teams de los equpos."""
from secrets import randbelow
from sqlite3 import dbapi2
from pyparsing import DebugExceptionAction
from pony.orm import commit,db_session
from loguru import logger
from datetime import datetime
from utils.db_model import Team


class orgTeamsDao:
    """Clase que gestiona Teams."""


    @staticmethod
    def getOrgTeams(org):
        """Devuelve todas los equipos de una organizacion."""
        results = []
        rows = Team.select()
        for row in rows:
            rowJson = row.to_dict()
            results.append(rowJson)
        return results


    @staticmethod
    def deleteOrgTeam(org, teamName):
        """Devuelve la informacion de una instancia de una herramienta."""
        rows = Team.select( org=org, name=teamName)
        for row in rows:
            row.delete()
        return True


    @staticmethod
    def addOrgTeam( org, name, shortname, description, owner):
        
        teams = Team.select(name=name)
        for team in teams:
            logger.warning(f"Team {name} ya existe, no se añade")
            return False
        
        """Crea un nuevo Empleado."""
        orgTeam = Team()
        orgTeam.org = org
        orgTeam.name = name
        orgTeam.shortname = shortname
        orgTeam.owner = owner
        orgTeam.description = description
        commit()
        return True 
 
 