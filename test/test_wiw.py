"""Tests para la clase whoiswho."""

from unittest import TestCase

from pony.orm import db_session

from utils.whoiswho import whoiswho


class whoiswho_tst(TestCase):
    """Test who is who methods."""

    @db_session
    def test_add_user(self):
        """Test Add User."""

        wiw = whoiswho()
        mail = "elena@nomail.com"
        wiw.addEmployee(mail, "elena", "626123123", "team-1")
        wiw.addBullet(mail=mail, bullet="comment1")

        empls = wiw.searchToken("comment1")
        self.assertEqual(len(empls), 1)

        mail = "elena2@nomail.com"
        wiw.addEmployee(mail, "elena2", "627123123", "team-2")
        wiw.addBullet(mail=mail, bullet="comment1")

        empls = wiw.searchToken("comment1")
        self.assertEqual(len(empls), 2)

        empls = wiw.searchToken("elena2")
        self.assertEqual(len(empls), 1)

    @db_session
    def test_delete_user(self):
        """Test Delete User."""
        wiw = whoiswho()
        mail = "elena@nomail.com"
        wiw.addEmployee(mail, "elena", "626123123", "comment-pepe")
        wiw.addBullet(mail=mail, bullet="comment1")

        empls = wiw.searchToken("comment-pepe")
        self.assertEqual(len(empls), 1)

        wiw.delEmployee(mail)
        empls = wiw.searchToken("comment-pepe")
        self.assertEqual(len(empls), 0)
