git push heroku master --force
Counting objects: 106, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (97/97), done.
Writing objects: 100% (106/106), 1.67 MiB | 272.00 KiB/s, done.
Total 106 (delta 6), reused 0 (delta 0)
remote: Compressing source files... done.
remote: Building source:
remote: 
remote: -----> Python app detected
remote:  !     Python has released a security update! Please consider upgrading to python-3.7.3
remote:        Learn More: https://devcenter.heroku.com/articles/python-runtimes
remote: -----> Installing python-3.7.1
remote: -----> Installing pip
remote: -----> Installing SQLite3
remote: -----> Installing requirements with pip
remote:        Collecting dj-database-url==0.5.0 (from -r /tmp/build_fde182505ff995d22d9e8142026ec228/requirements.txt (line 1))
remote:          Downloading https://files.pythonhosted.org/packages/d4/a6/4b8578c1848690d0c307c7c0596af2077536c9ef2a04d42b00fabaa7e49d/dj_database_url-0.5.0-py2.py3-none-any.whl
remote:        Collecting dj-static==0.0.6 (from -r /tmp/build_fde182505ff995d22d9e8142026ec228/requirements.txt (line 2))
remote:          Downloading https://files.pythonhosted.org/packages/2b/8f/77a4b8ec50c821193bf9682c7896f12fd0418eb3711a7d66796ede59c23b/dj-static-0.0.6.tar.gz
remote:        Collecting Django==2.2.3 (from -r /tmp/build_fde182505ff995d22d9e8142026ec228/requirements.txt (line 3))
remote:          Downloading https://files.pythonhosted.org/packages/39/b0/2138c31bf13e17afc32277239da53e9dfcce27bac8cb68cf1c0123f1fdf5/Django-2.2.3-py3-none-any.whl (7.5MB)
remote:        Collecting python-decouple==3.1 (from -r /tmp/build_fde182505ff995d22d9e8142026ec228/requirements.txt (line 4))
remote:          Downloading https://files.pythonhosted.org/packages/9b/99/ddfbb6362af4ee239a012716b1371aa6d316ff1b9db705bfb182fbc4780f/python-decouple-3.1.tar.gz
remote:        Collecting pytz==2019.1 (from -r /tmp/build_fde182505ff995d22d9e8142026ec228/requirements.txt (line 5))
remote:          Downloading https://files.pythonhosted.org/packages/3d/73/fe30c2daaaa0713420d0382b16fbb761409f532c56bdcc514bf7b6262bb6/pytz-2019.1-py2.py3-none-any.whl (510kB)
remote:        Collecting sqlparse==0.3.0 (from -r /tmp/build_fde182505ff995d22d9e8142026ec228/requirements.txt (line 6))
remote:          Downloading https://files.pythonhosted.org/packages/ef/53/900f7d2a54557c6a37886585a91336520e5539e3ae2423ff1102daf4f3a7/sqlparse-0.3.0-py2.py3-none-any.whl
remote:        Collecting static3==0.7.0 (from -r /tmp/build_fde182505ff995d22d9e8142026ec228/requirements.txt (line 7))
remote:          Downloading https://files.pythonhosted.org/packages/87/b0/9cf15108b73c4f2ffffe11d237c938f57785f55d3693d822d565432cb680/static3-0.7.0.tar.gz
remote:        Collecting gunicorn==19.8.1 (from -r /tmp/build_fde182505ff995d22d9e8142026ec228/requirements.txt (line 8))
remote:          Downloading https://files.pythonhosted.org/packages/55/cb/09fe80bddf30be86abfc06ccb1154f97d6c64bb87111de066a5fc9ccb937/gunicorn-19.8.1-py2.py3-none-any.whl (112kB)
remote:        Collecting psycopg2==2.7.4 (from -r /tmp/build_fde182505ff995d22d9e8142026ec228/requirements.txt (line 9))
remote:          Downloading https://files.pythonhosted.org/packages/74/83/51580322ed0e82cba7ad8e0af590b8fb2cf11bd5aaa1ed872661bd36f462/psycopg2-2.7.4.tar.gz (425kB)
remote:        Installing collected packages: dj-database-url, static3, dj-static, sqlparse, pytz, Django, python-decouple, gunicorn, psycopg2
remote:          Running setup.py install for static3: started
remote:            Running setup.py install for static3: finished with status 'done'
remote:          Running setup.py install for dj-static: started
remote:            Running setup.py install for dj-static: finished with status 'done'
remote:          Running setup.py install for python-decouple: started
remote:            Running setup.py install for python-decouple: finished with status 'done'
remote:          Running setup.py install for psycopg2: started
remote:            Running setup.py install for psycopg2: finished with status 'done'
remote:        Successfully installed Django-2.2.3 dj-database-url-0.5.0 dj-static-0.0.6 gunicorn-19.8.1 psycopg2-2.7.4 python-decouple-3.1 pytz-2019.1 sqlparse-0.3.0 static3-0.7.0
remote: 
remote: -----> $ python manage.py collectstatic --noinput
remote:        Traceback (most recent call last):
remote:          File "manage.py", line 21, in <module>
remote:            main()
remote:          File "manage.py", line 17, in main
remote:            execute_from_command_line(sys.argv)
remote:          File "/app/.heroku/python/lib/python3.7/site-packages/django/core/management/__init__.py", line 381, in execute_from_command_line
remote:            utility.execute()
remote:          File "/app/.heroku/python/lib/python3.7/site-packages/django/core/management/__init__.py", line 325, in execute
remote:            settings.INSTALLED_APPS
remote:          File "/app/.heroku/python/lib/python3.7/site-packages/django/conf/__init__.py", line 79, in __getattr__
remote:            self._setup(name)
remote:          File "/app/.heroku/python/lib/python3.7/site-packages/django/conf/__init__.py", line 66, in _setup
remote:            self._wrapped = Settings(settings_module)
remote:          File "/app/.heroku/python/lib/python3.7/site-packages/django/conf/__init__.py", line 157, in __init__
remote:            mod = importlib.import_module(self.SETTINGS_MODULE)
remote:          File "/app/.heroku/python/lib/python3.7/importlib/__init__.py", line 127, in import_module
remote:            return _bootstrap._gcd_import(name[level:], package, level)
remote:          File "<frozen importlib._bootstrap>", line 1006, in _gcd_import
remote:          File "<frozen importlib._bootstrap>", line 983, in _find_and_load
remote:          File "<frozen importlib._bootstrap>", line 967, in _find_and_load_unlocked
remote:          File "<frozen importlib._bootstrap>", line 677, in _load_unlocked
remote:          File "<frozen importlib._bootstrap_external>", line 728, in exec_module
remote:          File "<frozen importlib._bootstrap>", line 219, in _call_with_frames_removed
remote:          File "/tmp/build_fde182505ff995d22d9e8142026ec228/myproject/settings.py", line 24, in <module>
remote:            SECRET_KEY=config ("SECRECT_KEY")
remote:          File "/app/.heroku/python/lib/python3.7/site-packages/decouple.py", line 197, in __call__
remote:            return self.config(*args, **kwargs)
remote:          File "/app/.heroku/python/lib/python3.7/site-packages/decouple.py", line 85, in __call__
remote:            return self.get(*args, **kwargs)
remote:          File "/app/.heroku/python/lib/python3.7/site-packages/decouple.py", line 70, in get
remote:            raise UndefinedValueError('{} not found. Declare it as envvar or define a default value.'.format(option))
remote:        decouple.UndefinedValueError: SECRECT_KEY not found. Declare it as envvar or define a default value.
remote: 
remote:  !     Error while running '$ python manage.py collectstatic --noinput'.
remote:        See traceback above for details.
remote: 
remote:        You may need to update application code to resolve this error.
remote:        Or, you can disable collectstatic for this application:
remote: 
remote:           $ heroku config:set DISABLE_COLLECTSTATIC=1
remote: 
remote:        https://devcenter.heroku.com/articles/django-assets
remote:  !     Push rejected, failed to compile Python app.
remote: 
remote:  !     Push failed
remote: Verifying deploy...
remote: 
remote: !	Push rejected to myproject-jp.
remote: 
To https://git.heroku.com/myproject-jp.git
 ! [remote rejected] master -> master (pre-receive hook declined)
error: failed to push some refs to 'https://git.heroku.com/myproject-jp.git'

