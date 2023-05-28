
import logging.config
import os
from willow_core.library.sqlite_db import SqlLiteDb
from sqlite3 import Connection, Cursor, Error
from typing import Any


class KindleDb(SqlLiteDb):
    def __init__(self, logging_object: Any, db_location: str):
        self._logger: logging.Logger = logging_object.getLogger(type(self).__name__)
        self._logger.setLevel(logging.INFO)
        super().__init__(logging_object, db_location)
        self._check_db_schema()

    @staticmethod
    def add_file_path(relative_file_path: str) -> str:
        return f'{os.path.dirname(__file__)}{relative_file_path}'

    def _check_db_schema(self) -> None:
        if self._check_db_state(['WORDS']):
            self._logger.info(f'DB schema looks good')
        else:
            self._logger.info(f'Tables not found')

    def get_words(self) -> list[str]:
        try:
            conn: Connection = self._db_connect()
            db_cursor: Cursor = conn.cursor()
            db_words_result: list[list] = db_cursor.execute('select word from WORDS').fetchall()
            self._logger.info(f'Retrieved words from Kindle_DB successfully')
            return [row[0] for row in db_words_result]
        except Error as error:
            self._logger.error(f'Error occurred getting words from Kindle_DB: {str(error)}')
