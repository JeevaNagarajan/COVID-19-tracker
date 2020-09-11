from covid import Covid
from tkinter import *

gui = Tk()

covid_19 = Covid()

gui.title('Covid-19 Tracker')
gui.geometry('630x550')
gui.configure(background="dim grey")

string_variable = StringVar()

def search():
    try:
        getting_status = covid_19.get_status_by_country_name(string_variable.get())

        country = getting_status.get('country')
        cofirmed = getting_status.get('confirmed')
        active = getting_status.get('active')
        deaths = getting_status.get('deaths')
        recovered = getting_status.get('recovered')

        e2_var = StringVar(value=country)
        name_label = Label(gui, text="Country", fg='spring green', bg='dim grey', font=("Helvetica", 15)).grid(row=2,column=1)
        e2 = Entry(gui, textvariable=e2_var, font=("Helvetica", 17), fg='blue violet').grid(row=2, column=2, padx=20,pady=20)

        e3_var = StringVar(value=cofirmed)
        confirmed_label = Label(gui, text="Confirmed", fg='spring green', bg='dim grey', font=("Helvetica", 15)).grid(row=3, column=1)
        e3 = Entry(gui, textvariable=e3_var, font=("Helvetica", 17), fg='blue violet').grid(row=3, column=2, padx=20,pady=20)

        e4_var = StringVar(value=active)
        active_label = Label(gui, text="Active", fg='spring green', bg='dim grey', font=("Helvetica", 15)).grid(row=4,column=1)
        e4 = Entry(gui, textvariable=e4_var, font=("Helvetica", 17), fg='blue violet').grid(row=4, column=2, padx=20,pady=20)

        e5_var = StringVar(value=deaths)
        deaths_label = Label(gui, text="Deaths", fg='spring green', bg='dim grey', font=("Helvetica", 15)).grid(row=5,column=1)
        e5 = Entry(gui, textvariable=e5_var, font=("Helvetica", 17), fg='blue violet').grid(row=5, column=2, padx=20,pady=20)

        e6_var = StringVar(value=recovered)
        recovered_label = Label(gui, text="Recovered", fg='spring green', bg='dim grey', font=("Helvetica", 15)).grid(row=6, column=1)
        e6 = Entry(gui, textvariable=e6_var, font=("Helvetica", 17), fg='blue violet').grid(row=6, column=2, padx=20,pady=20)
    except:
        string_variable.set("Incorrect Country Name!!")

def clear():
    string_variable.set("")

def close():
    gui.destroy()

entry_label = Label(gui,text = "Enter the Country Name ",fg='ghost white',bg='dim grey',font = ('Helvetica',14)).grid(row = 0, column = 1)
e1 = Entry(gui,textvariable=string_variable,font=('Helvetica',14),fg='tomato').grid(row = 0, column = 2,padx=20, pady=20)

button_search = Button(gui, text='search ',font=("Helvetica", 10), fg='gainsboro', bg='royalblue4', command=search,  height=2, width=8).grid(row=0,column=3)
button_clear = Button(gui, text='clear ',font=("Helvetica", 10), fg='gainsboro', bg='royalblue4', command=clear,  height=2, width=8).grid(row=1,column=2)
button_exit = Button(gui, text='exit ',font=("Helvetica", 10), fg='gainsboro', bg='royalblue4', command=close,  height=2, width=8).grid(row=7,column=3)

gui.mainloop()
