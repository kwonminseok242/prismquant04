from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 실행 위치와 무관하게 항상 pq-backend/Prismquant.db를 바라보도록 고정
BASE_DIR = Path(__file__).resolve().parents[2]
DATABASE_FILE = BASE_DIR / "Prismquant.db"
DATABASE_URL = f"sqlite:///{DATABASE_FILE}"

# 각각의 스레드가 달라도 동일한 데이터베이스 파일을 사용하기 위해서 옵션을 줌
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},  # SQLite 전용 옵션
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# DB 세션 의존성
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
