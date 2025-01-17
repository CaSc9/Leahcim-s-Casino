import tkinter as tk

root= tk.Tk()
root.title = "Roulette"
root.geometry("1000x750")
root.grid()
root.label = tk.Label(root,text="Willkommen zu Roulettte"   )
root.label.grid(column=1, row=3)



root.mainloop()



# GUI Fenster
window = tk.Tk()
window.title("Leahcim's Roulette Casino")
window.geometry("600x600")

# Kontostand Sektion
frame_balance = tk.Frame(window, pady=10)
frame_balance.pack()

lbl_kontostand = tk.Label(frame_balance, text="Aktueller Kontostand: 0€", font=("Arial", 14))
lbl_kontostand.pack()

tk.Label(frame_balance, text="Betrag hinzufügen (in €):").pack()
e_wert = tk.Entry(frame_balance)
e_wert.pack()

btn_geld = tk.Button(frame_balance, text="Chips auszahlen", command= geld_anfordern())
btn_geld.pack()

# Wetten Sektion
frame_bets = tk.Frame(window, pady=20)
frame_bets.pack()

tk.Label(frame_bets, text="Wetttyp auswählen:").pack()
cb_wetttyp = ttk.Combobox(frame_bets, values=[
    "full number", "odd/even", "red/black"
])
cb_wetttyp.pack()

tk.Label(frame_bets, text="Wettwert (z.B. Zahl 12, Odd, Red):").pack()
e_wettwert = tk.Entry(frame_bets)
e_wettwert.pack()

tk.Label(frame_bets, text="Einsatz (in €):").pack()
e_einsatz = tk.Entry(frame_bets)
e_einsatz.pack()

btn_wette = tk.Button(frame_bets, text="Wette hinzufügen", command= define_bets())
btn_wette.pack()

# Wetten Liste
frame_wetten = tk.Frame(window, pady=10)
frame_wetten.pack()

tk.Label(frame_wetten, text="Ihre Wetten:").pack()
wett_liste = ttk.Treeview(frame_wetten, columns=("Typ", "Wert", "Einsatz"), show="headings")
wett_liste.heading("Typ", text="Typ")
wett_liste.heading("Wert", text="Wert")
wett_liste.heading("Einsatz", text="Einsatz")
wett_liste.pack()

# Spin Sektion
frame_spin = tk.Frame(window, pady=20)
frame_spin.pack()

btn_spin = tk.Button(frame_spin, text="Drehen!", command=spin)
btn_spin.pack()

lbl_ergebnis = tk.Label(frame_spin, text="", font=("Arial", 16))
lbl_ergebnis.pack()

# Hauptfenster starten
window.mainloop()



label = tk.Label(root, text="Roulette", font=("Helvetica", 24))
label.grid(row=0, column=0, columnspan=2, pady=10)
bet_label = tk.Label(root, text="Einsatz:")
bet_label.grid(row=1, column=0)
bet_entry = tk.Entry(root)
bet_entry.grid(row=1, column=1)

bet_type = tk.StringVar(value="Farbe")
farbe_button = tk.Radiobutton(root, text="Auf Farbe wetten", variable=bet_type, value="Farbe")
farbe_button.grid(row=2, column=0, sticky="w")
nummer_button = tk.Radiobutton(root, text="Auf Zahl wetten", variable=bet_type, value="Nummer")
nummer_button.grid(row=3, column=0, sticky="w")

farbe_choice = tk.StringVar(value="green")
farbe_menu = tk.OptionMenu(root, farbe_choice, "red", "black", "green")
farbe_menu.grid(row=2, column=1)
nummer_choice = tk.Entry(root)
nummer_choice.grid(row=3, column=1)

spin_button = tk.Button(root, text="Drehen", command=spin)
spin_button.grid(row=4, column=0, columnspan=2, pady=10)

win_label = tk.Label(root, text="", font=("Helvetica", 14))
win_label.grid(row=5, column=0, columnspan=2, pady=10)

balance_label = tk.Label(root, text=f"Dein Guthaben: {kontostand} CHF", font=("Helvetica", 14))
balance_label.grid(row=6, column=0, columnspan=2, pady=10)

quit_button = tk.Button(root, text="Beenden", command=root.quit)
quit_button.grid(row=7, column=0, columnspan=2)
root.mainloop()