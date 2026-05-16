from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from dependencies.database import SessionLocal
from models import PlanetType, Planet, Moon, Mission, PlanetMission

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/health")
def root():
    return {"message": "Health check passed"}


@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}


@app.get("/tables")
def get_all_tables(db: Session = Depends(get_db)):
    """
    Returns all data from all planetarium tables as JSON
    """
    try:
        planet_types = db.query(PlanetType).all()
        planets = db.query(Planet).all()
        moons = db.query(Moon).all()
        missions = db.query(Mission).all()
        planet_missions = db.query(PlanetMission).all()
        
        return {
            "planet_types": [
                {
                    "planet_type_id": pt.planet_type_id,
                    "type_name": pt.type_name
                }
                for pt in planet_types
            ],
            "planets": [
                {
                    "planet_id": p.planet_id,
                    "name": p.name,
                    "planet_type_id": p.planet_type_id,
                    "diameter_km": float(p.diameter_km) if p.diameter_km else None,
                    "mass_10e24kg": float(p.mass_10e24kg) if p.mass_10e24kg else None,
                    "gravity_ms2": float(p.gravity_ms2) if p.gravity_ms2 else None,
                    "distance_from_sun_km": p.distance_from_sun_km
                }
                for p in planets
            ],
            "moons": [
                {
                    "moon_id": m.moon_id,
                    "name": m.name,
                    "planet_id": m.planet_id,
                    "diameter_km": float(m.diameter_km) if m.diameter_km else None
                }
                for m in moons
            ],
            "missions": [
                {
                    "mission_id": m.mission_id,
                    "mission_name": m.mission_name,
                    "launch_year": str(m.launch_year) if m.launch_year else None,
                    "agency": m.agency
                }
                for m in missions
            ],
            "planet_missions": [
                {
                    "planet_id": pm.planet_id,
                    "mission_id": pm.mission_id
                }
                for pm in planet_missions
            ]
        }
    except SQLAlchemyError as e:
        return {
            "error": "Database error",
            "details": str(e)
        }