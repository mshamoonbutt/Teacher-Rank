# Teacher Rank

A web application that allows students to rate and review their teachers, helping them make informed decisions about their courses.

## Features

- User Authentication (Email/Password and Google Sign-in)
- Teacher Management and Ratings
- Course Management
- Review System
- Department and Course Filtering
- Admin Panel
- Responsive Design

## Tech Stack

### Frontend

- HTML, CSS, JavaScript
- Bootstrap
- Firebase (Authentication)

### Backend

- FastAPI
- SQLAlchemy
- Alembic (migrations)
- SQLite/PostgreSQL
- Firebase Admin SDK

## Setup Instructions

### Backend Setup

1. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:

```bash
cd backend
pip install -r requirements.txt
```

3. Set up environment variables:
   Create a `.env` file in the backend directory with the following variables:

```
DATABASE_URL=your_database_url
FIREBASE_CREDENTIALS=path_to_firebase_credentials.json
SECRET_KEY=your_secret_key
```

4. Run database migrations:

```bash
alembic upgrade head
```

5. Run the development server:

```bash
uvicorn app.main:app --reload
```

### Frontend Setup

1. Install dependencies:

```bash
cd frontend
npm install
```

2. Set up environment variables:
   Create a `.env` file in the frontend directory with your Firebase configuration.

3. Run the development server:

```bash
npm start
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License.
