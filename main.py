import pywhatkit

# !! in terminal xhost + if some error
# !! the transmitted text is written in qwerty even if your keyboard is in azerty
# no emoji
# you need to open whatsapp web and connect in

#sending programmed msg
pywhatkit.sendwhatmsg("+330629216675", "Hello you", 12, 35)

# Same as above but Closes the Tab in 2 Seconds after Sending the Message
#pywhatkit.sendwhatmsg("+910123456789", "Hi", 13, 30, 15, True, 2)

#send msg to group instantly
#pywhatkit.sendwhatmsg_to_group_instantly("address_to_invitation_group", "👋 Hello!")

#don't work msg it's sending to me
#pywhatkit.sendwhatmsg_to_group("address_to_invitation_group", "👋 Hello!", 12, 6)

# Send an Image to a Group with the Caption as Hello
# pywhatkit.sendwhats_image("AB123CDEFGHijklmn", "Images/Hello.png", "Hello")

# Send an Image to a Contact with the no Caption
#pywhatkit.sendwhats_image("+910123456789", "Images/Hello.png")