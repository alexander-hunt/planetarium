from sqlalchemy import Column, Integer, String, Numeric, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from dependencies.database import Base


class Moon(Base):
    __tablename__ = "Moons"
    
    moon_id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    planet_id = Column(Integer, ForeignKey("Planets.planet_id"), nullable=False)
    diameter_km = Column(Numeric(10, 2))
    
    planet = relationship("Planet", back_populates="moons")
    
    __table_args__ = (
        UniqueConstraint("name", "planet_id", name="uq_moon_planet"),
    )
