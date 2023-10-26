# TUCTF Website

An overengineered Django website for hosting a static TUCTF website, a cyber Capture the Flag (CTF) competition designed for high schoolers, college students, and professionals.

This website serves as the primary interface for participants, offering details about the event, links to the CTFd instance and registration, schedule, and more.

## Development Environment Setup

### Prerequisites
- Python (version 3.10 or higher)
- pip

### Installation


- **Clone the Repository:**

   ```
   git clone git@gitlab.root66tulsa.club:c6/tuctf-website.git
   cd tuctf-website
   ```

- **Set Up a Virtual Environment (Optional but Recommended):**

   ```bash
   # Create virtual environment
   python -m venv venv
   # Activate virtual environmen
   source venv/bin/activate # macOS or Linux
   # Or
   venv\Scripts\activate # Windows
   ```

- **Install Dependencies:**

   ```
   pip install -r requirements.txt
   ```

---

### Configuration

Copy `sample_settings.py` to `settings.py` and update the configurations accordingly.

---

## Running the Development Server

- **Migrate the Database:**

   ```
   python manage.py migrate
   ```

- **Run the Development Server:**

   ```
   python manage.py runserver
   ```

Access the website on `http://127.0.0.1:8000/`

---

## Deployment

Please refer to Django's official documentation for deployment best practices: [Deploying Django](https://docs.djangoproject.com/en/3.2/howto/deployment/).

---

## Authors and acknowledgment


## License

This project is licensed under the MIT License.

