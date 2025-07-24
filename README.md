# MovieMate

MovieMate is a modern movie recommendation web application built with Flask and MongoDB. It allows users to search for movies, get personalized recommendations, and manage their accounts with a beautiful, responsive UI.

## Features
- User registration, login, and account management
- Movie search powered by TMDb API
- Personalized movie recommendations based on user history
- Trending movies display
- Profile picture upload and update
- Flash messages for user feedback
- Responsive design with Bootstrap 5

## Tech Stack
- Python 3.12
- Flask
- MongoDB (via MongoEngine)
- Bootstrap 5
- TMDb API

## Setup Instructions
1. **Clone the repository:**
   ```bash
   git clone https://github.com/shishpal0666/MovieMate.git
   cd MovieMate
   ```
2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/Scripts/activate  # On Windows
   # or
   source venv/bin/activate      # On Mac/Linux
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Set up your `.env` file:**
   - Copy `.env.example` to `.env` and fill in your `SECRET_KEY`, `API_KEY` (TMDb), and `MONGO_DB` connection string.
5. **Run the app:**
   ```bash
   python run.py
   ```
6. **Access MovieMate:**
   - Open your browser and go to [http://127.0.0.1:5000](http://127.0.0.1:5000)

## Folder Structure
```
MovieMate/
├── app/
│   ├── __init__.py
│   ├── models/
│   ├── forms/
│   ├── routes/
│   ├── utils/
│   ├── static/
│   └── templates/
├── Datapreprocessing/
├── instance/
├── training/
├── requirements.txt
├── run.py
├── LICENSE
└── README.md
```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
