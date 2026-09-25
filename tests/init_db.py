from src.database.db import engine
from src.database.models import Base, User, Contact

if __name__ == "__main__":
    print("Создаем таблицы в базе данных...")
    Base.metadata.create_all(bind=engine)
    print("Таблицы успешно созданы!")