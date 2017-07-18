

PROFILE = ""

DB_CONFIG = {
        "local": {"host": "172.17.0.2", "port": 27017, "database": "local"},
        "devqa": {"host": "120.172.201.75", "port": 27017, "database": "local"},
    }


def get_database_configurations():
    return DB_CONFIG[PROFILE]
