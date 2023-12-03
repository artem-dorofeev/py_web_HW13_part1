# py_web_HW13_part1
start HW11, upd to HW12 upd to HW13

1. poetry add fastapi uvicorn sqlalchemy psycopg2 alembic

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

12. src/database/models.py - заповнення бази(за аналогією з попередніх дз) треба додати poetry add faker

13. додаємо static/covers.css templates/index.html

14. запуск сервера:
    uvicorn main:app --reload