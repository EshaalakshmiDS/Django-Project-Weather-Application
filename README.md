# Weather Application

This is a Weather Application that utilizes Django as the backend framework. Django provides a clean, pragmatic design and allows for rapid development. The app fetches real-time weather data for any city and displays the current weather conditions, including temperature, humidity, and weather description.

## Features

- **Real-time Weather Data**: Get current weather data for any city around the world.
- **City Search**: Easily search for a city's weather using the search bar.
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

1. **Clone the repository**:

    ```bash
    git clone https://github.com/EshaalakshmiDS/Django-Project-Weather-Application.git
    cd weather-app
    ```

2. **Create a virtual environment and activate it**:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the environment variables:**

    ```bash
    WEATHER_API_KEY=your_api_key
    ```

5. **Run migrations and start the development server:**

    ```bash
    python manage.py migrate
    python manage.py runserver
    ```

The app will be accessible at http://127.0.0.1:8000/.

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/EshaalakshmiDS/Django-Project-Weather-Application.git

2. **Create and activate a virtual environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate 

3. **Install dependencies:**:

   ```bash
   pip install -r requirements.txt

4. **Apply migrations:**:

   ```bash
   python manage.py migrate
   
5. **Access the application:**:

   Open your browser and navigate to http://127.0.0.1:8000/

### Project Directory

weather/
│
├── weather/                   # Main project directory <br>
│   ├── settings.py            # Django settings <br>
│   ├── urls.py                # URL routing <br>
│   ├── wsgi.py                # WSGI configuration <br>
│   ├── ... <br>
│ <br>
├── main/                      # Main app directory <br>
│   ├── models.py              # Models for the app <br>
│   ├── views.py               # Views handling the app logic <br>
│   ├── urls.py                # URL routing for the app <br>
│   ├── templates/             # HTML templates <br>
│   ├── static/                # Static files (CSS, JS, images) <br>
│   ├── ... <br>
│ <br>
├── manage.py                  # Django management script <br>
├── requirements.txt           # Python dependencies <br>






