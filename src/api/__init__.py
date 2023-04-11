"""Flask API da servicio de Acceso a Empleados."""
from flask_restx import Api
from pony.orm import db_session

from .jira_proyect.jiraProyect_api import api as jiraProyect_api
from .jira_proyect.jiraProyect_dao import jiraProyectDao
from .login.login import api as login_api
from .org_config.orgTools_api import api as orgConfig_api
from .org_config.orgTools_dao import orgToolsDao
from .team.teams_api import api as orgTeams_api
from .team.teams_dao import orgTeamsDao

api = Api(title="API Example", version="1.0", description="A simple demo API")
api.add_namespace(login_api)
api.add_namespace(orgConfig_api)
api.add_namespace(jiraProyect_api)
api.add_namespace(orgTeams_api)


with db_session:

    # Add Base Teams Rol to play
    orgTeamsDao.addOrgTeam(
        "74e73bde-026a-4f57-a62f-c5fd28b34858",
        "GR_ALMNXGN_ALM-AO",
        "ALMCORE",
        "Asset Owners de la Tribu ALM",
        "GR_ALMNXGN_ALM-AO",
    )
    orgTeamsDao.addOrgTeam(
        "74e73bde-026a-4f57-a62f-c5fd28b34858",
        "GR_ALMNXGN_ALMCORE-TL",
        "ALMCORE",
        "Technical Leads de ALMCORE",
        "GR_ALMNXGN_ALM-AO",
    )
    orgTeamsDao.addOrgTeam(
        "74e73bde-026a-4f57-a62f-c5fd28b34858",
        "GR_ALMNXGN_ALMCORE-PO",
        "ALMCORE",
        "Product Owners de ALMCORE",
        "GR_ALMNXGN_ALM-AO",
    )
    orgTeamsDao.addOrgTeam(
        "74e73bde-026a-4f57-a62f-c5fd28b34858",
        "GR_ALMNXGN_ALMCORE-DEV",
        "ALMCORE",
        "Product Owners de ALMCORE",
        "GR_ALMNXGN_ALM-AO",
    )
    orgTeamsDao.addOrgTeam(
        "74e73bde-026a-4f57-a62f-c5fd28b34858",
        "GR_ALMNXGN_ALMPLATFORM-TL",
        "ALMPLATFORM",
        "Technical Leads de ALMPLATFORM",
        "GR_ALMNXGN_ALM-AO",
    )
    orgTeamsDao.addOrgTeam(
        "74e73bde-026a-4f57-a62f-c5fd28b34858",
        "GR_ALMNXGN_ALMPLATFORM-PO",
        "ALMPLATFORM",
        "Product Owners de ALMPLATFORM",
        "GR_ALMNXGN_ALM-AO",
    )
    orgTeamsDao.addOrgTeam(
        "74e73bde-026a-4f57-a62f-c5fd28b34858",
        "GR_ALMNXGN_ALMPLATFORM-DEV",
        "ALMPLATFORM",
        "Product Owners de ALMPLATFORM",
        "GR_ALMNXGN_ALM-AO",
    )
    orgTeamsDao.addOrgTeam(
        "74e73bde-026a-4f57-a62f-c5fd28b34858",
        "GR_ALMNXGN_OHEONPREM-AO",
        "OHEONPREM",
        "Asset Owner de OHEONPREM",
        "GR_ALMNXGN_OHEONPREM-AO",
    )
    orgTeamsDao.addOrgTeam(
        "74e73bde-026a-4f57-a62f-c5fd28b34858",
        "GR_ALMNXGN_OHEONPREM-TL",
        "OHEONPREM",
        "Technical Leads de OHEONPREM",
        "GR_ALMNXGN_OHEONPREM-AO",
    )
    orgTeamsDao.addOrgTeam(
        "74e73bde-026a-4f57-a62f-c5fd28b34858",
        "GR_ALMNXGN_OHEONPREM-PO",
        "OHEONPREM",
        "Product Owners de OHEONPREM",
        "GR_ALMNXGN_OHEONPREM-AO",
    )
    orgTeamsDao.addOrgTeam(
        "74e73bde-026a-4f57-a62f-c5fd28b34858",
        "GR_ALMNXGN_OHEONPREM-DEV",
        "OHEONPREM",
        "Product Owners de OHEONPREM",
        "GR_ALMNXGN_OHEONPREM-AO",
    )

    # Add Licenses Grupos de Licencias de Jira y Confluence para el CCC
    orgTeamsDao.addOrgTeam(
        "74e73bde-026a-4f57-a62f-c5fd28b34858",
        "GR_ALMNXGN_CCC_SGT_JIRA-LIC",
        "CCC_SGT_JIRA",
        "Grupo Licencias Jira para CCC instancia SGT",
        "GR_ALMNXGN_ALM-AO",
    )
    orgTeamsDao.addOrgTeam(
        "74e73bde-026a-4f57-a62f-c5fd28b34858",
        "GR_ALMNXGN_CCC_SGT_CONFLUENCE-LIC",
        "CCC_SGT_CONFULENCE",
        "Grupo Licencias Confluence para CCC instancia SGT",
        "GR_ALMNXGN_ALM-AO",
    )

    # Add ConfigurationS
    orgToolsDao.addInstanceTool(
        "1f58fa85-fb3a-48ed-817d-f0d382b21a54",
        "cloud-competence-center",
        "ccc",
        "jira",
        "sgt",
        "GR_ALMNXGN_ALM-AO",
        "GR_ALMNXGN_CCC_SGT_JIRA-LIC",
    )
    orgToolsDao.addInstanceTool(
        "1f58fa85-fb3a-48ed-817d-f0d382b21a54",
        "cloud-competence-center",
        "ccc",
        "confluence",
        "sgt",
        "GR_ALMNXGN_ALM-AO",
        "GR_ALMNXGN_CCC_SGT_CONFLUENCE-LIC",
    )
    orgToolsDao.addInstanceTool(
        "1f58fa85-fb3a-48ed-817d-f0d382b21a54",
        "cloud-competence-center",
        "ccc",
        "github",
        "cloud-competence-center",
        "GR_ALMNXGN_ALM-AO",
        "",
    )

    orgToolsDao.addInstanceTool(
        "74e73bde-026a-4f57-a62f-c5fd28b34858",
        "alm-multicloud",
        "almmc",
        "jira",
        "sgt",
        "GR_ALMNXGN_ALM-AO",
        "GR_ALMNXGN_CCC_SGT_JIRA-LIC",
    )
    orgToolsDao.addInstanceTool(
        "74e73bde-026a-4f57-a62f-c5fd28b34858",
        "alm-multicloud",
        "almmc",
        "jira",
        "sgt-advanced",
        "GR_ALMNXGN_ALM-AO",
        "GR_ALMNXGN_CCC_SGT-ADVANCED_JIRA-LIC",
    )
    orgToolsDao.addInstanceTool(
        "74e73bde-026a-4f57-a62f-c5fd28b34858",
        "alm-multicloud",
        "almmc",
        "confluence",
        "sgt",
        "GR_ALMNXGN_ALM-AO",
        "GR_ALMNXGN_CCC_SGT_CONFLUENCE-LIC",
    )
    orgToolsDao.addInstanceTool(
        "74e73bde-026a-4f57-a62f-c5fd28b34858", "alm-multicloud", "almmc", "github", "almmulti-cloud", "GR_ALMNXGN_ALM-AO", ""
    )

    # Add Configuration of Proyectos Jira para la instancia sgt básica.
    jiraProyectDao.addOrgInstanceJiraProyects(
        "74e73bde-026a-4f57-a62f-c5fd28b34858",
        "sgt",
        "CCC_OHE_CORE_ONPREM",
        "CCCOHEONP",
        "GR_ALMNXGN_OHEONPREM-AO",
        "Agile",
        "n57083@santanderglobaltech.com",
        "Detalle",
    )
    jiraProyectDao.addOrgInstanceJiraProyects(
        "74e73bde-026a-4f57-a62f-c5fd28b34858",
        "sgt",
        "CCC_ALMMULTICLOUD",
        "CCCALMMC",
        "GR_ALMNXGN_ALM-AO",
        "Agile",
        "n57083@santanderglobaltech.com",
        "Detalle",
    )
    jiraProyectDao.addOrgInstanceJiraProyects(
        "74e73bde-026a-4f57-a62f-c5fd28b34858",
        "sgt",
        "CCC_ALM_SGS",
        "CCCALMSGS",
        "GR_ALMNXGN_ALM-AO",
        "Agile",
        "n57083@santanderglobaltech.com",
        "Detalle",
    )

    # Lin Team with Jira Roles
    jiraProyectDao.addTeamToOrgJiraInstanceProyect(
        "74e73bde-026a-4f57-a62f-c5fd28b34858", "sgt", "CCCOHEONP", "GR_ALMNXGN_ALMCORE-TL", "Technical-Lead"
    )
    jiraProyectDao.addTeamToOrgJiraInstanceProyect(
        "74e73bde-026a-4f57-a62f-c5fd28b34858", "sgt", "CCCOHEONP", "GR_ALMNXGN_ALMCORE-PO", "Product-Owner"
    )
    jiraProyectDao.addTeamToOrgJiraInstanceProyect(
        "74e73bde-026a-4f57-a62f-c5fd28b34858", "sgt", "CCCOHEONP", "GR_ALMNXGN_ALMCORE-DEV", "Developer"
    )
