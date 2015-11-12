from os.path import expanduser
import configparser

def noconfig_msg():
    return \
'''please set config file: \033[0;33m~/.tracrc\033[0m in format of:
\033[0;33m[server]
login: https://<account>:<password>@<login-endpoint>\033[0m'''

class Config(object):
    def __init__(self, configfile):
        parser = configparser.SafeConfigParser()
        parser.read(expanduser(configfile))
        self.login = parser.get("server", "login")
