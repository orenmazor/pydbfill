import unittest
import pymysql
import pytest

from pydbfill.pydbfill import connection, describe_table, fill_table


HOST = "db"
USERNAME = "root"
PASSWORD = "0xDEADBEEF"
PORT = 3306
DB = "test"


class PyDBFillTest(unittest.TestCase):
    """Test any of this even works."""

    def test_mysql_connection(self: unittest.TestCase) -> None:
        """Test we can connect to mysql properly."""
        conn = connection(
            host=HOST, username=USERNAME, password=PASSWORD, port=PORT, db=DB
        )

        conn.ping()

    def test_mysql_table_description(self: unittest.TestCase) -> None:
        """Confirm we can get a table description."""
        conn = connection(
            host=HOST, username=USERNAME, password=PASSWORD, port=PORT, db=DB
        )

        field_mapping = describe_table(conn, "users")
        assert field_mapping["email"] == "varchar(255)"
        assert field_mapping["password"] == "varchar(255)"

    def test_mysql_table_fill(self: unittest.TestCase) -> None:
        """Confirm we can write an arbitrary number of records."""
        conn = connection(
            host=HOST, username=USERNAME, password=PASSWORD, port=PORT, db=DB
        )

        current_count = self._get_record_count(conn, "users")

        fill_table(conn=conn, table_name="users", count=123)

        new_count = self._get_record_count(conn, "users")

        assert new_count - current_count == 123

    def _get_record_count(
        self: unittest.TestCase, conn: pymysql.Connection, table_name: str
    ) -> None:
        with conn.cursor() as cursor:
            sql = f"select count(*) from {table_name}"
            cursor.execute(sql)
            count = cursor.fetchone()
            return count["count(*)"]
