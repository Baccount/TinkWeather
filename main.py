import tkinter as tk

WIN_SIZE = "200x100"


def clear_text():
    # clear the text in the text
    text.delete(0, tk.END)

def get_weather(zip):
    clear_text()
    # get the weather for the given zip code using the API
    import requests
    url = f"http://api.openweathermap.org/data/2.5/weather?zip={zip}&appid=49da89b32f4c7a4fc739dc2ba9f278d0"
    response = requests.get(url)
    # set the text of the label to the weather temp
    try:
        temp = response.json()["main"]["temp"]
        # convert the temp from Kelvin to Fahrenheit
        temp = (temp - 273.15) * 9/5 + 32
        temp = round(temp)
        # get the city name
        city_label["text"] = response.json()["name"]
        temp_label["text"] = str(temp) + "°F"
    except Exception as e:
        print(e)
        city_label["text"] = "Error"
        temp_label["text"] = ""

### ? Main Program Entry Point ###

window = tk.Tk()
window.title("TinkWeather")
window.geometry(WIN_SIZE)
window.resizable(False, False)
# center the window
x = (window.winfo_screenwidth() // 2) - (100 // 2)
y = (window.winfo_screenheight() // 2) - (100 // 2)
window.geometry('{}x{}+{}+{}'.format(200, 100, x, y))

# * add label to top of window
city_label = tk.Label(window, text="TinkWeather", font=("Arial", 20))
city_label.pack()

# * add label under the top label
temp_label = tk.Label(window, text="Enter Zip:", font=("Arial", 20))
temp_label.pack()


# * clicking enter in the txt box will call this function
text = tk.Entry(window, width=20) 
text.focus_set()
# bind the enter key to the get_weather function
window.bind('<Return>', lambda event: get_weather(text.get()))
# place the text box at the bottom
text.pack(side="bottom", fill="x", padx=10, pady=10)




def main():
    # Create a window
    window.mainloop()






if __name__ == '__main__':
    main()