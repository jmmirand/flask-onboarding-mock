"""Modulo gestión conf herramientas de las organizaciones."""
from flask import jsonify
from pyparsing import DebugExceptionAction
from pony.orm import commit
from loguru import logger
from datetime import datetime
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
    def getOrgTools(org):
        """Devuelve todas las instancias de herramientas de una organizacion."""
        results = []
        orgs = OrgTool.select(org=org)
        for org in orgs:
            org_json = org.to_dict()
            results.append(org_json)
        return results

    @staticmethod
    def getOrgToolInstances(org,tool):
        """Devuelve todas las instancias de herramientas de una organizacion."""
        results = []
        orgs = OrgTool.select(org=org, tool=tool)
        for org in orgs:
            org_json = org.to_dict()
            results.append(org_json)
        return results


    @staticmethod
    def getInstanceTool(org, tool, instance):
        """Devuelve la informacion de una instancia de una herramienta."""
        jiraInstance = OrgTool.get(org=org, tool=tool, instance_name=instance)
        jiraInstanceJSON = jiraInstance.to_dict()
        return jiraInstanceJSON

    @staticmethod
    def deleteInstanceTool(org, tool, instance):
        """Devuelve la informacion de una instancia de una herramienta."""
        orgs = OrgTool.select( org=org, tool=tool, instance_name=instance)
        for org in orgs:
            org.delete()
        return True



    @staticmethod
    def addInstanceTool( org, tool, name, owner, licences=""):
        """Crea un nueva Entrada de Configuracion de Instancia."""
        
        orgtools = OrgTool.select(org=org, tool=tool, instance_name=name)
        for orgtool in orgtools:
            logger.warning(f"Config para org:{org} tool:{tool} instancia:{name}, not added")
            return False
        
        orgTool = OrgTool()
        orgTool.org = org
        orgTool.tool = tool
        orgTool.instance_name = name
        orgTool.owner = owner
        orgTool.licences = licences
        
        commit()
        return True 
 
 