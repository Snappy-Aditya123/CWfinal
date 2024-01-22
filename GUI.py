import tkinter as tk
from Simulation import Simulation
import Lane_Management
import threading
from datetime import datetime
import os
class App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("450x200")
        self.create_frames()
        self.create_buttons()
        self.simulation = Simulation()
    
    def create_frames(self):
        self.frame = tk.Frame(self.root, bg="black", width=410, height=100)
        self.frame.grid(row=0, column=0, padx=10, pady=10)
        self.frame.grid_propagate(False)

    def rander_sim_labels(self):
        pass

    def start_simulation_thread(self, button_type):
        if button_type == "start_simulation":
    
            self.simulation_thread = threading.Thread(target=self.start_simulation)
            self.simulation_thread.start()
        elif button_type == "stop_Simulation_thread":
            self.stop_simulation()
        elif button_type == "end_simulation_thread":
            self.exit_simulation()
            self.simulation_thread.join()
        elif button_type == "run_sub_feature_5_thread":
            threading.Thread(target=self.run_sub_feature_5_thread).start()

    def exit_simulation(self):
        
        if self.simulation_thread is not None:
            self.simulation.stop_simulation()
        self.root.destroy()
        print("",end="\r")
    def stop_simulation(self):
        if self.simulation_thread is not None:
            self.simulation.stop_simulation()
    
    
    def start_simulation(self):
        print("--------------------------------------------------\n"
          "                     MENU\n"
          "Supermarket Checkout Lane Queue Simulation System\n"
          "\n"
          "- Simulation starts by generating 10 customers\n"
          "- The System will assign customers to lanes\n"
          "- If a lane is full, a new one opens if available\n"
          "- During the Simulation, Customers will leave lane when checkout\n"
          "- Simulation ends after a specific time entered by the user\n"
          "\n"
          "--------------------------------------------------\n")
    

    # Creating an instance of the Simulation class
        

    # Initiating the simulation with the prepared lanes
        self.simulation.set_sim_flag()
        self.simulation.initiate_simulation()

    # Displaying detailed information about all customers after the simulation

    def run_sub_feature_5_thread(self):
        self.simulation.display_currentlane_statuses()

 

   
        

    def create_buttons(self):
        start_button = tk.Button(self.frame, text="Start Simulation", command=lambda: self.start_simulation_thread("start_simulation"))
        run_sub_feature_5 = tk.Button(self.frame, text="Show Customer Details", command=lambda: self.start_simulation_thread("run_sub_feature_5_thread"))
        stop_Simulation =  tk.Button(self.frame, text="Stop Simulation", command=lambda: self.start_simulation_thread("stop_Simulation_thread"))
        exit_simultion = tk.Button(self.frame, text="exit simultion", command=lambda: self.start_simulation_thread("end_simulation_thread"))

        start_button.grid(row=1, column=0)
        run_sub_feature_5.grid(row=1, column=1)
        stop_Simulation.grid(row=1, column=2)
        exit_simultion.grid(row=1, column=3)

    def toggle_labels(self, button_type):
        if button_type == "start_simulation":
            pass
        elif button_type == "show_customer_details":
            pass

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()