# 🚀 Modern Blog - Full Stack Blogging Platform

> **Developed with AI Assistance** 🤖 + **Human Expertise** 👨‍💻

A modern blogging web application built with FastAPI and cutting-edge technologies, developed through human-AI collaboration.

## 🌐 Live Application
**🔗 Live URL:** [https://modern-blog-tkzl.onrender.com/](https://modern-blog-tkzl.onrender.com/)
**📚 API Documentation:** [https://modern-blog-tkzl.onrender.com/docs](https://modern-blog-tkzl.onrender.com/docs)

## 🛠 Technology Stack
**Backend:** Python 3.11, FastAPI 0.100.0, SQLAlchemy 1.4.46, PostgreSQL, Uvicorn 0.23.2
**Frontend:** HTML5, CSS3, JavaScript, Modern UI/UX
**Security:** Werkzeug 2.3.7, BCrypt, CORS
**Deployment:** Render.com, GitHub, PostgreSQL

## ✨ Key Features
**🔐 Authentication:** Secure user registration, login, profile management
**📝 Content Management:** Full CRUD operations for posts, rich editor, post preview
**📊 Dashboard & Analytics:** User statistics, activity metrics, most active user tracking
**🎨 User Experience:** Responsive design, real-time notifications, search functionality

## 🏗 Project Architecture

modern-blog/
├── main.py # FastAPI application
├── database.py # Database configuration
├── models/ # SQLAlchemy models & schemas
├── templates/ # HTML templates
├── static/ # CSS, JS, assets
├── requirements.txt # Dependencies
├── build.sh # Render deployment
└── runtime.txt # Python version


## 🚀 Development Journey
**AI-Human Collaboration:** This project was developed through iterative AI assistance combined with human oversight for architecture decisions, code review, and deployment.

**Development Milestones:**
1. Architecture design and technology selection
2. FastAPI backend with SQLAlchemy ORM
3. Database modeling (User and Post entities)
4. Authentication system implementation
5. Frontend integration with responsive design
6. Render.com deployment configuration

## 📦 API Endpoints
**Authentication:**
- POST /api/auth/register - User registration
- POST /api/auth/login - User login
- GET /api/auth/me - Get current user
- PUT /api/auth/profile - Update user profile

**Post Management:**
- GET /api/posts - Get all posts
- POST /api/posts - Create new post
- GET /api/posts/my-posts - Get user's posts
- GET /api/posts/{id} - Get specific post
- PUT /api/posts/{id} - Update post
- DELETE /api/posts/{id} - Delete post

**Analytics:**
- GET /api/dashboard/stats - Platform statistics
- GET /api/users/{id}/stats - User analytics

- 🌍 Deployment
Render.com Configuration:

Auto-deploy from GitHub main branch

Managed PostgreSQL database

Python 3.11 runtime

Build Command: ./build.sh

Start Command: python main.py

🤖 AI Development Insights
AI Contributions: Code generation, debugging, dependency management, optimization, documentation
Human Oversight: Architecture decisions, security implementations, deployment strategy, code quality

📈 Performance Features
⚡ FastAPI for high-performance async operations

🗃️ SQLAlchemy for efficient database operations

🔒 Werkzeug Security for password hashing

🌐 CORS Enabled for cross-origin requests

📱 Responsive Design for all devices

👨‍💻 Developer  
**Marcelo**  
[View GitHub Profile](https://github.com/MarceloAdan73)

"This project showcases how AI can accelerate development while maintaining code quality and architectural integrity."

⭐ Star this repo if you found it helpful!

🚀 Live Demo | 📚 API Docs


## ��� Screenshot

![Modern Blog Screenshot](static/images/screenshot.png)

> *Main dashboard showing posts and user interface*


## ��� Application Screenshot

![Modern Blog Application](static/images/screenshot.png)

> *Modern Blog Platform - Main Interface*
