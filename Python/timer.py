import tkinter as tk

class timerApp:
    def __init__ (self,root):
        self.root = root
        self.root.title("Timer Application")

        self.milli = 0

        self.seconds = 0
        self.timerRunning = False

        self.timerLabel = tk.Label(root, text="00:00:00:000", font=("Helvetica", 48))
        self.timerLabel.pack(pady = 20)

        self.startButton = tk.Button(root, text = "Start Timer", command = self.startTimer)
        self.stopButton = tk.Button(root, text = "Stop Timer", command = self.stopTimer)
        self.startButton.pack (side=tk.LEFT, padx=10)
        self.stopButton.pack (side=tk.RIGHT, padx=10)

        self.updateTimer()

    def startTimer(self):
        if not self.timerRunning:
            self.timerRunning = True
            self.updateTimer()

    def stopTimer(self):
        self.timerRunning = False

    def updateTimer(self):
        if self.timerRunning:
            self.milli += 20
            seconds = self.milli // 1000
            milli = self.milli % 1000
            minutes = seconds // 60
            seconds = seconds % 60
            hour = minutes // 60
            minutes = minutes % 60
            timeString = "{:02}:{:02}:{:02}:{:02}".format(hour, minutes, seconds, milli)
            self.timerLabel.config(text=timeString)
            self.root.after(20, self.updateTimer) #Update Timer few milliseconds

if __name__ == "__main__":
    root = tk.Tk()

    app = timerApp(root)
    root.mainloop() 