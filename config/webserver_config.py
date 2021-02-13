import os
from airflow import configuration as conf
from flask_appbuilder.security.manager import AUTH_LDAP

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = conf.get('core', 'SQL_ALCHEMY_CONN')
CSRF_ENABLED = True
AUTH_TYPE = os.environ.get("AUTH_TYPE")

AUTH_ROLE_ADMIN = os.environ.get("AUTH_ROLE_ADMIN")
AUTH_USER_REGISTRATION = os.environ.get("AUTH_USER_REGISTRATION")

AUTH_USER_REGISTRATION_ROLE = os.environ.get("AUTH_USER_REGISTRATION_ROLE")

AUTH_LDAP_SERVER = os.environ.get("AUTH_LDAP_SERVER")
AUTH_LDAP_SEARCH = os.environ.get("AUTH_LDAP_SEARCH")
AUTH_LDAP_BIND_USER = os.environ.get("AUTH_LDAP_BIND_USER")
AUTH_LDAP_BIND_PASSWORD = os.environ.get("AUTH_LDAP_BIND_PASSWORD")
AUTH_LDAP_UID_FIELD = os.environ.get("AUTH_LDAP_UID_FIELD")

# LDAPS
AUTH_LDAP_USE_TLS = os.environ.get("AUTH_LDAP_USE_TLS")
AUTH_LDAP_ALLOW_SELF_SIGNED = os.environ.get("AUTH_LDAP_ALLOW_SELF_SIGNED")
AUTH_LDAP_TLS_CACERTFILE = os.environ.get("AUTH_LDAP_TLS_CACERTFILE")
