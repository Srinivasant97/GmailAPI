import psycopg2
from email_actions import config 

connection = psycopg2.connect(
    database = config.DB_NAME,
    host = config.DB_HOST_NAME,
    user = config.DB_USERNAME,
    password = config.DB_PASSWORD,
    port = config.DB_PORT
)

def run_db_command(command):
    data = ""
    try:
        cursor = connection.cursor()
        cursor.execute(command)
        data = cursor.fetchall()
        cursor.close()
        connection.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        pass
        #print(error)
    finally:
        if connection is not None:
            connection.close()
        return data

def table_creation():
    run_db_command(
        """
        CREATE TABLE IF NOT EXISTS email_meta_data (
            message_id VARCHAR(50) PRIMARY KEY,
            from_email VARCHAR(100) NOT NULL,
            to_email VARCHAR(100) NOT NULL,
            created_at TIMESTAMPTZ NOT NULL,
            subject VARCHAR(500) NOT NULL
        );
        """
    )
    print("Request Completed")

def insert_data(values):
    command = """
        INSERT INTO email_meta_data (message_id,from_email,to_email,created_at,subject)
        VALUES
        """
    command +=values + ' ON CONFLICT (message_id) DO NOTHING;'
    run_db_command(command)
    print("Data Added Successfully")

def get_data(values):
    command = """
        SELECT message_id FROM email_meta_data 
        WHERE
        """
    command +=values + ';'
    return run_db_command(command)
