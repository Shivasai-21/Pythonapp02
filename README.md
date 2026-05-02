📄 README.md (ready to copy)
markdown
# Realtime Chat Application

A realtime chat application built with **Flask**, **Socket.IO**, **MongoDB**, and **Nginx**.  
The app supports user registration, login, and chat messaging with persistent storage.



## 🚀 Features
- User registration and login (MongoDB backend)
- Realtime chat using Flask-SocketIO
- Message persistence in MongoDB
- Nginx reverse proxy for clean URLs
- Dockerized setup with `docker-compose`



## 📂 Project Structure
Pythonapp02/
├── app.py              # Flask app entrypoint
├── models.py           # MongoDB models (users, messages)
├── chat_routes.py      # Socket.IO event handlers
├── requirements.txt    # Python dependencies
├── docker-compose.yml  # Multi-container setup
├── Dockerfile          # Flask app container build
├── nginx.conf          # Nginx reverse proxy config
├── templates/          # HTML templates (index, login, register, chat)
└── static/             # CSS/JS assets



**Code**
## 🐳 Docker Setup

### Build & Run

docker-compose up -d --build


**Stop**
docker-compose down


🌐 **Access**
Nginx (recommended):  
http://<EC2-IP>/

Direct Flask (debugging):  
http://<EC2-IP>:3434/


🔧 **Environment**
Flask runs on port 5000 (proxied by Nginx on port 80)

MongoDB runs internally on port 27017

Nginx proxies requests to Flask and serves static files



📝 **Usage**
Visit /register to create a new account.

Log in via /login.

Start chatting in /chat.


⚠️ **Security Notes**
Passwords are currently stored in plain text.
For production, use bcrypt hashing in models.py.

Ensure port 80 is open in your EC2 security group.


📌 **Next Steps**
Add password hashing with bcrypt

Implement session management

Deploy with HTTPS using Let’s Encrypt
