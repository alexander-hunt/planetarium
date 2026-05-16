from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from dependencies.database import Base


class PlanetType(Base):
    __tablename__ = "PlanetTypes"
    
    planet_type_id = Column(Integer, primary_key=True)
    type_name = Column(String(50), unique=True, nullable=False)
    
    planets = relationship("Planet", back_populates="planet_type")
