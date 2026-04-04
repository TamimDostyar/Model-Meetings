import os
from office import Office

DIRECTOR = os.getenv("DIRECTOR")
MANAGER = os.getenv("MANAGER")

if not DIRECTOR or not MANAGER:
    raise ValueError("DIRECTOR or MANAGER not set in environment variables.")


class Leadership(Office):
    def __init__(self):
        super().__init__()
        self._director_system = self.read_policy() + "\n\n" + self.read_position("position_details/director.md")
        self._manager_system = self.read_policy() + "\n\n" + self.read_position("position_details/manager.md")

    def director_respond(self, history: str) -> str:
        return self.ollama_respond(DIRECTOR, self._director_system, history, "Tamim Dostyar")

    def manager_respond(self, history: str) -> str:
        return self.ollama_respond(MANAGER, self._manager_system, history, "Sarah Johnson")
