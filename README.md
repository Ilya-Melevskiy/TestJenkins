# 1. Структура
mkdir api-tests && cd api-tests
mkdir -p api/models tests utils config
touch api/__init__.py api/models/__init__.py tests/__init__.py utils/__init__.py config/__init__.py

# 2. venv
python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate

# 3. Зависимости
pip install --upgrade pip
# создать requirements.txt с пинами
pip install -r requirements.txt

# 4. Конфиги
cp .env.example .env               # после создания .env.example
# создать .gitignore

# 5. Файлы проекта
touch config/settings.py pytest.ini
touch api/client.py api/endpoints.py
touch api/models/user.py api/models/common.py
touch tests/conftest.py tests/test_users.py
touch utils/data_factory.py utils/assertions.py
touch README.md

# 6. Проверка
python -c "from config.settings import settings; print(settings)"
pytest --co -q
allure --version

# 7. Git
git init
git add .
git status                        # убедиться, что .env не в списке!
git commit -m "Initial structure"