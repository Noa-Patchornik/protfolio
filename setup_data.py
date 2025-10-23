import json
import os

# 📁 Define the directory where JSON files will be saved
output_dir = "assets/user_data"

# 🛠️ Create the directory if it doesn't already exist
os.makedirs(output_dir, exist_ok=True)

# 👤 User basic info including name, role, bio, and skills
user = {
    "name": "Noa Patchornik",
    "role": "Back-End Developer | Software Engineer",
    "bio": (
        "Passionate about backend development, scalable architecture, and clean, maintainable code. "
        "Currently expanding my skills through self-learning and participating in collaborative projects "
        "within the TCP community, working with multidisciplinary teams to build real-world software solutions."
    ),
    "skills": [
        "Python", "FastAPI", "Java", "C#", "C++", "Node.js", "React", "Vue", "SQL",
        "MongoDB", "Docker", "GCP", "Azure DevOps", "Git", "REST APIs", "OOP", "Design Patterns"
    ]
}

# 🌐 Social media and professional links
social_links = {
    "email-id": "noap2580@gmail.com",
    "linkedin": "https://www.linkedin.com/in/noa-patchornik/",
    "github": "https://github.com/Noa-Patchornik"
}

# 💼 Projects
projects = [
    {
        "name": "Recipes Website",
        "description": (
            "A full-stack recipe-sharing platform built with Vue 3, Node.js, and MySQL. "
            "Includes Spoonacular API integration, authentication, favorites, dynamic search, and responsive SPA design."
        ),
        "link": {
            "github": "https://github.com/Noa-Patchornik/Recipes-Website",
            "live_demo": ""
        },
        "tools": ["Vue 3", "Node.js", "MySQL", "BootstrapVue", "Swagger", "REST API"],
        "image": "https://img.freepik.com/free-photo/online-recipe-book-food-blogging_53876-138091.jpg"
    },
    {
        "name": "Task Management App",
        "description": (
            "A full-stack task management system for creating, editing, filtering, and tracking tasks. "
            "Built with React (Vite) and FastAPI + MongoDB, fully containerized with Docker Compose."
        ),
        "link": {
            "github": "https://github.com/Noa-Patchornik/Task-Manager",
            "live_demo": ""
        },
        "tools": ["React", "FastAPI", "Python", "MongoDB", "Docker"],
        "image": "https://cdn-icons-png.flaticon.com/512/1032/1032432.png"
    },
    {
        "name": "Super-Lee HR System",
        "description": (
            "A multi-layer human resources management system built in Java. "
            "Implements CRUD operations, payroll management, contracts, and shift planning."
        ),
        "link": {
            "github": "https://github.com/Noa-Patchornik/Super-Lee",
            "live_demo": ""
        },
        "tools": ["Java", "SQLite", "OOP", "Design Patterns"],
        "image": "https://cdn-icons-png.flaticon.com/512/189/189664.png"
    },
    {
        "name": "Super Mario Maze Game",
        "description": (
            "An interactive Super Mario–themed maze game built with JavaFX and MVVM architecture. "
            "Implements DFS, BFS, and Best-First algorithms for maze generation and solving."
        ),
        "link": {
            "github": "https://github.com/Noa-Patchornik/SuperMario-Maze",
            "live_demo": ""
        },
        "tools": ["Java", "JavaFX", "MVVM", "Algorithms", "Client-Server"],
        "image": "https://cdn-icons-png.flaticon.com/512/3039/3039391.png"
    },
    {
        "name": "Network Speed Test",
        "description": (
            "A Python-based client-server app that simulates TCP and UDP protocols to measure transfer speed, latency, and packet loss. "
            "Ranked 1st in course evaluation."
        ),
        "link": {
            "github": "https://github.com/Noa-Patchornik/Network-speed-CS",
            "live_demo": ""
        },
        "tools": ["Python", "Sockets", "Networking", "CLI"],
        "image": "https://cdn-icons-png.flaticon.com/512/1828/1828884.png"
    },
    {
        "name": "Frida Kahlo Landing Page",
        "description": (
            "A clean, responsive landing page celebrating Frida Kahlo’s art, built with HTML, CSS, and vanilla JavaScript. "
            "Focused on design, accessibility, and storytelling."
        ),
        "link": {
            "github": "https://github.com/Noa-Patchornik/Frida-Kahlo-Website",
            "live_demo": ""
        },
        "tools": ["HTML", "CSS", "JavaScript"],
        "image": "https://cdn-icons-png.flaticon.com/512/616/616408.png"
    },
    {
        "name": "Pacman SpaceShoot Game",
        "description": (
            "A browser-based arcade game combining Pacman gameplay with space shooter mechanics. "
            "Includes user registration, shooting mechanics, and dynamic scoring."
        ),
        "link": {
            "github": "https://github.com/Noa-Patchornik/Pacman-Spaceshoot-game",
            "live_demo": ""
        },
        "tools": ["HTML", "CSS", "JavaScript"],
        "image": "https://cdn-icons-png.flaticon.com/512/185/185211.png"
    }
]

# 🎓 Certifications
certifications = [
    {
        "title": "B.Sc. in Software & Information Systems Engineering",
        "issuer": "Ben-Gurion University of the Negev",
        "year": "2024",
        "link": ""
    }
]

# 🎓 Education
education = [
    {
        "degree": "B.Sc. in Software & Information Systems Engineering",
        "institution": "Ben-Gurion University of the Negev",
        "year": "2020 - 2024",
        "details": "Focused on software engineering, data structures, backend development, and system design."
    }
]

# 🎯 Hobbies and interests
hobbies = [
    {
        "title": "Learning New Technologies",
        "publication": "Constantly exploring emerging tools and frameworks to improve development workflows.",
        "link": ""
    },
    {
        "title": "Open Source Contribution",
        "publication": "Contributing to GitHub projects and developer communities.",
        "link": "https://github.com/Noa-Patchornik"
    },
    {
        "title": "Creative Writing & Reading",
        "publication": "Enjoy reading tech blogs, biographies, and writing about problem-solving approaches.",
        "link": ""
    }
]

# 📄 Research papers (empty for now)
research_papers = []

# 💾 Utility function to save any Python dictionary/list as a formatted JSON file
def save_json(data, filename):
    with open(os.path.join(output_dir, filename), "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
    print(f"✅ {filename} saved!")

# 🚀 Save all JSON files
save_json(user, "user.json")
save_json(social_links, "social_links.json")
save_json(projects, "projects.json")
save_json(certifications, "certifications.json")
save_json(education, "education.json")
save_json(hobbies, "hobbies.json")
save_json(research_papers, "research_papers.json")
