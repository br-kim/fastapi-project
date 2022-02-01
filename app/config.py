import os

env = os.getenv("FASTAPI_ENV")
if env == "production":
    DATABASE_URL = os.getenv("DATABASE_URL")
    DOCS_URL = None
    REDOC_URL = None
    if DATABASE_URL and DATABASE_URL.startswith("postgres://"):
        DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql+asyncpg://", 1)

elif env == "local" or env is None:
    DATABASE_URL = "postgresql+asyncpg://postgres:1234@localhost/sample_app_prd"
    DOCS_URL = "/docs"
    REDOC_URL = "/redoc"
    if os.getenv("TEST") == "TEST":
        DATABASE_URL = "postgresql+asyncpg://postgres:1234@localhost/sample_app_dev"
