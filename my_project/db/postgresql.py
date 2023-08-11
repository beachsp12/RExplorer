import psycopg2
from psycopg2 import pool

def create_conn_pool(minconn, maxconn, host, database, user, password):
    return psycopg2.pool.SimpleConnectionPool(minconn, maxconn, host=host, database=database, user=user, password=password)

def get_conn(conn_pool):
    return conn_pool.getconn()

def release_conn(conn_pool, conn):
    conn_pool.putconn(conn)