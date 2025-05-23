# src/translator/gui.py
import sys
import os
import tkinter as tk
from tkinter import ttk, messagebox
from translator.core import load_translations

class TranslatorApp:
    def __init__(self, master):
        self.master = master
        master.title("NMS Translator")
        master.geometry("600x400")

        # Load translations with error handling
        try:
            self.translations = load_translations()
        except FileNotFoundError:
            messagebox.showerror("Error", "Translations file not found!")
            self.translations = {}
            self.master.destroy()
            return

        self.create_widgets()
        self.center_window()

    def center_window(self):
        self.master.update_idletasks()
        width = self.master.winfo_width()
        height = self.master.winfo_height()
        x = (self.master.winfo_screenwidth() // 2) - (width // 2)
        y = (self.master.winfo_screenheight() // 2) - (height // 2)
        self.master.geometry(f'+{x}+{y}')

    def create_widgets(self):
        main_frame = ttk.Frame(self.master)
        main_frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

        # Input Section
        input_frame = ttk.LabelFrame(main_frame, text=" Input Text ")
        input_frame.pack(fill=tk.X, pady=5)

        self.input_text = tk.Text(input_frame, height=8, wrap=tk.WORD)
        self.input_text.pack(padx=10, pady=10, fill=tk.BOTH)

        # Controls
        control_frame = ttk.Frame(main_frame)
        control_frame.pack(pady=10)

        self.translate_btn = ttk.Button(
            control_frame,
            text="Translate",
            command=self.translate_text
        )
        self.translate_btn.pack(side=tk.LEFT, padx=5)

        clear_btn = ttk.Button(
            control_frame,
            text="Clear",
            command=self.clear_text
        )
        clear_btn.pack(side=tk.LEFT, padx=5)

        # Output Section
        output_frame = ttk.LabelFrame(main_frame, text=" Translation ")
        output_frame.pack(fill=tk.BOTH, expand=True, pady=5)

        self.output_text = tk.Text(
            output_frame,
            height=8,
            wrap=tk.WORD,
            state='disabled'
        )
        self.output_text.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    def translate_text(self):
        input_str = self.input_text.get("1.0", "end-1c").strip()
        if not input_str:
            return

        translated_words = []
        for word in input_str.split():
            translated = self.translations.get(word.lower(), word)
            translated_words.append(translated)

        translated_text = ' '.join(translated_words)

        self.output_text.config(state='normal')
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, translated_text)
        self.output_text.config(state='disabled')

    def clear_text(self):
        self.input_text.delete("1.0", tk.END)
        self.output_text.config(state='normal')
        self.output_text.delete("1.0", tk.END)
        self.output_text.config(state='disabled')

def main():
    root = tk.Tk()
    try:
        TranslatorApp(root)
        root.mainloop()
    except Exception as e:
        messagebox.showerror("Fatal Error", f"Application crashed: {str(e)}")

if __name__ == "__main__":
    # Add package to path for direct execution
    sys.path.insert(0, os.path.abspath(os.path.join(
        os.path.dirname(__file__), '..', '..')))
    main()