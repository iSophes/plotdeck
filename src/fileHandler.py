from PySide6.QtWidgets import QFileDialog
import plot

def GetFiles(QWidget):
    return QFileDialog.getOpenFileNames(QWidget, "Import Files", "", "Media (*.mp3 *.mp4 *.aac *.wav *.flac *.m4a *.ogg *.avi *.mkv *.flv *.mov)")

def ImportFiles(QWidget, explorer):
    files = GetFiles(QWidget)
    if not files:
        return False
    
    CurrentPlots = explorer.getPlots()
    usableFiles = files[0]

    for file in usableFiles:
        skipFile = False

        for loopPlots in CurrentPlots:            
            if loopPlots.getTrack() == file:
                skipFile = True
                break
                
        
        if skipFile:
            continue

        newPlot = plot.Plot(file, len(explorer.getPlots()) + 1)
        
        fileName = file.split("/")[-1]
        newPlot.setName(fileName)

        CurrentPlots.append(newPlot)
    
    explorer.setPlots(CurrentPlots)