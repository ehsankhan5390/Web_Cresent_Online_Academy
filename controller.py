import os
import sys
import json
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn

app = FastAPI()

# 🌐 www ڈومین کو مین ڈومین پر خودکار ری ڈائریکٹ کرنے کا مڈل ویئر
@app.middleware("http")
async def redirect_www(request: Request, call_next):
    host = request.headers.get("host", "")
    if host.startswith("www."):
        new_url = str(request.url).replace("//www.", "//", 1)
        return RedirectResponse(url=new_url, status_code=301)
    return await call_next(request)

# 📂 Static ڈائریکٹری
os.makedirs("static", exist_ok=True)
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

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
            "page": "home",
            "courses": courses,
            "seo_title": "Crescent Online Academy - Learn Quran & Islamic Studies",
            "seo_desc": "Online Quran Classes with Tajweed for kids and adults worldwide."
        }
    )

# 📚 اکیڈمک ایجوکیشن پیج راؤٹ
@app.get("/academic", response_class=HTMLResponse)
async def academic(request: Request):
    courses = get_dynamic_courses()
    return templates.TemplateResponse(
        request=request, 
        name="index.html",
        context={
            "page": "academic",
            "courses": courses,
            "seo_title": "Academic Education - Crescent Online Academy",
            "seo_desc": "Comprehensive Tuition & Modern Curriculum Support for All Grades."
        }
    )

# 🎈 پرائمری ایجوکیشن پیج راؤٹ (Grades 1-5)
@app.get("/academic/primary", response_class=HTMLResponse)
async def academic_primary(request: Request):
    courses = get_dynamic_courses()
    return templates.TemplateResponse(
        request=request, 
        name="index.html",
        context={
            "page": "academic_primary",
            "courses": courses,
            "seo_title": "Primary Education (Grades 1-5) - Crescent Online Academy",
            "seo_desc": "Interactive 1-on-1 Online Learning for Grades 1 to 5."
        }
    )

# 📘 مڈل سکول پیج راؤٹ (Grades 6-8)
@app.get("/academic/middle", response_class=HTMLResponse)
async def academic_middle(request: Request):
    courses = get_dynamic_courses()
    return templates.TemplateResponse(
        request=request, 
        name="index.html",
        context={
            "page": "academic_middle",
            "courses": courses,
            "seo_title": "Middle School (Grades 6-8) - Crescent Online Academy",
            "seo_desc": "Comprehensive 1-on-1 Academic Support for Grades 6 to 8."
        }
    )

# 🎓 ہائی سکول و بورڈ ایگزام پیج راؤٹ (Grades 9-12 / O & A Levels)
@app.get("/academic/high_school", response_class=HTMLResponse)
async def academic_high_school(request: Request):
    courses = get_dynamic_courses()
    return templates.TemplateResponse(
        request=request, 
        name="index.html",
        context={
            "page": "academic_high_school",
            "courses": courses,
            "seo_title": "High School & Board Exams - Crescent Online Academy",
            "seo_desc": "Advanced Prep for Grades 9-12, O & A Levels & Board Exams."
        }
    )

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 7860))
    uvicorn.run(app, host="0.0.0.0", port=port)