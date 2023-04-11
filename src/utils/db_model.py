import os
from datetime import datetime

from loguru import logger
from pony.orm import Database, Optional, PrimaryKey, Required, Set, commit, db_session, select, sql_debug

# Aseguro que el path existe y trabajo con el path absoluto
dbFilePath = os.environ["DB_BASE_PATH"]
if not (os.path.exists(dbFilePath)):
    os.makedirs(dbFilePath)
dbFileAbsPath = os.path.abspath(dbFilePath)


dbFile = f"{dbFileAbsPath}/sqllite.db"
dbTest = os.getenv("DB_TEST", False)

db = Database()
# ========================================


class Team(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Optional(str)
    shortname = Optional(str)
    org = Optional(str)
    owner = Optional(str)
    description = Optional(str)
    jira_proyects_owner = Set("JiraProyect")
    jira_proyect_teams = Set("JiraProjectTeam")


class JiraProyect(db.Entity):
    id = PrimaryKey(int, auto=True)
    key = Optional(str)
    name = Optional(str)
    org = Optional(str)
    instance_name = Optional(str)
    owner = Required(Team)
    template = Optional(str)  # Nombre de los proyectos Templates que se gestiona para la instancia
    description = Optional(str)
    proyect_lead = Optional(str)
    jira_project_teams = Set("JiraProjectTeam")


class OrgTool(db.Entity):
    id = PrimaryKey(int, auto=True)
    org_id = Optional(str)
    org_name = Optional(str)  # organzacion
    org_acronym = Optional(str)
    tool = Optional(str)  # Tipo herramienta SaaS
    instance_name = Optional(str)  # nombre instancia o nombre organizacion github
    owner = Optional(str)
    licences = Optional(str)  # Grupo Licencias Cuando sea Necesario


class JiraProjectTeam(db.Entity):
    id = PrimaryKey(int, auto=True)
    team = Required(Team)
    role = Optional(str)
    jira_project = Required(JiraProyect)


# ==========

# Modo Debug Pony
sql_debug(False)

logger.info("Generamos el Mapping")


@db.on_connect(provider="sqlite")
def sqlite_case_sensitivity(db, connection):
    cursor = connection.cursor()
    logger.info("PRAGMA Case case_sensitive_like OFF")
    cursor.execute("PRAGMA case_sensitive_like = OFF")


if dbTest and dbTest.lower() == "true":
    db.bind(provider="sqlite", filename=":sharedmemory:")
    logger.info("Creo base dedatos en Memoria")
else:
    db.bind("sqlite", dbFile, create_db=True)
    logger.info(f"Abrimos Instancia BBDDs {dbFile}")


db.generate_mapping(create_tables=True)
