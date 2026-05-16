DROP DATABASE IF EXISTS planetarium_db;
CREATE DATABASE planetarium_db;
USE planetarium_db;

CREATE TABLE PlanetTypes (
    planet_type_id INT AUTO_INCREMENT PRIMARY KEY,
    type_name VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE Planets (
    planet_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE,
    planet_type_id INT NOT NULL,
    diameter_km DECIMAL(10,2),
    mass_10e24kg DECIMAL(10,3),
    gravity_ms2 DECIMAL(5,2),
    distance_from_sun_km BIGINT,
    CONSTRAINT fk_planets_planet_types
        FOREIGN KEY (planet_type_id)
        REFERENCES PlanetTypes(planet_type_id)
);

CREATE TABLE Moons (
    moon_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(80) NOT NULL,
    planet_id INT NOT NULL,
    diameter_km DECIMAL(10,2),
    CONSTRAINT fk_moons_planets
        FOREIGN KEY (planet_id)
        REFERENCES Planets(planet_id),
    CONSTRAINT uq_moon_planet
        UNIQUE (name, planet_id)
);

CREATE TABLE Missions (
    mission_id INT AUTO_INCREMENT PRIMARY KEY,
    mission_name VARCHAR(100) NOT NULL UNIQUE,
    launch_year YEAR,
    agency VARCHAR(80)
);

CREATE TABLE PlanetMissions (
    planet_id INT NOT NULL,
    mission_id INT NOT NULL,
    PRIMARY KEY (planet_id, mission_id),
    CONSTRAINT fk_planet_missions_planets
        FOREIGN KEY (planet_id)
        REFERENCES Planets(planet_id),
    CONSTRAINT fk_planet_missions_missions
        FOREIGN KEY (mission_id)
        REFERENCES Missions(mission_id)
);

INSERT INTO PlanetTypes (type_name) VALUES
('Terrestrial'),
('Gas Giant'),
('Ice Giant'),
('Dwarf Planet');

INSERT INTO Planets
(name, planet_type_id, diameter_km, mass_10e24kg, gravity_ms2, distance_from_sun_km)
VALUES
('Mercury', 1, 4879.00, 0.330, 3.70, 57900000),
('Venus', 1, 12104.00, 4.870, 8.87, 108200000),
('Earth', 1, 12742.00, 5.972, 9.81, 149600000),
('Mars', 1, 6779.00, 0.642, 3.71, 227900000),
('Jupiter', 2, 139820.00, 1898.000, 24.79, 778500000),
('Saturn', 2, 116460.00, 568.000, 10.44, 1434000000),
('Uranus', 3, 50724.00, 86.800, 8.69, 2871000000),
('Neptune', 3, 49244.00, 102.000, 11.15, 4495000000),
('Pluto', 4, 2376.60, 0.013, 0.62, 5906000000);

INSERT INTO Moons (name, planet_id, diameter_km) VALUES
('Moon', 3, 3474.80),
('Phobos', 4, 22.40),
('Deimos', 4, 12.40),
('Io', 5, 3643.20),
('Europa', 5, 3121.60),
('Ganymede', 5, 5268.20),
('Callisto', 5, 4820.60),
('Titan', 6, 5149.50),
('Enceladus', 6, 504.20),
('Mimas', 6, 396.40),
('Titania', 7, 1576.80),
('Oberon', 7, 1522.80),
('Triton', 8, 2706.80),
('Charon', 9, 1212.00);

INSERT INTO Missions (mission_name, launch_year, agency) VALUES
('Mariner 10', 1973, 'NASA'),
('Viking 1', 1975, 'NASA'),
('Voyager 1', 1977, 'NASA'),
('Voyager 2', 1977, 'NASA'),
('Galileo', 1989, 'NASA'),
('Cassini-Huygens', 1997, 'NASA/ESA/ASI'),
('New Horizons', 2006, 'NASA'),
('Juno', 2011, 'NASA'),
('Mars Perseverance Rover', 2020, 'NASA');

INSERT INTO PlanetMissions (planet_id, mission_id) VALUES
(1, 1),
(2, 1),
(4, 2),
(5, 3),
(6, 3),
(5, 4),
(6, 4),
(7, 4),
(8, 4),
(5, 5),
(6, 6),
(9, 7),
(5, 8),
(4, 9);