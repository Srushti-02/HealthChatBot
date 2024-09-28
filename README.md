# HealthChatBot
This health chatbot web application provides users with health-related information and suggestions based on user input. The app includes a login and signup page, allowing users to create an account, and access the chatbot functionality. The application is built using Flask for the backend, Python for the core logic and HTML, CSS and JavaScript for the frontend. Docker is used to containerize the application for easy deployment.

## Table of Contents
1. Project Structure
2. Prerequisites
3. Installation
4. Usage
5. Docker Setup
6. File Structure
7. Contributing

## Project Structure
* app.py : Main flask application file that routes HTTP requests and controls the chatbot logic.
* templates/ : Contains all HTML, CSS and images.
* Dockerfile : Docker configuration to containerize the application.
* .dockerignore & .gitignore : Have file paths which need to be ignored.

## Prerequisites
Ensure you have the following installed:
* Python 3.x
* Docker
* Flask
* VS Code

## Installation
1. Clone the repository:
git clone [https://github.com/your-username/health-chatbot.git](https://github.com/Srushti-02/HealthChatBot.git)
cd HealthChatBot

2. Create a virtual environment and install dependencies:
python3 -m venv venv
source venv/bin/activate  # For Linux/macOS
venv\Scripts\activate     # For Windows

4. Run the application:
python app.py

## Docker Setup
To run the application inside a Docker container, follow these steps:

1. Build the Docker image:
docker build -t health-chatbot .

2. Run the Docker container:
docker run -d -p 5000:5000 health-chatbot

## File Structure

health-chatbot/
│
├── app.py              # Main Flask application
├── dockerfile          # Docker configuration file
├── templates/          # HTML templates
│   ├── login.html      # Login page
│   ├── signup.html     # Signup page
│   ├── liverchatbot.html     # Liver chatbot page
│   ├── kidneychatbot.html     # Kidney chatbot page
│   ├── diabeteschatbot.html     # Diabetes chatbot page
│   └── index.html    # Main page
│
├── venv/               # Virtual environment files
├── .dockerignore               
├── .gitignore              
├── liver_disease_model.h5    # weights for model to predict
├── users.db               # Database
└── README.md           # Project README file

## Contributing
Constributions are welcome! Please follow the steps below to contribute:
1. Fork the repository.
2. Create a new branch (git checkout -b feature-branch).
3. Commit your changes (git commit -m "Added a new feature").
4. Push to the branch (git push origin feature-branch).
5. Open a pull request.
