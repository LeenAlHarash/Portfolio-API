from fastapi import FastAPI

app = FastAPI(
    title="Leen Al Harash – Portfolio API",
    description="Simple API showcasing backend structure and Swagger documentation",
    version="1.0.0",
    docs_url="/swagger",
    redoc_url=None
)


@app.get("/")
def root():
    return {
        "message": "Portfolio API is running",
        "docs": "/swagger"
    }


@app.get("/api/health")
def health():
    return {
        "status": "ok",
        "service": "portfolio-api",
        "version": "2.0.0"
    }


@app.get("/api/projects")
def projects():
    return [
        {
            "id": 1,
            "name": "Afterglam",
            "type": "Backend API",
            "tech": ["Python", "SQL", "Swagger"],
            "description": "Secure backend API with authentication"
        }
    ]


@app.get("/api/skills")
def skills():
    return {
        "frontend": ["HTML", "CSS", "JavaScript", "Angular", "TypeScript"],
        "backend": ["Python", "ASP.NET", "Spring Boot", "Java", "PHP", ],
        "mobile": ["Kotlin"],
        "tools": ["Git", "Docker", "Swagger"]
    }


@app.get("/api/contact")
def contact():
    return {
        "Email:" "leen.zh.2004@gmail.com",
        "Github:" "https://github.com/LeenAlHarash",
        "Linkedin:" "https://www.linkedin.com/in/leen-al-harash-6134a0304/",
        "Discord:" "https://discordid.netlify.app/?id=1077390981688729702"
    }
