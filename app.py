import re
import time
from groq_m import Engineers
from ollama_m import Leadership

TOPIC = (
    """
    Stocks are down 2% today, and we need to discuss our strategy for the next quarter.
    
    """
)

PARTICIPANTS = {
    "Tamim Dostyar": ("Tamim Dostyar (Director)", "director"),
    "Sarah Johnson": ("Sarah Johnson (Manager)", "manager"),
    "Marcus Williams": ("Marcus Williams (Senior Engineer)", "senior"),
    "Priya Patel": ("Priya Patel (Junior Engineer)", "junior"),
}

FIRST_NAMES = {
    "Tamim": "Tamim Dostyar",
    "Sarah": "Sarah Johnson",
    "Marcus": "Marcus Williams",
    "Priya": "Priya Patel",
}


def find_next_speaker(last_message: str, last_speaker: str) -> str:
    for name in PARTICIPANTS:
        if name in last_message and name != last_speaker:
            return name
    for first, full in FIRST_NAMES.items():
        if re.search(rf"\b{first}\b", last_message) and full != last_speaker:
            return full
    names = list(PARTICIPANTS.keys())
    idx = names.index(last_speaker) if last_speaker in names else 0
    return names[(idx + 1) % len(names)]

SEPARATOR = "─" * 60


def run_meeting():
    leadership = Leadership()
    engineers = Engineers()

    opening = f"[Tamim Dostyar (Director)]: {TOPIC}"
    conversation_log = opening

    print(SEPARATOR)
    print("TD COMPANY — TEAM MEETING")
    print(SEPARATOR)
    print(f"\n{opening}\n")

    duration = 5 * 60
    end_time = time.time() + duration
    last_speaker = "Tamim Dostyar"
    last_message = TOPIC

    while time.time() < end_time:
        next_name = find_next_speaker(last_message, last_speaker)
        label, role = PARTICIPANTS[next_name]

        try:
            if role == "director":
                response = leadership.director_respond(conversation_log)
            elif role == "manager":
                response = leadership.manager_respond(conversation_log)
            elif role == "senior":
                response = engineers.senior_respond(conversation_log)
            elif role == "junior":
                response = engineers.junior_respond(conversation_log)

            response = response.strip()
            if not response:
                print(f"[{label}]: (no response)\n")
                last_speaker = next_name
                last_message = ""
                continue

            message = f"[{label}]: {response}"
            print("Time remaining:", int(end_time - time.time()), "seconds")
            print(message)
            print()

            conversation_log += f"\n{message}"
            last_speaker = next_name
            last_message = response

        except Exception as e:
            print(f"[Error — {label}]: {e}\n")
            last_speaker = next_name
            last_message = ""

        time.sleep(3)

    print(SEPARATOR)
    print("Meeting ended (5 minutes)")
    print(SEPARATOR)


if __name__ == "__main__":
    run_meeting()
