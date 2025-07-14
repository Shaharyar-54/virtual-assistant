
# ui/main_ui.py
import customtkinter as ctk
import threading
from assistant import listen, handle_command, speak
import webbrowser

def create_ui():
    app = ctk.CTk()
    app.title("Virtual Assistant")
    app.geometry("800x600")
    app.configure(fg_color="#0a0a23")  # dark background

    def start_listening():
        threading.Thread(target=capture_voice).start()

    def capture_voice():
        command = listen()
        if command:
            output_textbox.configure(state="normal")
            output_textbox.insert(ctk.END, f"You: {command}\n", "user")
            output_textbox.update()
            handle_command(command)
            output_textbox.insert(ctk.END, f"Assistant: Done!\n", "assistant")
            output_textbox.configure(state="disabled")
            output_textbox.yview(ctk.END)

    def search_online():
        query = search_entry.get()
        if query:
            webbrowser.open(f"https://www.google.com/search?q={query}")
            speak(f"Searching for {query}")

    # UI Widgets
    title_label = ctk.CTkLabel(app, text="Virtual Assistant", font=("Arial", 28, "bold"), text_color="white")
    title_label.pack(pady=20)

    search_entry = ctk.CTkEntry(app, width=400, placeholder_text="Type to Search...")
    search_entry.pack(pady=10)

    search_button = ctk.CTkButton(app, text="Search 🔍", command=search_online)
    search_button.pack(pady=5)

    mic_button = ctk.CTkButton(app, text="🎤 Speak", command=start_listening, width=100)
    mic_button.pack(pady=10)

    output_textbox = ctk.CTkTextbox(app, width=700, height=300, state="disabled")
    output_textbox.pack(pady=20)

    output_textbox.tag_config("user", foreground="cyan")
    output_textbox.tag_config("assistant", foreground="lightgreen")

    app.mainloop()
