"""Modulo gestión de los proyectos Jira de luna Organizacion."""

from datetime import datetime

from loguru import logger
from pony.orm import commit

from utils.db_model import JiraProjectTeam, JiraProyect, Team


class jiraProyectDao:
    """Clase que gestiona los proyectos Jira."""

    @staticmethod
    def getOrgJiraInstanceProyects(org, instance):
        """Devuelve todas proyectos Jira de Una Instancia de una Organziacion."""
        results = []
        rows = JiraProyect.select(org=org, instance_name=instance)
        for row in rows:
            row_json = row.to_dict()
            row_json["owner"] = row.owner.name
            results.append(row_json)
        return results

    def getOrgInstanceJiraProyect(org, instance, key):
        """Devuelve info un proyecto Jira de Una Instancia de una Organziacion."""
        jproyect = JiraProyect.get(org=org, instance_name=instance, key=key)
        row_json = jproyect.to_dict()
        row_json["owner"] = jproyect.owner.owner
        return row_json

    @staticmethod
    def addOrgInstanceJiraProyects(org, instance_name, name, key, owner, template, proyect_lead, description):
        """Crea un nuevo Proyecto Jira en una instancia de una organizacion."""
        pryts = JiraProyect.select(key=key)
        for proy in pryts:
            logger.warning(f"Proyecto Jira Key:{key} existe, not created")
            return False

        team_owner = Team.get(name=owner)
        if team_owner == None:
            logger.warning(f"El team owner NO EXISTE , darlo de alta previamente")
            team_owner = Team(name=owner, org=org, owner=owner, shortname=owner, description="Auto Guardado")
            commit()

        obj = JiraProyect(owner=team_owner)
        obj.org = org
        obj.instance_name = instance_name
        obj.name = name
        obj.key = key
        obj.description = description
        obj.proyect_lead = proyect_lead
        obj.template = template
        commit()
        return True

    @staticmethod
    def deleteOrgIntanceJiraProyects(org, instance, key):
        """Borra el proyecto Jira de una instancia de una organizacion."""
        rows = JiraProyect.select(org=org, instance_name=instance, key=key)
        for row in rows:
            row.delete()
        return True

    @staticmethod
    def getOrgJiraInstanceProyectTeams(org, instance, key):
        """Recupera la lista de grupos/roles asociados a un Proyecto Jira."""
        proy = JiraProyect.get(org=org, instance_name=instance, key=key)
        result = []
        if proy != None:
            for team in proy.jira_project_teams:
                team_json = team.to_dict()
                team_json["team"] = team.team.name
                team_json["org"] = proy.org
                team_json["instance_name"] = proy.instance_name
                team_json["jira_project_name"] = proy.name
                team_json["jira_project_key"] = proy.key
                result.append(team_json)
        return result

    @staticmethod
    def addTeamToOrgJiraInstanceProyect(org, instance, key, team, role):
        """Recupera la lista de grupos/roles asociados a un Proyecto Jira."""

        # Recupero el Team que estamos buscando, si no devuelvo error.
        teamObj = Team.get(name=team)
        if team == None:
            return "Team No existe"

        # Recupero el proyecto, si no devuelvo error.
        proy = JiraProyect.get(org=org, instance_name=instance, key=key)
        if proy == None:
            return "Proyecto No existe"
        else:
            teamRoleExist = False
            for teamRole in proy.jira_project_teams:
                if teamRole.team.name == team and teamRole.role == role:
                    teamRoleExist = True

            if not teamRoleExist:
                # Creo la relación y se la añado al proyecto.
                jiraTeam = JiraProjectTeam(team=teamObj, jira_project=proy)
                jiraTeam.role = role
                jiraTeam.team = teamObj
                commit()
                return "Team-Role asignado al proyecto correctamente"
            else:
                return "Team-role link exist."

        return "ok"
