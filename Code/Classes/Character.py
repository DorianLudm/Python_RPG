import random
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from User import User

import sys
sys.path.append("..")
from ORM_connector import session, Base

class Character(Base):
    __tablename__ = 'characters'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    profession = Column(String)
    skill_points = relationship('SkillPoints', uselist=False, back_populates='character')

    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates='characters')
    
    def __init__(self, prof = "None", skill_points = [0 for i in range(7)]):
        self.skill_points = dict()
        self.initialize_skill_points(skill_points)
        self.prof = prof
        self.name = "NotYetNamed"

    def initialize_skill_points(self, skill_points):
        Character.random_spliter(skill_points, 10)
        self.skill_points["strength"] = skill_points[0]
        self.skill_points["dexterity"] = skill_points[1]
        self.skill_points["defense"] = skill_points[2]
        self.skill_points["magic"] = skill_points[3]
        self.skill_points["holiness"] = skill_points[4]
        self.skill_points["charisma"] = skill_points[5]
        self.skill_points["speed"] = skill_points[6]

    def add_skill_points(self, skill_points):
        self.skill_points["strength"] += skill_points[0]
        self.skill_points["dexterity"] += skill_points[1]
        self.skill_points["defense"] += skill_points[2]
        self.skill_points["magic"] += skill_points[3]
        self.skill_points["holiness"] += skill_points[4]
        self.skill_points["charisma"] += skill_points[5]
        self.skill_points["speed"] += skill_points[6]
        
    def random_spliter(stats, points_to_give):
        while points_to_give > 0:
            stats[random.randint(0, len(stats)-1)] += 1
            points_to_give -= 1
    
    def to_dict(self):
        return {"prof": self.prof, "skill_points": self.skill_points}
    
class Arbalist(Character):
    def __init__(self):
        super().__init__("Arbalist", [6, 9, 3, 3, 0, 1, 3])

class Bard(Character):
    def __init__(self):
        super().__init__("Bard", [4, 3, 1, 5, 5, 2, 4])

class Dragoon(Character):
    def __init__(self):
        super().__init__("Dragoon", [12, 2, 4, 2, 2, 2, 1])

class Guardian(Character):
    def __init__(self):
        super().__init__("Guardian", [4, 0, 10, 1, 4, 6, 0])

class Seraph(Character):
    def __init__(self):
        super().__init__("Seraph", [2, 2, 2, 7, 7, 4, 1])

class Slaughterer(Character):
    def __init__(self):
        super().__init__("Slaughterer", [7, 5, 1, 4, 0, 3, 5])

class Spellcaster(Character):
    def __init__(self):
        super().__init__("Spellcaster", [3, 5, 1, 9, 2, 1, 4])
        
class SkillPoints(Base):
    __tablename__ = 'skill_points'

    id = Column(Integer, primary_key=True)
    base_strength = Column(Integer)
    base_dexterity = Column(Integer)
    base_defense = Column(Integer)
    base_magic = Column(Integer)
    base_holiness = Column(Integer)
    base_charisma = Column(Integer)
    base_speed = Column(Integer)

    bonus_strength = Column(Integer)
    bonus_dexterity = Column(Integer)
    bonus_defense = Column(Integer)
    bonus_magic = Column(Integer)
    bonus_holiness = Column(Integer)
    bonus_charisma = Column(Integer)
    bonus_speed = Column(Integer)

    character_id = Column(Integer, ForeignKey('characters.id'))
    character = relationship('Character', back_populates='skill_points')

    @property
    def total_strength(self):
        return self.base_strength + self.bonus_strength
    
    @property
    def total_dexterity(self):
        return self.base_dexterity + self.bonus_dexterity
    
    @property
    def total_defense(self):
        return self.base_defense + self.bonus_defense
    
    @property
    def total_magic(self):
        return self.base_magic + self.bonus_magic
    
    @property
    def total_holiness(self):
        return self.base_holiness + self.bonus_holiness
    
    @property
    def total_charisma(self):
        return self.base_charisma + self.bonus_charisma
    
    @property
    def total_speed(self):
        return self.base_speed + self.bonus_speed
    
    def __init__(self, base_sp):
        self.base_strength = base_sp[0]
        self.base_dexterity = base_sp[1]
        self.base_defense = base_sp[2]
        self.base_magic = base_sp[3]
        self.base_holiness = base_sp[4]
        self.base_charisma = base_sp[5]
        self.base_speed = base_sp[6]

        self.bonus_strength = 0
        self.bonus_dexterity = 0
        self.bonus_defense = 0
        self.bonus_magic = 0
        self.bonus_holiness = 0
        self.bonus_charisma = 0
        self.bonus_speed = 0