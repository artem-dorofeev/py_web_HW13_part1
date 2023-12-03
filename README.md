# py_web_HW13_part1 (поетапна реалізація застосунку від дз11 до дз 13)
# почнемо з ДЗ11

1. poetry add fastapi uvicorn sqlalchemy psycopg2 alembic jinja2

2. створюємо структуру проєкту, db.py - підключення до БД, models.py - моделі, config.ini - дані для підключення

3. запускаємо докер, запускаємо дбивер, створюємо базу

4. alembic init migrations

5. migrstions/env.py
    from src.database.models import Base
    from src.database.db import URI

    # target_metadata = None
    target_metadata = Base.metadata
    config.set_main_option("sqlalchemy.url", URI)

6. alembic revision --autogenerate -m 'Init'
7. alembic upgrade head

8. src/schemas.py - Створюємо схеми валідації

9. Додаємо реалізацію маршрутів у файл main.py

10. src/routes/contacts.py - Роутери для модулів contacts містять точки доступу для операцій CRUD із контактами

11. src/repository/contacts.py - методи роботи бази даних із контактами

12. poetry add faker
    poetry add pydantic@^2.4.2 --extras "email"

13. src/database/models.py - заповнення бази(за аналогією з попередніх дз) треба додати poetry add faker

14. додаємо static/covers.css templates/index.html

15. запуск сервера:
    uvicorn main:app --reload

# ДЗ12

16. нам потрібно додати наступні пакети:
    poetry add python-jose["cryptography"]
    poetry add passlib["bcrypt"]
    poetry add python-multipart