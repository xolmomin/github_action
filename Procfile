web: gunicorn --log-level=INFO --workers 3 config.wsgi:application --error-logfile - --access-logfile -
release: python manage.py migrate --noinput --settings=root.settings
