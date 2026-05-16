from sqlalchemy import Column, Integer, String, Numeric, BigInteger, ForeignKey
from sqlalchemy.orm import relationship
from dependencies.database import Base


class Planet(Base):
    __tablename__ = "Planets"
    
    planet_id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    planet_type_id = Column(Integer, ForeignKey("PlanetTypes.planet_type_id"), nullable=False)
    diameter_km = Column(Numeric(10, 2))
    mass_10e24kg = Column(Numeric(20, 4))
    gravity_ms2 = Column(Numeric(5, 2))
    distance_from_sun_km = Column(BigInteger)
    
    planet_type = relationship("PlanetType", back_populates="planets")
    moons = relationship("Moon", back_populates="planet")
    missions = relationship("Mission", secondary="PlanetMissions", back_populates="planets")
