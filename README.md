# pet etl

# write to postgres from jupyter
use this code:

from sqlalchemy import create_engine
engine = create_engine('postgresql://user:password@postgres:5432/postgres_db')
name = 'city_id'
data_xlsx.to_sql(name, engine, if_exists='replace')

where
- "postgresql" - type in engine
- "user" - user from docker-compose sittings (POSTGRES_USER:)
- "password" - password from docker-compose sittings (POSTGRES_PASSWORD:)
- "postgres" - host == container name "postgres" is set before the build command
- "5432" - port from docker-compose sittings (ports:)
- "postgres_db" - DB name from docker-compose sittings (POSTGRES_DB:)

## Task list:

- need run python scripts in docker
- need add import connection sittings to docker-compose.yml from secrets
