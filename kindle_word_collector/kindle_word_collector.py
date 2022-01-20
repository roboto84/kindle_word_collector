# kindle vocabulary collector
import os
import time
import logging.config
from typing import Any
from dotenv import load_dotenv
from lexicon.library.lexicon import Lexicon
from bin.kindle_db import KindleDb


class KindleWordCollector:
    def __init__(self, logging_object: Any, webster_key: str, oxford_app_id: str, oxford_key: str,
                 sql_lite_db_path: str, kindle_sql_lite_db_path: str):
        self._logger: logging.Logger = logging_object.getLogger(type(self).__name__)
        self._logger.setLevel(logging.INFO)
        self._lexicon: Lexicon = Lexicon(webster_key, oxford_app_id, oxford_key, sql_lite_db_path, logging_object)
        self._kindleDb: KindleDb = KindleDb(logging_object, kindle_sql_lite_db_path)

    def run_word_collector(self) -> None:
        try:
            db_count: int = 0
            web_count: int = 0
            word_not_found_count: int = 0
            words_not_found: list[str] = []
            kindle_words: list[str] = self._kindleDb.get_words()
            kindle_words_count: int = len(kindle_words)
            print(f'\n Number of Words in Kindle DB: {kindle_words_count}')
            print(f'\n Collection definitions and inserting into Lexicon: {len(kindle_words)}')
            for word in kindle_words:
                word_def: dict = self._lexicon.get_definition(word)
                if word_def['source'] == 'web':
                    time.sleep(8)
                    web_count += 1
                    if not word_def['definition_is_acceptable']:
                        word_not_found_count += 1
                        words_not_found.append(word)
                elif word_def['source'] == 'db':
                    db_count += 1
            self.print_report(db_count, web_count, word_not_found_count, words_not_found)

        except KeyboardInterrupt:
            self._logger.info('Received a KeyboardInterrupt... closing')
            exit()

    @staticmethod
    def print_report(db_num: int, web_num: int, word_not_found_num: int, words_not_found: list[str]):
        print('')
        print(f'  Words already in Lexicon DB: {round(db_num / (db_num + web_num) * 100, 2)}%')
        print(f'  Number of Words already in Lexicon: {db_num}')
        print('')
        print(f'  Number of Words searched on web resources: {web_num}')
        print(f'  Number of Words added from web resources: {web_num - word_not_found_num}')
        print(f'  Number of Words not found on web resources: {word_not_found_num}')
        print(f'  Words not found on web resources: {str(words_not_found)}')
        print('')


if __name__ == '__main__':
    logging.config.fileConfig(fname=os.path.abspath('kindle_word_collector/bin/logging.conf'), disable_existing_loggers=False)
    logger: logging.Logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    try:
        load_dotenv()
        MERRIAM_WEBSTER_API_KEY: str = os.getenv('MERRIAM_WEBSTER_API_KEY')
        OXFORD_APP_ID: str = os.getenv('OXFORD_APP_ID')
        OXFORD_APP_KEY: str = os.getenv('OXFORD_APP_KEY')
        SQL_LITE_DB: str = os.getenv('SQL_LITE_DB')
        KINDLE_SQLITE_DB: str = os.getenv('KINDLE_SQLITE_DB')

        print(f'\nKindle word collector running')
        word_collector: KindleWordCollector = KindleWordCollector(
            logging,
            MERRIAM_WEBSTER_API_KEY,
            OXFORD_APP_ID,
            OXFORD_APP_KEY,
            SQL_LITE_DB,
            KINDLE_SQLITE_DB
        )
        word_collector.run_word_collector()
    except TypeError:
        logger.error('Received TypeError: Check that the .env project file is configured correctly')
        exit()