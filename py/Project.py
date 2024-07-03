import tkinter as tk
from tkinter import messagebox
import platform
from PIL import ImageTk, Image
import webbrowser

# Function to display project information
def show_project_info():
    webbrowser.open("file:///C:\Python\py\pro.html")

# Function to block a website
def block_website():
    if website_entry.get() == "":
        messagebox.showerror("Error", "Please Enter a Website")
        return
    if password_entry.get() == "":
        messagebox.showerror("Error", "Please Enter a Password")
        return
    if password_entry.get() != "Supraja":
        messagebox.showerror("Error", "Please Enter a Valid Password")
        return

    # Define the websites you want to block
    websites_to_block = website_entry.get()

    # Determine the path of the hosts file based on the operating system
    system_name = platform.system()
    if system_name == "Windows":
        hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
    elif system_name == "Linux" or system_name == "Darwin":  # macOS is a Unix-like system
        hosts_path = "/etc/hosts"
    else:
        messagebox.showerror("Error", "Unsupported operating system: " + system_name)
        return

    # Open the hosts file in append mode and add blocking rules
    with open(hosts_path, "a") as hosts_file:
        entry = "127.0.0.1 " + websites_to_block + "\n"
        hosts_file.write(entry)

    messagebox.showinfo("Blocked", "Successfully Blocked Website")

# Function to unblock a website
def unblock_website():
    if website_entry.get() == "":
        messagebox.showerror("Error", "Please Enter a Website")
        return
    if password_entry.get() == "":
        messagebox.showerror("Error", "Please Enter a Password")
        return
    if password_entry.get() != "Supraja":
        messagebox.showerror("Error", "Please Enter a Valid Password")
        return

    # Define the websites you want to unblock
    websites_to_unblock = website_entry.get()

    # Determine the path of the hosts file based on the operating system
    system_name = platform.system()
    if system_name == "Windows":
        hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
    elif system_name == "Linux" or system_name == "Darwin":  # macOS is a Unix-like system
        hosts_path = "/etc/hosts"
    else:
        messagebox.showerror("Error", "Unsupported operating system: " + system_name)
        return

    # Read the contents of the hosts file
    with open(hosts_path, "r") as hosts_file:
        lines = hosts_file.readlines()

    # Remove the blocking rules from the hosts file
    with open(hosts_path, "w") as hosts_file:
        for line in lines:
            should_remove = False
            if websites_to_unblock in line:
                should_remove = True
            if not should_remove:
                hosts_file.write(line)

    messagebox.showinfo("Unblocked", "Successfully Unblocked Website")

# Function to check if a website is blocked and redirect to the website
def check_website():
    if website_entry.get() == "":
        messagebox.showerror("Error", "Please Enter a Website")
        return

    # Define the website to check
    website_to_check = website_entry.get()

    # Open the website in the default web browser
    webbrowser.open(website_to_check)

# Create a tkinter window
window = tk.Tk()
window.title("Website Blocker")
window.configure(background="black")

# Set window size and position
window_width = 400
window_height = 400
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Load and display an image
image = Image.open("pro.jpg")  # Replace "proimg.jpg" with your image file
image = image.resize((100, 100), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image)
image_label = tk.Label(window, image=photo)
image_label.pack(pady=10)

# Create the "Website Blocker" label
title_label = tk.Label(window, text="Website Blocker", font=("Arial", 18), fg="white", bg="black")
title_label.pack(pady=5)

# Create the "Enter Website" label and entry
website_frame = tk.Frame(window, bg="black")
website_frame.pack(pady=10)
website_label = tk.Label(website_frame, text="Enter Website:", font=("Arial", 12), fg="white", bg="black")
website_label.pack(side="left", padx=(5, 10))
website_entry = tk.Entry(website_frame, font=("Arial", 12))
website_entry.pack(side="left")

# Create the "Enter Password" label and entry
password_frame = tk.Frame(window, bg="black")
password_frame.pack(pady=5)
password_label = tk.Label(password_frame, text="Enter Password:", font=("Arial", 12), fg="white", bg="black")
password_label.pack(side="left", padx=(5, 10))
password_entry = tk.Entry(password_frame, show="*", font=("Arial", 12))
password_entry.pack(side="left")

# Create the buttons frame
button_frame = tk.Frame(window, bg="black")
button_frame.pack(pady=10)

# Create the "Block" button
block_button = tk.Button(button_frame, text="Block", font=("Arial", 12), bg="red", command=block_website)
block_button.pack(side="left", padx=5)

# Create the "Unblock" button
unblock_button = tk.Button(button_frame, text="Unblock", font=("Arial", 12), bg="blue", command=unblock_website)
unblock_button.pack(side="left", padx=5)

# Create the "Check Website" button
check_button = tk.Button(button_frame, text="Check Website", font=("Arial", 12), bg="green", command=check_website)
check_button.pack(side="left", padx=5)

# Create the "Project Info" button
info_button = tk.Button(button_frame, text="Project Info", font=("Arial", 12), bg="yellow", command=show_project_info)
info_button.pack(side="left", padx=5)

# Run the GUI event loop
window.mainloop()