# High-level Development Log for TUCTF Website

## Initial project setup: 20231026

- Updated README.md
- Created local venv

```powershell
python -m venv venv

.\venv\Scripts\activate
```

- Created `.gitignore` from: <https://github.com/jpadilla/django-project-template/blob/master/.gitignore>

    - Added `venv/` to `.gitignore`

- Create `requirments.txt` and added `django`
- Installed requirements to virtual env: `pip install -r requirements.txt`

- Created django project and app

```bash
# Create django project
django-admin startproject tuctf
# Create django app within project
cd tuctf
python manage.py startapp core_site
# Modify settings.py to include 'core_site' in INSTALLED _APPS
```

- Test run and create super user (local envinroment)

```bash
python manage.py migrate
python manage.py runserver # Access in web

python manage.py createsuperuser
```

- Commited: `Initial project setup`

- Mapped main urls.py to core_site
- Created `base.html`, `index.html`, and a basic `style.css` (inspo from ChatGPT)

- Committed

- Installed `django_bootstrap5`
- Split out `tuctf_2023` from main page (but will make home for duration of comp)
- Added `rules_2023`
- Spent way too much time messing with CSS and adding dark mode toggle

- Committed `CSS and Dark Mode Toggle`