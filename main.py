from typing import List
from fastapi import FastAPI
from API import schemaProjects 
from fastapi import HTTPException

app = FastAPI(
    title="Leen Al Harash - Portfolio API",
    description="Public API showcasing projects, skills, and contact info for portfolio purposes.",    version="1.0.0",
    docs_url="/swagger",
    redoc_url=None
)


@app.get("/", tags=["Default"])
def root():
    return {
        "message": "Portfolio API is running",
        "docs": "/swagger"
    }


@app.get("/api/health", tags=["System status"])
def health():
    return {
        "status": "ok",
        "service": "portfolio-api",
        "version": "1.0.0"
    }


@app.get("/api/projects", response_model=List[schemaProjects.Project], tags=["Portfolio projects"])
def projects():
    return [
        {
            "id": 1,
            "name": "Afterglam",
            "category": "Backend API",
            "tech": ["Python", "SQL", "FastAPI", "Swagger"],
            "description": "Secure backend API managing users, cosmetic products, and housing data with authentication, admin-only access, and advanced filtering.",
        },
        {
            "id": 2,
            "name": "Kaypic",
            "category": "Web Platform",
            "tech": ["ASP.NET", "C#", "JavaScript", "SignalR", "Swagger"],
            "description": "Community and sports platform featuring role-based authentication, real-time interactions, file sharing, and live updates.",
        },
        {
            "id": 3,
            "name": "Shatter Click",
            "category": "Game",
            "tech": ["Python", "Pygame"],
            "description": "Interactive mini-game where clicking triggers glass-breaking sound effects, animated cracks, and dynamic background color changes.",
        },
        {
            "id": 4,
            "name": "Hotel Res",
            "category": "Mobile Application",
            "tech": ["Kotlin", "Android SDK", "REST API", "JSON"],
            "description": "Android app for browsing and managing hotel reservations with live API data, loading states, and clean architecture.",
        },
        {
            "id": 5,
            "name": "Green Pulse",
            "category": "Web Application",
            "tech": ["Angular", "Spring Boot", "TypeScript", "REST API", "HTML", "CSS"],
            "description": "Transactional website providing agricultural products and real-time market data through a modern web interface.",
        },
        {
            "id": 6,
            "name": "Cowboy Hero 2D",
            "category": "Game",
            "tech": ["Unity", "C#"],
            "description": "2D desert-themed game featuring obstacles and level progression, with an extended experience combining 2D and 3D gameplay.",
        },
        {
            "id": 7,
            "name": "Snake",
            "category": "Web Game",
            "tech": ["HTML", "CSS", "JavaScript"],
            "description": "Classic snake game where the player grows the snake by collecting apples while avoiding self-collision.",
        },
        {
            "id": 8,
            "name": "Tic Tac Toe",
            "category": "Mobile Game",
            "tech": ["Kotlin"],
            "description": "Classic Tic Tac Toe game with an AI opponent and multilingual support (English, French, Spanish).",
        },
        {
            "id": 9,
            "name": "Portfolio",
            "category": "Website",
            "tech": ["HTML", "CSS", "JavaScript", "Swiper"],
            "description": "Responsive bilingual portfolio website showcasing projects, skills, and experience with smooth animations.",
        },
        {
            "id": 10,
            "name": "Music Library",
            "category": "Mobile Application",
            "tech": ["Kotlin"],
            "description": "Android music library app supporting English and French, allowing users to add, edit, delete, and search songs.",
        },
        {
            "id": 11,
            "name": "Portfolio API",
            "category": "Backend API",
            "tech": ["Python", "FastAPI", "Pydantic", "Swagger", "Uvicorn"],
            "description": "Simple portfolio REST API demonstrating FastAPI structure, Pydantic schemas, and Swagger/OpenAPI documentation."
        }
    ]


@app.get("/api/projects/{project_id}", response_model=schemaProjects.Project, tags=["Projects by id"])
def get_project_by_id(project_id: int):
    all_projects = projects()
    for project in all_projects:
        if project["id"] == project_id:
            return project
    raise HTTPException(status_code=404, detail="This project does not exist")


@app.get("/api/skills", tags=["Technical Skills"])
def skills():
    return {
        "frontend": ["HTML", "CSS", "JavaScript", "Angular", "TypeScript"],
        "backend": ["ASP.NET Core", "Spring Boot", "API INTEGRATION", "PHP", ],
        "programming": ["Kotlin", "JFX", "SQL", "Python", "JavaEE", "JavaSE", "C#"],
        "devops&tools": ["Git", "Docker", "Linux", "CI/CD Pipeline"],
        "others": ["OOP", "IoT", "Unity"]
    }


@app.get("/api/contact", tags=["Contact Information"])
def contact():
    return {
        "Email": "leen.zh.2004@gmail.com",
        "Github": "https://github.com/LeenAlHarash",
        "Linkedin": "https://www.linkedin.com/in/leen-al-harash-6134a0304/",
        "Discord": "https://discordid.netlify.app/?id=1077390981688729702"
    }
