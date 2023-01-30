#importing public libraries
from sqlalchemy import create_engine
from sqlalchemy import text

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

def load_df_to_tpm_table(df, table_name, dtypes):
    print(f'{table_name} loading into DB...')
    df.to_sql(f'{table_name}_tmp',
        #the engine is set up above in the code 
        con = engine, 
        if_exists = 'replace', 
        index = False,
        chunksize = 10_000, 
        method = 'multi',
        #like this 
        #weather_dtypes = {'time': Time, 'date': Date}
        dtype = dtypes)
    print(f'{table_name}_tmp loaded')

def load_tmp_table_to_prod_table(sql_query):
    with engine.connect() as con:
        
        #SQL query looks like
        #"""
        #insert into tk.facts(
        #   "ID"
        #   , x_in
        #   , y_in
        #select
        #   "ID"
        #   , x_in
        #   , y_in
        #from dw.facts_tmp;
        #"""
        con.execute(text(sql_query))