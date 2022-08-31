"""API Organization Team."""
from textwrap import shorten
from flask import jsonify,request
from flask_jwt_extended import jwt_required
from flask_restx import Namespace, Resource, reqparse, fields

from utils.db_model import Team

from .teams_dao import orgTeamsDao


api = Namespace("orgteams", description="Gestiona los teams de una organziacion")

model_orgteams_entry = api.model(
    "model_orgteams_entry", {
        "name": fields.String(required=True, description="Nombre del Team Role con sufijo (DV,TL,PO,AO)"),
        "shortname": fields.String(required=True, description=" Nombre sin Prefijo ni sufijo"),
        "description": fields.String(required=True, description="Descripcion del Team"),
        "owner": fields.String(required=True, description="Grupo Owner de la instancia/orgainizcion"),
    })

@api.route("/org/<string:org>")
class api_orgteams_org(Resource):
    
    @api.doc("Get los Teams de una organizacion.")
    def get(sef,org):
        """Get los Teams de una organizacion."""
        result = orgTeamsDao.getOrgTeams(org)
        return jsonify(result)

    @api.doc("Add new organziation instance tools.")
    @api.doc(body=model_orgteams_entry)
    def post(sef, org):
        """Add a new Employee."""
        name = request.json["name"]
        shortname = request.json["shortname"]
        description = request.json["description"]
        owner = request.json["owner"]
        
        orgTeamsDao.addOrgTeam(org,name,shortname,description,owner)
        return "Insertada la Instancia de la Herramienta Con Exito", 200


@api.route("/org/<string:org>/team/<string:teamName>")
class api_orgteams_org_team(Resource):
    
    @api.doc("Get los Teams de una organizacion.")
    def delete(sef,org,teamName):
        orgTeamsDao.deleteOrgTeam(org, teamName)
        return "Team eliminado correctamente"