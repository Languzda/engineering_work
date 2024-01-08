from datetime import datetime

class Logs:
    logs = []

    def __init__(self):
        self.logs = []

    def add(self, logType: str, logMessage: str):
        currentTime = datetime.now()
        logEntry = {
            "type": logType,
            "message": logMessage,
            "time": int(currentTime.timestamp() * 1000)  # Czas w milisekundach od 1970 roku
        }
        self.logs.append(logEntry)

logger = Logs()