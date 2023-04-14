import tkinter as tk

import pickle


def main():
    # Create the main window
    root = tk.Tk()
    with open('NBClassifier.pkl','rb') as f:
        md = pickle.load(f)
        
    res = md.predict([[50,50,50]])
    
    # Set the window title
    root.title("Simple App")
    
    # Set the window size
    root.geometry("300x200")
    
    # Create a label widget
    label = tk.Label(root, text=res)
    
    # Add the label widget to the window
    label.pack()
    
    # Create a button widget
    button = tk.Button(root, text="Click Me!", command=button_clicked)
    
    # Add the button widget to the window
    button.pack()
    
    # Start the main event loop
    root.mainloop()

def button_clicked():
    print("Button clicked!")

if __name__ == "__main__":
    main()