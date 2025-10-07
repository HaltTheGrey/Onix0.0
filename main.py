import customtkinter as ctk
import os
import sys

ctk.set_appearance_mode("dark")  # Options: "light", "dark", "system"
ctk.set_default_color_theme("blue")  # Options: "blue", "green", "dark-blue"


class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        #c Configure the main window
        
        self.title("onix 0.0")
        self.geometry("800x600")
        self.minsize(400, 300)
        
        self.center_window()
        
        self.create_widgets()
        
    def center_window(self):
        """Center the window on the screen"""
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f"{width}x{height}+{x}+{y}")
        
    def create_widgets(self):
        """Create and place all widgets"""
        
        # Main title
        
        self.title_label = ctk.CTkLabel(
            self,
            text="Welcome to Onix 0.0",
            font=ctk.CTkFont(size=24, weight="bold")
        )
        self.title_label.pack(pady=20)
        
        
        # Example button
        self.button = ctk.CTkButton(
            self,
            text="Click Me!",
            command=self.button_callback,
            width=200,
            height=40,
            
        )
        self.button.pack(pady=10)
        
        # Example text box
        self.textbox = ctk.CTkTextbox(self, width=400, height=200)
        self.textbox.pack(pady=20, padx=20, fill="both", expand=True)
        self.textbox.insert("0.0", "This is a text box. \nYou can add your content here...")
        
    def button_callback(self):
        """Handle button clicked"""
        print("Button clicked!")
        self.textbox.insert("end", "\nButton was clicked!")
        

def main():
    """Main function to run the application"""
    app = MainWindow()
    app.mainloop
    
if __name__ == "__main__":
    main()