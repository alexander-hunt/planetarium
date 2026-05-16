from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from dependencies.database import Base


class Mission(Base):
    __tablename__ = "Missions"
    
    mission_id = Column(Integer, primary_key=True)
    mission_name = Column(String(100), unique=True, nullable=False)
    launch_year = Column(Integer)
    agency = Column(String(80))
    
    planets = relationship("Planet", secondary="PlanetMissions", back_populates="missions")
