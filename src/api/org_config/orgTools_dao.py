"""Modulo gestión conf herramientas de las organizaciones."""
from datetime import datetime

from flask import jsonify
from loguru import logger
from pony.orm import commit

from utils.db_model import OrgTool


class orgToolsDao:
    """Clase que gestiona configuracion herramientas."""

    @staticmethod
    def getAllTools():
        """Devuelve todas las instancias de herramientas de una organizacion."""
        results = []
        orgs = OrgTool.select()
        for org in orgs:
            org_json = org.to_dict()
            results.append(org_json)
        return results

    @staticmethod
    def getOrgTools(org_id):
        """Devuelve todas las instancias de herramientas de una organizacion."""
        results = []
        orgTools = OrgTool.get(org_id=org_id)
        for tool in orgTools:
            orgtool_json = tool.to_dict()
            results.append(orgtool_json)
        return results

    @staticmethod
    def getOrgToolInstances(org_id, tool):
        """Devuelve todas las instancias de herramientas de una organizacion."""
        results = []
        orgTools = OrgTool.select(org_id=org_id, tool=tool)
        for tool in orgTools:
            orgtool_json = tool.to_dict()
            results.append(orgtool_json)
        return results

    @staticmethod
    def getInstanceTool(orgId, tool, instance):
        """Devuelve la informacion de una instancia de una herramienta."""
        jiraInstance = OrgTool.get(org_id=orgId, tool=tool, instance_name=instance)
        jiraInstanceJSON = jiraInstance.to_dict()
        return jiraInstanceJSON

    @staticmethod
    def deleteInstanceTool(org_id, tool, instance):
        """Devuelve la informacion de una instancia de una herramienta."""
        orgs = OrgTool.select(org_id=org_id, tool=tool, instance_name=instance)
        for tool in orgs:
            tool.delete()
        return True

    @staticmethod
    def addInstanceTool(org_id, orgName, orgAcronym, tool, name, owner, licences=""):

        """Crea un nueva Entrada de Configuracion de Instancia."""

        orgtools = OrgTool.select(org_id=org_id, tool=tool, instance_name=name)
        for tool in orgtools:
            logger.warning(f"Config para org:{orgAcronym} tool:{tool} instancia:{name}, not added, Already exist.")
            return False

        orgTool = OrgTool()
        orgTool.org_id = org_id
        orgTool.org_name = orgName
        orgTool.org_acronym = orgAcronym
        orgTool.tool = tool
        orgTool.instance_name = name
        orgTool.owner = owner
        orgTool.licences = licences
        orgTool.org_id = org_id

        commit()
        return True
