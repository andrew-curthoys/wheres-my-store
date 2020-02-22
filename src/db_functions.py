import psycopg2
from psycopg2 import extras
from config import config


def pg_select(query_string : str) -> tuple:
    """
    Parameters
    ----------
    query_string : str
        The SELECT query to run on the database

    Returns
    -------
    query_response : tuple
        A tuple of tuples with each inner tuple representing a DB row
    """

    # connect to the PostgreSQL database server
    conn = None
    try:
        # read connection parameters
        params = config()
 
        # connect to the PostgreSQL server
        print('Connecting to PostgreSQL database...')
        conn = psycopg2.connect(**params)
      
        # create a cursor
        cur = conn.cursor()
        
        # execute a statement
        print('Executing query...')
        cur.execute(query_string)
 
        # run the query
        query_response = cur.fetchall()

       # close the communication with the PostgreSQL
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
    
    return query_response


def pg_insert(db_name : str, insert_values : str):
    """
    Parameters
    ----------
    db_name : str
        The name of the database to connect to
    
    insert_values : str
        A string of values to insert into the database
    """
    
    # connect to the PostgreSQL database server
    conn = None
    try:
        # read connection parameters
        params = config()
 
        # connect to the PostgreSQL server
        print('Connecting to PostgreSQL database...')
        conn = psycopg2.connect(**params)
      
        # create a cursor
        cur = conn.cursor()
        
        # get insert statement
        insert_statement = get_insert_statement(db_name)

        # execute a statement
        print('Executing insert query...')
        psycopg2.extras.execute_batch(cur, insert_statement, insert_values)

        # commit to the db
        conn.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


def get_insert_statement(db_name : str) -> str:
    """
    Parameters
    ----------
    db_name : str
        The name of the database to connect to
    
    Returns
    -------
    insert_statement : str
        The insert statement to add data to the specified database
    """
    insert_statement = f"""INSERT INTO {db_name}(
                                    store_id, store_name, address, phone_number
                                    )
                            VALUES (%s, %s, %s, %s)
                            ON CONFLICT (store_id) DO NOTHING"""
    
    return insert_statement