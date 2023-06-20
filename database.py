from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./full_secop.db"
# SQLALCHEMY_DATABASE_URL = "sqlite:///./final_secop_db.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"
# SQLALCHEMY_DATABASE_URL_2 = "sqlite:///./full_secop.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# engine_2 = create_engine(
#     SQLALCHEMY_DATABASE_URL_2, connect_args={"check_same_thread": False}
# )

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# SessionLocal_2 = sessionmaker(autocommit=False, autoflush=False, bind=engine_2)

Base = declarative_base()