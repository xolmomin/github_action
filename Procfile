web: gunicorn --log-level=INFO --workers 3 root.wsgi:application --error-logfile - --access-logfile -
release: python manage.py migrate --noinput --settings=root.settings
