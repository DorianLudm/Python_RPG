import random

class Character:
    
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