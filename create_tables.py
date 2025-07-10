from sqlalchemy import create_engine
from models import Base

# Replace with your Docker PostgreSQL credentials
DATABASE_URL = "postgresql://postgres:root@localhost:5432/roadmap_db"

engine = create_engine(DATABASE_URL)

# This will create all tables in the database
Base.metadata.create_all(bind=engine)

print("✅ Tables created successfully.")
