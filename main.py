import tkinter as tk

WIN_SIZE = "200x100"



def close_window():
    window.destroy()

def get_weather(zip):
    # get the weather for the given zip code using the API
    import requests
    url = f"http://api.openweathermap.org/data/2.5/weather?zip={zip}&appid=49da89b32f4c7a4fc739dc2ba9f278d0"
    response = requests.get(url)
    # set the text of the label to the weather temp
    try:
        temp = response.json()["main"]["temp"]
        # convert the temp from Kelvin to Fahrenheit
        temp = (temp - 273.15) * 9/5 + 32
        # round the temp to whole number
        temp = round(temp)
        # set the text of the label to the temp
        label["text"] = str(temp) + "°F"
    except:
        label["text"] = "Error"
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
# bind the enter key to the get_weather function
window.bind('<Return>', lambda event: get_weather(text.get()))
text.pack()




def main():
    # Create a window
    window.mainloop()






if __name__ == '__main__':
    main()