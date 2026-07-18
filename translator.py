"""
CodeAlpha - Task 1: Language Translation Tool
GUI translator using deep-translator (wraps Google Translate, no API key required).
Optional text-to-speech via gTTS + playsound.
"""

import tkinter as tk
from tkinter import ttk, messagebox
from deep_translator import GoogleTranslator

# Common language codes supported by GoogleTranslator
LANGUAGES = {
    "auto": "Auto Detect", "en": "English", "ur": "Urdu", "hi": "Hindi",
    "ar": "Arabic", "fr": "French", "de": "German", "es": "Spanish",
    "zh-CN": "Chinese (Simplified)", "ja": "Japanese", "ko": "Korean",
    "ru": "Russian", "pt": "Portuguese", "it": "Italian", "tr": "Turkish",
}
CODE_BY_NAME = {v: k for k, v in LANGUAGES.items()}


class TranslatorApp:
    def __init__(self, root):
        self.root = root
        root.title("AI Language Translator - CodeAlpha")
        root.geometry("640x480")
        root.resizable(False, False)

        # Source language
        tk.Label(root, text="Source Language").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.src_lang = ttk.Combobox(root, values=list(LANGUAGES.values()), state="readonly", width=25)
        self.src_lang.set("Auto Detect")
        self.src_lang.grid(row=0, column=1, padx=10, pady=5)

        # Target language
        tk.Label(root, text="Target Language").grid(row=0, column=2, padx=10, pady=5, sticky="w")
        self.tgt_lang = ttk.Combobox(root, values=[v for v in LANGUAGES.values() if v != "Auto Detect"],
                                      state="readonly", width=25)
        self.tgt_lang.set("Urdu")
        self.tgt_lang.grid(row=0, column=3, padx=10, pady=5)

        # Input text box
        tk.Label(root, text="Enter Text:").grid(row=1, column=0, padx=10, pady=(15, 0), sticky="w")
        self.input_box = tk.Text(root, height=8, width=70, wrap="word")
        self.input_box.grid(row=2, column=0, columnspan=4, padx=10, pady=5)

        # Buttons
        tk.Button(root, text="Translate", command=self.translate, bg="#4CAF50", fg="white",
                  width=15).grid(row=3, column=0, padx=10, pady=10)
        tk.Button(root, text="Copy Output", command=self.copy_output, width=15).grid(row=3, column=1, pady=10)
        tk.Button(root, text="Speak Output", command=self.speak_output, width=15).grid(row=3, column=2, pady=10)
        tk.Button(root, text="Clear", command=self.clear_all, width=15).grid(row=3, column=3, pady=10)

        # Output text box
        tk.Label(root, text="Translated Text:").grid(row=4, column=0, padx=10, pady=(10, 0), sticky="w")
        self.output_box = tk.Text(root, height=8, width=70, wrap="word", bg="#f2f2f2")
        self.output_box.grid(row=5, column=0, columnspan=4, padx=10, pady=5)

    def translate(self):
        text = self.input_box.get("1.0", tk.END).strip()
        if not text:
            messagebox.showwarning("Input needed", "Please enter text to translate.")
            return

        src_code = CODE_BY_NAME.get(self.src_lang.get(), "auto")
        tgt_code = CODE_BY_NAME.get(self.tgt_lang.get(), "en")

        try:
            result = GoogleTranslator(source=src_code, target=tgt_code).translate(text)
            self.output_box.delete("1.0", tk.END)
            self.output_box.insert(tk.END, result)
        except Exception as e:
            messagebox.showerror("Translation Error", str(e))

    def copy_output(self):
        text = self.output_box.get("1.0", tk.END).strip()
        if text:
            self.root.clipboard_clear()
            self.root.clipboard_append(text)
            messagebox.showinfo("Copied", "Translated text copied to clipboard.")

    def speak_output(self):
        text = self.output_box.get("1.0", tk.END).strip()
        if not text:
            return
        try:
            from gtts import gTTS
            import tempfile, os, platform
            tgt_code = CODE_BY_NAME.get(self.tgt_lang.get(), "en")
            tts_lang = "zh-CN" if tgt_code == "zh-CN" else tgt_code
            tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
            gTTS(text=text, lang=tts_lang).save(tmp.name)
            if platform.system() == "Windows":
                os.system(f'start "" "{tmp.name}"')
            elif platform.system() == "Darwin":
                os.system(f'afplay "{tmp.name}"')
            else:
                os.system(f'xdg-open "{tmp.name}"')
        except Exception as e:
            messagebox.showerror("Text-to-Speech Error", str(e))

    def clear_all(self):
        self.input_box.delete("1.0", tk.END)
        self.output_box.delete("1.0", tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = TranslatorApp(root)
    root.mainloop()
