class Plot:
    def __init__(self, trackPath: str, trackOrder=int):
        self._trackPath = trackPath or ""
        self._cues = [
            {"cueName": "lighting", "message": "test", "timeStamp": "00:00.00"}
        ]
        self._name = ""
        self._trackOrder = trackOrder or 0

    def setTrack(self, trackPath):
        self._trackPath = trackPath
        # update signals

    def setName(self, name):
        self._name = name
    
    def getName(self):
        return self._name

    def getTrack(self):
        return self._trackPath

    def getCues(self):
        return self._cues

    def addCue(self, cueType, message, timestamp):
        currentCues = self._cues
        currentCues.append(
            {"cueType": cueType, "message": message, "timestamp": timestamp}
        )
        self._cues = currentCues
        return currentCues

    def setOrder(self, newOrder: int):
        self._trackOrder = newOrder
        return True

    def getOrder(self):
        return self._trackOrder
