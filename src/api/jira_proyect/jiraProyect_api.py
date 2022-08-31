"""API Collections."""
from flask import jsonify,request
from flask_jwt_extended import jwt_required
from flask_restx import Namespace, Resource, reqparse, fields

from .jiraProyect_dao import jiraProyectDao


api = Namespace("jiraproyects", description="Gestion de los proyectos Jiras")

model_jiraproyects_entry = api.model(
    "model_jiraproyects_entry", {
        "org": fields.String(required=True, description="Nombre de la Organziacion"),
        "instance_name": fields.String(required=True, description="Nombre de la instancia/orgainizcion"),
        "key": fields.String(required=True, description="Key Proyecto Jira"),
        "name": fields.String(required=True, description="Nombre Proyecto Jira"),
        "owner": fields.String(required=True, description="Grupo Owner de la instancia/orgainizcion"),
        "template": fields.String(required=True, description="Nombre Proyecto Template de la instancia"),
        "proyect_lead": fields.String(required=True, description="Administrador Proyecto Jira"),
        "description": fields.String(required=False, description="Descripcion Proyecto Jira")
    })

model_jiraproyect_team_entry = api.model(
    "model_jiraproyect_team_entry", {
        "team": fields.String(required=True, description="Nombre del Team a Relacionar"),
        "role": fields.String(required=True, description="Nombre del Role Jira"),
    })



@api.route("/")
class api_jiraproyects(Resource):


    @api.doc("Add new organziation instance tools.")
    @api.doc(body=model_jiraproyects_entry)
    def post(sef):
        """Add a new Employee."""
        org = request.json["org"]
        instance = request.json["instance_name"]
        owner = request.json["owner"]
        name = request.json["name"]
        key = request.json["key"]
        template = request.json["key"]
        proyect_lead = request.json["proyect_lead"]
        description = ""
        if "description" in request.json:
            description = request.json["description"]
        
        jiraProyectDao.addOrgInstanceJiraProyects(org,instance,name, key, owner, template, proyect_lead, description)
        return "Creado Proyecto Jira Con Existo", 200


@api.route("/org/<string:orgnizationName>/tools/<string:toolName>")
class api_orgtools_org_tool(Resource):
    @api.doc("Get instancias de una herramienta")
    def get(sef,orgnizationName, toolName):
        """Recupera las instancias de una herramienta en una organizacion."""
        result = jiraProyectDao.getOrgJiraProyects(org, toolName)
        return jsonify(result)

    
@api.route("/org/<string:orgnizationName>/instance/<string:instanceName>/proyects")
class api_jiraproyect_org_tool_instance_proyects(Resource):
    """Gestiona los proyectos de una instancia de jira de una organizacion"""
    
    @api.doc("Devuelve los proyectos de una instancia Jira para una organización")
    def get(self,orgnizationName, instanceName):
        """Recupera las instancias de una herramienta de una organizacion."""
        result = jiraProyectDao.getOrgJiraInstanceProyects(orgnizationName, instanceName)
        return jsonify(result)


    
@api.route("/org/<string:orgnizationName>/instance/<string:instanceName>/proyects/proyect/<string:keyProyect>")
class api_jiraproyect_org_tool_instance_proyects_proyect(Resource):
    """Gestiona los datos de un proyecto Jira de una instancia de jira de una organizacion."""
    
    @api.doc("Devuelve informacion de un proyecto Jira de una organizacion en una instancia.")
    def get(self,orgnizationName, instanceName,keyProyect):
        """Devuelve informacion de un proyecto Jira de una organizacion en una instancia."""
        result = jiraProyectDao.getOrgInstanceJiraProyect(orgnizationName, instanceName,keyProyect)
        return jsonify(result)
    
    @api.doc("Borra un proyecto Jira de una organizacion en una instancia.")
    def delete(self,orgnizationName, instanceName,keyProyect):
        """Borra un proyecto Jira de una organizacion en una instancia."""
        result = jiraProyectDao.deleteOrgIntanceJiraProyects(orgnizationName, instanceName,keyProyect)
        return ""
    
@api.route("/org/<string:orgnizationName>/instance/<string:instanceName>/proyects/proyect/<string:keyProyect>/teams")
class api_jiraproyect_org_tool_instance_proyects_proyect_teams(Resource):
    """Gestiona los teams de un proyecto Jira."""
    
    @api.doc("Devuelve los Teams de un Proyecto Jira")
    def get(self,orgnizationName, instanceName,keyProyect):
        """Devuelve los Teams asociados a un Proyecto Jira."""
        result = jiraProyectDao.getOrgJiraInstanceProyectTeams(orgnizationName, instanceName,keyProyect)
        return jsonify(result)
        
    @api.doc("Relacionar un Team con un Proyecto Jira.")
    @api.doc(body=model_jiraproyect_team_entry)
    def post(self,orgnizationName, instanceName,keyProyect):
        """Relacionar un Team con un Proyecto Jira."""
        role = request.json["role"]
        teamName  = request.json["team"]
        result = jiraProyectDao.addTeamToOrgJiraInstanceProyect(orgnizationName, instanceName,keyProyect,teamName,role)
        return jsonify(result)
