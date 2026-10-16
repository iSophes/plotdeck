import json

from PySide6.QtWidgets import QFileDialog

import plot


class showFileHandler:
    showDictionary = {}  # {tracks: {[string]: {"cues": {
    # {name: string, type: number, timestamp: string, notes: string}
    # }}}}

    def __init__(self, explorer) -> None:
        self.explorer = explorer
