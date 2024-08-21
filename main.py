import pywhatkit as pykit
from ttkbootstrap import *


root = Window(themename="cyborg")
root.geometry("800x500")
root.title("WhatsApp!")

style = Style()
style.configure("warning.TButton", font=("Trebuchet MS", 18))
F1 = Frame(root)
L1 = Label(F1, text="Time: ", font=("Trebuchet MS", 18))
L1.pack(side="left")
E1 = Entry(F1, font=("Trebuchet MS", 18), bootstyle = "warning")
E1.pack(side="right")
F1.place(relx=0.5, rely=0.275, anchor="center")

F2 = Frame(root)
L2 = Label(F2, text="Phone Number: ", font=("Trebuchet MS", 18))
L2.pack(side="left")
E2 = Entry(F2, font=("Trebuchet MS", 18), bootstyle = "warning", width=20)
E2.pack(side="right")
S1 = Spinbox(F2, font=("Trebuchet MS", 18), values=["+" + str(i) for i in range(1, 999)], width=5)
S1.pack(side="right", padx = 10)
F2.place(relx=0.5, rely=0.5, anchor="center")

F3 = Frame(root)
L3 = Label(F3, text="Message: ", font=("Trebuchet MS", 18))
L3.pack(side="left")
E3 = Entry(F3, font=("Trebuchet MS", 18), bootstyle = "warning")
E3.pack(side="left")
def SendWhatMsg():
    global E1, E2, E3, S1
    Time_Hour = int(list(str(E1.get()).split(" : "))[0])
    Time_Min = int(list(str(E1.get()).split(" : "))[1])
    Phone = S1.get() + E2.get()
    Msg = E3.get()

    pykit.sendwhatmsg(phone_no=Phone, message=Msg, time_hour=Time_Hour, time_min=Time_Min)
    print("Done.... ")


B1 = Button(F3, text="Send", width=5, style = "warning.TButton", command=SendWhatMsg)
B1.pack(side="right", padx = 10)

F3.place(relx=0.5, rely=0.725, anchor="center")


root.mainloop()

