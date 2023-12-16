import random

class Character:
    
    def __init__(self, prof = "None", skill_points = [0 for i in range(7)]):
        self.skill_points = dict()
        self.initialize_skill_points(skill_points)
        self.prof = prof

    def initialize_skill_points(self, skill_points):
        Character.random_spliter(skill_points, 10)
        self.skill_points["strength"] = skill_points[0]
        self.skill_points["dexterity"] = skill_points[1]
        self.skill_points["defense"] = skill_points[2]
        self.skill_points["magic"] = skill_points[3]
        self.skill_points["holiness"] = skill_points[4]
        self.skill_points["charisma"] = skill_points[5]
        self.skill_points["speed"] = skill_points[6]
        
    def random_spliter(stats, points_to_give):
        while points_to_give > 0:
            stats[random.randint(0, len(stats)-1)] += 1
            points_to_give -= 1
