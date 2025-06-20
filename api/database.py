##databse configuration"""
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base,sessionmaker

SQLALCHELY_DATABASE_URL="sqlite:///./movies.db"

### creation de moteurde base de données (engine) qui établit la connexion avec notre base sqlite(movie.db)
engine=create_engine(
    SQLALCHELY_DATABASE_URL, connect_args={"check_same_thread":False}
)

##definir la session local qui permet de créer des sessions pour interagir avec la base de données
SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)

##définir la base, qui servira de clase pour nos modèles sqlalchemy
Base=declarative_base()

##tester la connection
if __name__=="__main__":
    try:
        with engine.connect() as conn:
            print("connexion réussi")
    except Exception as e:
        print(f"errur de connexion à la database : {e}")