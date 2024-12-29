from appJar import gui
### http://appjar.info/
app = gui()

app.addLabel("title","wellcome")
app.yesNoBox("yes","Do you want to play poker")

app.go()