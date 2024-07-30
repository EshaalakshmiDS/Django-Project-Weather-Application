# Weather App

This is a Weather Application that utilizes Django as the backend framework. Django provides a clean, pragmatic design and allows for rapid development. The app fetches real-time weather data for any city and displays the current weather conditions, including temperature, humidity, and weather description.

## Features

- **Real-time Weather Data**: Get current weather data for any city around the world.
- **Coordinates**: Displays the coordinates of the place.
- **User-Friendly Interface**: Simple and intuitive UI for displaying weather information.
- **Responsive Design**: Optimized for different screen sizes, ensuring a great experience on mobile and desktop devices.

## Tech Stack

- **Backend**: Django
- **Frontend**: HTML
- **APIs**: OpenWeatherMap API 

## Installation

### Prerequisites

- Python 3.x
- Django 4.x
- A valid API key from a weather data provider (e.g., OpenWeatherMap)

### Setup

1. **Clone the repository:**
 
git https://github.com/EshaalakshmiDS/Django-Project-Weather-Application.git
cd weather-app

2. **Create a virtual environment and activate it:**

python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

3. **Install the required packages:**
   
pip install -r requirements.txt

4.**Set up the environment variables:**

WEATHER_API_KEY=your_api_key

5. **Run migrations and start the development server:**
python manage.py migrate
python manage.py runserver

The app will be accessible at http://127.0.0.1:8000/.

### Project Directory

weather/
│
├── main/               # Main project directory <br>
│   ├── settings.py            # Django settings <br>
│   ├── urls.py                # URL routing <br>
│   ├── wsgi.py                # WSGI configuration <br>
│   ├── ... <br>
│ <br>
├── weather/                   # Main app directory <br>
│   ├── models.py              # Models for the app <br>
│   ├── views.py               # Views handling the app logic <br>
│   ├── urls.py                # URL routing for the app <br>
│   ├── templates/             # HTML templates <br>
│   ├── static/                # Static files (CSS, JS, images) <br>
│   ├── ... <br>
│ <br>
├── manage.py                  # Django management script <br>
├── requirements.txt           # Python dependencies <br>






