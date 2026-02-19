import os
import ast

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


def read_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def test_required_files_exist():
    # בדיקות בסיסיות שהקבצים המרכזיים קיימים
    assert os.path.isfile(os.path.join(PROJECT_ROOT, "app.py"))
    assert os.path.isfile(os.path.join(PROJECT_ROOT, "requirements.txt"))
    assert os.path.isdir(os.path.join(PROJECT_ROOT, "resources"))


def test_app_has_flask_run_config():
    # בדיקה סטטית: בקובץ app.py יש host 0.0.0.0 ופורט 5000 (כמו שנדרש לדוקר)
    content = read_file(os.path.join(PROJECT_ROOT, "app.py"))
    assert "host='0.0.0.0'" in content or 'host="0.0.0.0"' in content
    assert "port=5000" in content


def test_requirements_contains_flask_and_restplus():
    # בדיקה סטטית: לוודא שה-deps המרכזיים קיימים
    req = read_file(os.path.join(PROJECT_ROOT, "requirements.txt")).lower()
    assert "flask==" in req
    assert "flask-restplus==" in req
    assert "flask-sqlalchemy==" in req


def test_app_py_is_valid_python_syntax():
    # בדיקת תחביר: לוודא שהקובץ ניתן לפענוח (לא מריץ אותו!)
    content = read_file(os.path.join(PROJECT_ROOT, "app.py"))
    ast.parse(content)
