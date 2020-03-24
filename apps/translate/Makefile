serve:
	flask run
po:
	pybabel extract -F translations/babel.cfg -k lazy_gettext -o translations/messages.pot .

init_lang:
	pybabel init -i translations/messages.pot -d translations -l $(lang)

update_lang:
	pybabel update -i translations/messages.pot -d translations/

compile:
	pybabel compile -d translations
