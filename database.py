from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import settings

engine = create_engine(settings.SQLALCHEMY_DATABASE_URI, echo=False)

Session = sessionmaker(bind=engine)
