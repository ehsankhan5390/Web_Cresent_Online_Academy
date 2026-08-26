import os
import sys
import json
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn

app = FastAPI()

# 📂 Static اور Templates ڈائریکٹریز سیٹ کرنا
os.makedirs("static", exist_ok=True)
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory=[
    "templates",
    "templates/includes"
])

# 🛠️ ڈائنامک کورسز اسکین کرنے کا فنکشن
def get_dynamic_courses():
    courses_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "courses")
    courses_list = []
    
    if os.path.exists(courses_dir):
        for folder in sorted(os.listdir(courses_dir)):
            course_path = os.path.join(courses_dir, folder)
            config_path = os.path.join(course_path, "config.json")
            
            if os.path.isdir(course_path) and os.path.exists(config_path):
                try:
                    with open(config_path, "r", encoding="utf-8") as f:
                        cfg = json.load(f)
                        cfg["slug"] = folder
                        courses_list.append(cfg)
                except Exception as e:
                    print(f"Error reading config for {folder}: {e}")
                    
    return courses_list

# 🏠 ہوم پیج راؤٹ
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    courses = get_dynamic_courses()
    return templates.TemplateResponse(
        request=request, 
        name="index.html",
        context={
            "courses": courses,
            "seo_title": "Crescent Online Academy - Learn Quran & Islamic Studies",
            "seo_desc": "Online Quran Classes with Tajweed for kids and adults worldwide."
        }
    )

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 7860))
    uvicorn.run(app, host="0.0.0.0", port=port)