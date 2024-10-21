import customtkinter 

def button_callback():
    print("button pressed")

app = customtkinter.CTk()
app.title("Calculaí")
app.geometry("300x350")
app.minsize(300, 300)  # Tamanho mínimo
app.maxsize(400, 400)
app.grid_columnconfigure((0), weight=1)

numero1 = customtkinter.CTkEntry(app, placeholder_text="Números")
numero1.grid(row=0, column=0, padx=20, pady=20, sticky="ew", columnspan=4)

#linha 2
button = customtkinter.CTkButton(app, text="7", command=button_callback, fg_color="#578018", hover_color="#009440", width=40, height=30)
button.grid(row=2, column=0, padx=10, pady=(0, 20), sticky="w")

button = customtkinter.CTkButton(app, text="8", command=button_callback, fg_color="#578018", hover_color="#009440", width=40, height=30)
button.grid(row=2, column=1, padx=20, pady=(0, 20), sticky="w")

button = customtkinter.CTkButton(app, text="9", command=button_callback, fg_color="#578018", hover_color="#009440", width=40, height=30)
button.grid(row=2, column=2, padx=20, pady=(0, 20), sticky="w")

button = customtkinter.CTkButton(app, text="+", command=button_callback, fg_color="#578018", hover_color="#009440", width=40, height=30)
button.grid(row=2, column=3, padx=20, pady=(0, 20), sticky="w")

#linha 3
button = customtkinter.CTkButton(app, text="4", command=button_callback, fg_color="#578018", hover_color="#009440", width=40, height=30)
button.grid(row=3, column=0, padx=10, pady=(0, 20), sticky="w")

button = customtkinter.CTkButton(app, text="5", command=button_callback, fg_color="#578018", hover_color="#009440", width=40, height=30)
button.grid(row=3, column=1, padx=20, pady=(0, 20), sticky="w")

button = customtkinter.CTkButton(app, text="6", command=button_callback, fg_color="#578018", hover_color="#009440", width=40, height=30)
button.grid(row=3, column=2, padx=20, pady=(0, 20), sticky="w")

button = customtkinter.CTkButton(app, text="-", command=button_callback, fg_color="#578018", hover_color="#009440", width=40, height=30)
button.grid(row=3, column=3, padx=20, pady=(0, 20), sticky="w")

#linha 4
button = customtkinter.CTkButton(app, text="1", command=button_callback, fg_color="#578018", hover_color="#009440", width=40, height=30)
button.grid(row=4, column=0, padx=10, pady=(0, 20), sticky="w")

button = customtkinter.CTkButton(app, text="2", command=button_callback, fg_color="#578018", hover_color="#009440", width=40, height=30)
button.grid(row=4, column=1, padx=20, pady=(0, 20), sticky="w")

button = customtkinter.CTkButton(app, text="3", command=button_callback, fg_color="#578018", hover_color="#009440", width=40, height=30)
button.grid(row=4, column=2, padx=20, pady=(0, 20), sticky="w")

button = customtkinter.CTkButton(app, text="x", command=button_callback, fg_color="#578018", hover_color="#009440", width=40, height=30)
button.grid(row=4, column=3, padx=20, pady=(0, 20), sticky="w")

#linha 5
button = customtkinter.CTkButton(app, text="0", command=button_callback, fg_color="#578018", hover_color="#009440", width=40, height=30)
button.grid(row=5, column=0, padx=10, pady=(0, 20), sticky="w")

button = customtkinter.CTkButton(app, text=",", command=button_callback, fg_color="#578018", hover_color="#009440", width=40, height=30)
button.grid(row=5, column=1, padx=20, pady=(0, 20), sticky="w")

button = customtkinter.CTkButton(app, text=".", command=button_callback, fg_color="#578018", hover_color="#009440", width=40, height=30)
button.grid(row=5, column=2, padx=20, pady=(0, 20), sticky="w")

button = customtkinter.CTkButton(app, text="/", command=button_callback, fg_color="#578018", hover_color="#009440", width=40, height=30)
button.grid(row=5, column=3, padx=20, pady=(0, 20), sticky="w")

#linha 6
button = customtkinter.CTkButton(app, text="=", command=button_callback, fg_color="#FFFF00", hover_color="#ff6400", text_color="#000")
button.grid(row=6, column=0, padx=10, pady=(0, 20), sticky="ew", columnspan=4)


app.mainloop()