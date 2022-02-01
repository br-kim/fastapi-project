import os

env = os.getenv("FASTAPI_ENV")
if env == "production":
    DATABASE_URL = os.getenv("DATABASE_URL")
    if DATABASE_URL and DATABASE_URL.startswith("postgres://"):
        DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql+asyncpg://", 1)

elif env == "local" or env is None:
    DATABASE_URL = "postgresql+asyncpg://postgres:1234@localhost/sample_app_prd"
    if os.getenv("TEST") == "TEST":
        DATABASE_URL = "postgresql+asyncpg://postgres:1234@localhost/sample_app_dev"
