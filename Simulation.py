
from datetime import datetime, timedelta
from Lane_Management import Lane_Management
import time
import random

class Simulation:
    def __init__(self):
        self.lane_manager = Lane_Management()
        self.stop_flag = False
        self.flag_lane = False
    def stop_simulation(self):
        self.stop_flag = True
    def set_sim_flag(self):
        self.stop_flag = False

    def display_currentlane_statuses(self):
        self.flag_lane = True
    

    def initiate_simulation(self):
        
        # Get the simulation duration from the user
        simulation_duration_seconds = int(input("Enter the duration of the simulation in seconds: "))
        time_interval_seconds = 3  # Time in seconds for the simulation to continue (3 seconds to see status)
        lanes = self.lane_manager.set_up_lanes()

        # Assign 10 customers to lanes at the beginning of the simulation
        self.lane_manager.assign_customers_to_lanes(lanes, 10)

        # Record the start time of the simulation
        timestamp_start = datetime.now().strftime('%H:%M:%S')

        # Print the initial status of lanes
        print(f"------------Lane status at the start of simulation------------")
        print(
            f"Total number of customers waiting to check out at {timestamp_start} is: {self.lane_manager.get_total_customers(lanes)}")
        
        
        self.lane_manager.display_lane_statuses(lanes)

        # Start the simulation with the specified parameters
        self.run_simulation(lanes, simulation_duration_seconds, time_interval_seconds)


    def run_simulation(self,lanes, simulation_duration_seconds, time_interval_seconds):
        # Record the start time of the simulation
        start_time = datetime.now()

        # Calculate the end time of the simulation
        end_time = start_time + timedelta(seconds=simulation_duration_seconds)

        # Run the simulation loop until the end time is reached
        flag = 0 
        n = 0
        while datetime.now() < end_time and not self.stop_flag:
            # Pause execution to simulate the passage of time
            time.sleep(time_interval_seconds)

            # Record the current time for display
            current_time = datetime.now().strftime('%H:%M:%S')
            print(f"\n------------Lane status at {current_time}------------")

            # Display the current status of lanes
            if self.flag_lane:
                
                self.lane_manager.display_lane_statuses(lanes)
        
            else:
                pass

            # Generate a random number of customers and assign them to lanes
          
            if datetime.now() >= start_time + timedelta(seconds=15 * n):
        # Generate customers
                self.lane_manager.generate_random_customers(lanes)
                n += 1   
            

            # Process customers in lanes and manage the status of lanes
            self.lane_manager.process_customers_in_lanes(lanes)
            self.lane_manager.manage_lanes(lanes)

        # End the simulation and display the simulation end time
        Simulation.end_simulation()
        self.lane_manager.display_all_customer_details()
    


    @staticmethod
    def end_simulation():
        # Record the end time of the simulation
        timestamp_end = datetime.now().strftime('%H:%M:%S')

        # Display a message indicating the end of the simulation
        print(f"\n------------Simulation ended at {timestamp_end}------------")
        


