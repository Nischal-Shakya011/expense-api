class Developer:

    def __init__(
        self,
        name: str,
        experience: int,
        skills: list[str]
    ):
        self.name = name
        self.experience = experience
        self.skills = skills

    def add_skill(self, skill: str):
        self.skills.append(skill)

    def has_skill(self, skill: str) -> bool:
        return skill in self.skills

    def is_senior(self) -> bool:
        return self.experience >= 3
    

developer = Developer(
    "Nischal",
    2,
    ["Python", "React"]
)

developer.add_skill("FastAPI")
print(developer.has_skill("FastAPI"))
print(developer.skills)
print(developer.is_senior())