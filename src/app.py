"""
High School Management System API

A super simple FastAPI application that allows students to view and sign up
for extracurricular activities at Mergington High School.
"""

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
import os
from pathlib import Path

app = FastAPI(title="Mergington High School API",
              description="API for viewing and signing up for extracurricular activities")

# Mount the static files directory
current_dir = Path(__file__).parent
app.mount("/static", StaticFiles(directory=os.path.join(Path(__file__).parent,
          "static")), name="static")

# In-memory activity database
activities = {
    "Chess Club": {
        "description": "Learn strategies and compete in chess tournaments",
        "schedule": "Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 12,
        "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
    },
    "Programming Class": {
        "description": "Learn programming fundamentals and build software projects",
        "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
        "max_participants": 20,
        "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
    },
    "Gym Class": {
        "description": "Physical education and sports activities",
        "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
        "max_participants": 30,
        "participants": ["john@mergington.edu", "olivia@mergington.edu"]
    },
    # Sports related activities
    "Soccer Team": {
        "description": "Join the school soccer team and compete in matches",
        "schedule": "Wednesdays, 4:00 PM - 6:00 PM",
        "max_participants": 22,
        "participants": ["lucas@mergington.edu", "mia@mergington.edu"]
    },
    "Basketball Club": {
        "description": "Practice basketball skills and play friendly games",
        "schedule": "Mondays, 5:00 PM - 6:30 PM",
        "max_participants": 15,
        "participants": ["liam@mergington.edu", "ava@mergington.edu"]
    },
    "Track and Field": {
        "description": "Train for running, jumping, and throwing events",
        "schedule": "Tuesdays, 4:00 PM - 5:30 PM",
        "max_participants": 25,
        "participants": ["sam@mergington.edu", "ella@mergington.edu"]
    },
    "Swimming Team": {
        "description": "Practice swimming techniques and compete in meets",
        "schedule": "Thursdays, 5:00 PM - 6:30 PM",
        "max_participants": 20,
        "participants": ["jake@mergington.edu", "lily@mergington.edu"]
    },
    # Artistic activities
    "Art Workshop": {
        "description": "Explore painting, drawing, and sculpture techniques",
        "schedule": "Thursdays, 3:30 PM - 5:00 PM",
        "max_participants": 18,
        "participants": ["noah@mergington.edu", "isabella@mergington.edu"]
    },
    "Drama Club": {
        "description": "Act, direct, and produce school plays and performances",
        "schedule": "Tuesdays, 4:00 PM - 5:30 PM",
        "max_participants": 20,
        "participants": ["ethan@mergington.edu", "charlotte@mergington.edu"]
    },
    "Photography Club": {
        "description": "Learn photography skills and participate in photo exhibitions",
        "schedule": "Wednesdays, 3:30 PM - 5:00 PM",
        "max_participants": 15,
        "participants": ["oliver@mergington.edu", "amelia@mergington.edu"]
    },
    "Music Ensemble": {
        "description": "Perform in a group and learn various musical instruments",
        "schedule": "Mondays, 4:00 PM - 5:30 PM",
        "max_participants": 20,
        "participants": ["jack@mergington.edu", "emily@mergington.edu"]
    },
    # Intellectual activities
    "Math Olympiad": {
        "description": "Prepare for math competitions and solve challenging problems",
        "schedule": "Fridays, 2:00 PM - 3:30 PM",
        "max_participants": 16,
        "participants": ["alex@mergington.edu", "grace@mergington.edu"]
    },
    "Science Club": {
        "description": "Conduct experiments and explore scientific concepts",
        "schedule": "Wednesdays, 3:30 PM - 5:00 PM",
        "max_participants": 20,
        "participants": ["ben@mergington.edu", "zoe@mergington.edu"]
    },
    "Debate Team": {
        "description": "Develop public speaking and argumentation skills",
        "schedule": "Thursdays, 4:00 PM - 5:30 PM",
        "max_participants": 12,
        "participants": ["lucy@mergington.edu", "henry@mergington.edu"]
    },
    "Robotics Club": {
        "description": "Design, build, and program robots for competitions",
        "schedule": "Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 15,
        "participants": ["leo@mergington.edu", "mia@mergington.edu"]
    }
}


@app.get("/")
def root():
    return RedirectResponse(url="/static/index.html")


@app.get("/activities")
def get_activities():
    return activities


@app.post("/activities/{activity_name}/signup")
def signup_for_activity(activity_name: str, email: str):
    """Sign up a student for an activity"""
    # Validate activity exists
    if activity_name not in activities:
        raise HTTPException(status_code=404, detail="Activity not found")

    # Get the specific activity
    activity = activities[activity_name]

    # Validate student is not already signed up 
    if email in activity["participants"]:
        raise HTTPException(status_code=400, detail="Already signed up for this activity")
    
    # Add student
    activity["participants"].append(email)
    return {"message": f"Signed up {email} for {activity_name}"}
