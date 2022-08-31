"""API Collections."""
from flask import jsonify,request
from flask_jwt_extended import jwt_required
from flask_restx import Namespace, Resource, reqparse, fields

from .orgTools_dao import orgToolsDao


api = Namespace("orgtools", description="Configuracion Instancias SaaS para las Organizaciones")

model_orgtools_entry = api.model(
    "model_orgtools_entry", {
        "org": fields.String(required=True, description="Nombre de la Organziacion"),
        "tool": fields.String(required=True, description="Identificador de la herramienta Saas ( jira, confluence, github)"),
        "instance_name": fields.String(required=True, description="Nombre de la instancia/orgainizcion"),
        "owner": fields.String(required=True, description="Grupo Owner de la instancia/orgainizcion"),
        "licenses": fields.String(required=False, description="Grupo de usuarios para licencias (solo jira y Confluence)"),
        
    })

@api.route("/")
class api_orgtools(Resource):
    
    @api.doc("Get Todas Las instancias de todas las orgs, No Requiere token")
    def get(sef):
        """Recupera las colleciones Buscandolas."""
        result = orgToolsDao.getAllTools()
        return jsonify(result)

    @api.doc("Add new organziation instance tools.")
    @api.doc(body=model_orgtools_entry)
    def post(sef):
        """Add a new Employee."""
        org = request.json["org"]
        instance = request.json["instance"]
        owner = request.json["owner"]
        tool = request.json["tool"]
        licences = ""
        if "licenses" in request.json:
            licences = request.json["licences"]
        orgToolsDao.addInstanceTool(org,tool,instance,owner,licences)
        return "Insertada la Instancia de la Herramienta Con Exito", 200


@api.route("/org/<string:orgnizationName>/tools/<string:toolName>")
class api_orgtools_org_tool(Resource):
    @api.doc("Get instancias de una herramienta")
    def get(sef,orgnizationName, toolName):
        """Recupera las instancias de una herramienta en una organizacion."""
        result = orgToolsDao.getOrgToolInstances(orgnizationName,toolName)
        return jsonify(result)

    
@api.route("/org/<string:orgnizationName>/tools/<string:toolName>/instance/<string:instanceName>")
class api_orgtools_org_tool_instance(Resource):
    @api.doc("Devuelve info de una instancia de una herramienta de una Organizacion")
    def get(self,orgnizationName, toolName, instanceName):
        """Recupera las instancias de una herramienta de una organizacion."""
        result = orgToolsDao.getInstanceTool(orgnizationName, toolName, instanceName)
        return result

    def delete(self,orgnizationName, toolName, instanceName):
        """Borra instancias de una herramienta de una organizacion."""
        result = orgToolsDao.deleteInstanceTool(orgnizationName, toolName, instanceName)
        return jsonify(result)