import os
from office import Office

SENIOR_ENGINEER = os.getenv("SENIOR_ENGINEER")
JUNIOR_ENGINEER = os.getenv("JUNIOR_ENGINEER")

if not SENIOR_ENGINEER or not JUNIOR_ENGINEER:
    raise ValueError("SENIOR_ENGINEER or JUNIOR_ENGINEER not set in environment variables.")


class Engineers(Office):
    def __init__(self):
        super().__init__()
        self._senior_system = self.read_policy() + "\n\n" + self.read_position("position_details/senior_engineer.md")
        self._junior_system = self.read_policy() + "\n\n" + self.read_position("position_details/juniorengineer.md")

    def senior_respond(self, history: str) -> str:
        return self.groq_respond(SENIOR_ENGINEER, self._senior_system, history, "Marcus Williams")

    def junior_respond(self, history: str) -> str:
        return self.groq_respond(JUNIOR_ENGINEER, self._junior_system, history, "Priya Patel")
