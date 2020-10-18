from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from .settings import PostgresConfiguration

pg = PostgresConfiguration()
engine = create_engine(pg.postgres_db_path)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

if __name__ == "__main__":
    print(f'{pg.postgres_db_path}')