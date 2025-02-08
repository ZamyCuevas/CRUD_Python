from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# Configuración de la conexión local a MySQL con usuario root
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:12345678@127.0.0.1:3306/test"

# Crear el engine de SQLAlchemy
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"ssl_disabled": True}  
)

# Crear la sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para modelos
Base = declarative_base()
