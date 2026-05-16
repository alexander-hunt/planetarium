from sqlalchemy import Column, Integer, ForeignKey
from dependencies.database import Base


class PlanetMission(Base):
    __tablename__ = "PlanetMissions"
    
    planet_id = Column(Integer, ForeignKey("Planets.planet_id"), primary_key=True)
    mission_id = Column(Integer, ForeignKey("Missions.mission_id"), primary_key=True)
