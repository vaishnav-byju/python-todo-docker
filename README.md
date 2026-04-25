📝 Python Flask To-Do Application
A simple To-Do web application built with Python Flask, containerized using Docker, and orchestrated with Docker Compose. This project demonstrates DevOps workflows including containerization, deployment, and GitHub integration.

🚀 Features
Add, update, and delete tasks

Flask-based backend with Jinja2 templates

Lightweight SQLite database

Dockerized for easy deployment

Docker Compose for multi-container orchestration

📂 Project Structure
app.py → Main Flask application

requirements.txt → Python dependencies

Dockerfile → Docker image definition

docker-compose.yml → Multi-container setup

⚙️ Prerequisites
Python 3.9 or higher

Docker Desktop (with WSL2 enabled on Windows)

GitHub account for repository hosting

🛠️ Setup & Installation
Clone the repository from GitHub.

Install dependencies using pip install -r requirements.txt.

Run the app with python app.py.

Open your browser and go to http://localhost:5000.

🐳 Run with Docker
Build the Docker image using docker build -t flask-todo-app ..

Run the container with docker run -d -p 5000:5000 flask-todo-app.

Access the app at http://localhost:5000.

🔧 Run with Docker Compose
Start the app with docker-compose up --build -d.

Stop it with docker-compose down.

📸 Expected Output
Docker Desktop showing the running container

Browser displaying the To-Do app at http://localhost:5000

🧹 Cleanup
Stop and remove containers with docker-compose down.

Remove the image with docker rmi flask-todo-app.

📤 Submission Checklist
Project files (app.py, requirements.txt, Dockerfile, docker-compose.yml)

Screenshots: Docker Desktop running container, browser showing To-Do app

GitHub repository link

README.md (this file)

Optional: PDF report with labeled screenshots

👨‍💻 Author
Vaishnav Byju  
BCA Student, Marian College Kuttikkanam Autonomous
Internship Project – DevOps Workflow with Docker & GitHub
