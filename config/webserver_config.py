import os
from airflow import configuration as conf
from flask_appbuilder.security.manager import AUTH_LDAP

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = conf.get('core', 'SQL_ALCHEMY_CONN')
CSRF_ENABLED = True
AUTH_TYPE = AUTH_LDAP

AUTH_ROLE_ADMIN = 'Admin'
AUTH_USER_REGISTRATION = True

AUTH_USER_REGISTRATION_ROLE = "Op"

AUTH_LDAP_SERVER = os.environ.get("AUTH_LDAP_SERVER")
AUTH_LDAP_SEARCH = os.environ.get("AUTH_LDAP_SEARCH")
AUTH_LDAP_BIND_USER = 'uid=ssaappuser,ou=serviceaccounts,dc=redhat,dc=com'
AUTH_LDAP_BIND_PASSWORD = os.environ.get("AUTH_LDAP_BIND_PASSWORD")
AUTH_LDAP_UID_FIELD = 'uid'

# LDAPS
AUTH_LDAP_USE_TLS = False
AUTH_LDAP_ALLOW_SELF_SIGNED = False
AUTH_LDAP_TLS_CACERTFILE = os.environ.get("AUTH_LDAP_TLS_CACERTFILE")
