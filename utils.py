import yaml
from sqlalchemy import create_engine


def load_config(config_file) -> dict:
    """Read the YAML config file

    Args:
        config_file (str): YAML configuration file path
    """
    with open(config_file, "r") as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
            
            
def get_db_engine(config_file, db_name=None):
    # load the configurations
    config = load_config(config_file=config_file)
    # Database connection configuration
    dbms = config['database']['dbms']
    db_host = config['database']['host']
    db_port = config['database']['port']
    db_user = config['database']['user']
    db_pass = config['database']['password']
    db_name = db_name if db_name else ''
    
    # creating SQLAlchemy Engine instance
    con_str = f'postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}'
    db_engine = create_engine(con_str, echo=True, future=True)
    
    return db_engine