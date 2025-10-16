## Setup Instructions

1. **Create virtual environment and activate**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install requirements**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set env and put values there as per .env.example**
   ```bash
   cp .env.example .env
   # Edit .env file with your values
   ```

4. **Run migrate to apply migration**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Run server command and see on admin if its running or not**
   ```bash
   python manage.py runserver
   ```
   Visit: http://127.0.0.1:8000/admin/