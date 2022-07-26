from logging import DEBUG, INFO, StreamHandler, basicConfig, getLogger
from logging.handlers import TimedRotatingFileHandler
from pathlib import Path

from pydantic import BaseConfig, BaseModel
from yaml import safe_load

CONFIG_FILE = str(Path(__file__).parent.absolute()) + "/settings.yaml"
LOGFILE_FILE = str(Path(__file__).parent.absolute()) + "/icare.yaml"
basicConfig(
    level=DEBUG,
    format="[%(asctime)s] [%(levelname)s] [%(name)s] [%(funcName)s():%(lineno)s] %(message)s",
    handlers=[
        TimedRotatingFileHandler(
            filename=LOGFILE_FILE, when="midnight", interval=1, backupCount=30, encoding="utf-8", delay=False
        ),
        StreamHandler(),
    ],
)


class Service(BaseModel):
    host: str
    port: str
    environment: str
    workers: int


class Postgres(BaseModel):
    host: str
    port: str
    user: str
    password: str
    database: str


class Graph(BaseModel):
    endpoint: str


class Settings(BaseModel):
    service: Service
    postgres: Postgres
    graph: Graph


def load_settings(path: Path | str = CONFIG_FILE) -> Settings:
    if isinstance(path, str):
        path = Path(path)
    with path.open() as f:
        return Settings.parse_obj(safe_load(f))
