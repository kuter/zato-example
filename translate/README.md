# Flask-Babel example

## Installation

Create and activate virtualenv first:

```
$ virtualenv -p python3 ~/virtualenvs/flask-babel-blog
$ source ~/virtualenv/flask-babel-blog/bin/activate
```

then install requirements:

```
$ pip install -r requirements.txt
```

## pybabel commnands

collect all messages from python files and generate POT:

```
$ pybabel extract -F translations/babel.cfg -k lazy_gettext -o translations/messages.pot .
```

create directory structure from POT file for given language:

```
$ pybabel init -i translations/messages.pot -d translations/ -l pl
```

update existing message directories:

```
$ pybabel update -i translations/messages.pot -d translations/
```

then compile messages to MO files:

```
$ pybabel compile -d translations
```

## Running project

```
$ flask run
```

## Example usage

```
$ curl -XPOST \
    -F "text=Welcome" \
    -H 'Accept-Language: pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7' \
    localhost:5000
```
