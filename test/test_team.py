"""Casos de Test para la clase Team."""
from unittest import TestCase

from pony.orm import db_session

from utils.db_model import Team
from utils.mj_teams import mjTeam


class team_tst(TestCase):
    """Test who is who methods."""

    @db_session
    def test_add_team_01(self):
        """Creamos un team con un Padre."""
        teamName = "team_hijo_01"
        teamParentName = "team_padre_01"
        mjTeam.addTeam(teamName, teamParentName, "description hijo")
        oHijo = Team.get(team=teamName)
        self.assertEqual(oHijo.team, teamName)
        self.assertEqual(oHijo.parent_team.team, teamParentName)

    @db_session
    def test_add_team_02(self):
        """Test Crear un team sin Padre."""
        teamName = "team_hijo_02"
        teamParentName = "no-team"
        mjTeam.addTeam(teamName, "", "description hijo")
        oHijo = Team.get(team=teamName)
        self.assertEqual(oHijo.team, teamName)
        self.assertEqual(oHijo.parent_team.team, teamParentName)
