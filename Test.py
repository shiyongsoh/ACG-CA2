import  tkinter as tk
from tkinter import filedialog
import webbrowser

root = tk.Tk()

def hi():
    root.filename = filedialog.askopenfilename(initialdir="/Users/bryan/OneDrive - Singapore Polytechnic/DISM Y1 S2")

def spatsOpenWeb():
    webbrowser.open("https://myats.sp.edu.sg/psc/cs90atstd/EMPLOYEE/HRMS/c/A_STDNT_ATTENDANCE.A_ATS_STDNT_SBMIT.GBL?",new=1)

def keepOpenWeb():
    webbrowser.open("https://keep.google.com/u/0/",new=1)

def bbOpenWeb():
    webbrowser.open("https://esp.sp.edu.sg/webapps/portal/execute/tabs/tabAction?tab_tab_group_id=_3_1",new=1)

button1=tk.Button(padx=1000, pady=100,bg="#A9A9A9",text="Singapore Polytechnic - Attendance Taking",command=spatsOpenWeb)
button1.pack()

button3=tk.Button(padx=1000, pady=100,bg="#A9A9A9",text="Singapore Polytechnic - Blackboard",command=bbOpenWeb)
button3.pack()

button2=tk.Button(padx=1000, pady=100,bg="#A9A9A9",text="Google Keep",command=keepOpenWeb)
button2.pack()

root.mainloop()
