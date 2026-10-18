from core.signal import Signal

current_selected_cue: int = -1
update_selected_cue = Signal()


def updateSelectedCue(id: int):
    global current_selected_cue
    current_selected_cue = id
    update_selected_cue.fire(id)
