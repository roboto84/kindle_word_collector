<h1 align="center">kindle_word_collector</h1>

<div align="center">
	<img src="assets/kindle_word_collector.png" width="250" title="kindle_word_collector logo">
</div>

## About
`kindle_word_collector` is a command line tool that collects words looked up on an
Amazon kindle reader, which are stored on its SQLite DB, and adds them to
[Lexicon](https://github.com/roboto84/lexicon).

## Install
This project is managed with [Poetry](https://github.com/python-poetry/poetry). With Poetry installed correctly, simply clone this project and install its dependencies:
- Clone repo
    ```
    git clone https://github.com/roboto84/kindle_word_collector.git
    ```
    ```
    cd kindle_word_collector
    ```
- Install dependencies
    ```
    poetry install
    ```

## API Keys
Before you begin with `kindle_word_collector` you first need a dictionary API key.

- Merriam-Webster Dictionary (Required) - https://dictionaryapi.com

## Environmental Variables
`kindle_word_collector` requires that an `.env` file is available in the *same* directory it is running under.

- The format of the `.env` file should contain the following as defined environmental variables:
    - `MERRIAM_WEBSTER_API_KEY` : Key obtained in the previous step.
    - `SQL_LITE_DB`: Location of Lexicon SQLite DB.
    - `KINDLE_SQLITE_DB`: Location of Kindle SQLite DB (from the Kindle itself).

- An explained `.env` file format is shown below:
    ```
    MERRIAM_WEBSTER_API_KEY=<Merriam Webster API Key>
    SQL_LITE_DB=<Lexicon DB Location>
    KINDLE_SQLITE_DB=<Kindle DB Location>
    ```

- A typical `.env` file may look like this:
    ```
    MERRIAM_WEBSTER_API_KEY=9d1e4882-x649-20f4-34h5-7eole23fe931
    SQL_LITE_DB=/home/data/lexicon.db
    KINDLE_SQLITE_DB=/run/media/roboto/Kindle/system/vocabulary/vocab.db
    ```

## Usage
- Run the script once the environment (`.env`) file is created:
    ```
    poetry run python kindle_word_collector/kindle_word_collector.py
    ```

## Commit Conventions
Git commits follow [Conventional Commits](https://www.conventionalcommits.org) message style as explained in detail on their website.

<br/>
<sup>
    <a href="https://www.flaticon.com/free-icons/kindle" title="kindle icons">Kindle icons created by iconixar - Flaticon</a>
</sup>
