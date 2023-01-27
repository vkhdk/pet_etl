#importing public libraries
from sqlalchemy import create_engine

#importing internal modules
from ETL_secrets import postgres_db, \
                    postgres_user, \
                    postgres_password, \
                    postgres_port, \
                    postgres_host

engine = create_engine(
    'postgresql://{user}:{password}@{host}:{port}/{bd_name}'.format(
        user = postgres_user,
        password = postgres_password,
        host = postgres_host,
        port = postgres_port,
        bd_name = postgres_db)
        )
