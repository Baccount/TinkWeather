import tkinter as tk

WIN_SIZE = "200x100"



def close_window():
    window.destroy()

def check_weather(stuff):
    # Check the weather
    print(stuff)

### ? Main Program Entry Point ###

window = tk.Tk()
window.title("TinkWeather")
window.geometry(WIN_SIZE)
window.protocol("WM_DELETE_WINDOW", close_window)
window.resizable(False, False)
# center the window
x = (window.winfo_screenwidth() // 2) - (100 // 2)
y = (window.winfo_screenheight() // 2) - (100 // 2)
window.geometry('{}x{}+{}+{}'.format(200, 100, x, y))

# * add label to top of window
label = tk.Label(window, text="TinkWeather", font=("Arial", 20))
label.pack()


# * clicking enter in the txt box will call this function
text = tk.Entry(window, width=20)
text.focus_set()
# bind the enter key to the check_weather function
window.bind('<Return>', lambda event: check_weather(text.get()))
text.pack()




def main():
    # Create a window
    window.mainloop()






if __name__ == '__main__':
    main()