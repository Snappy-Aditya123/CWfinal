from Simulation import Simulation
from Lane_Management import Lane_Management

if __name__ == "__main__":
    # Displaying a simple menu to provide information about the simulation
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
    lane_manager = Lane_Management()
    # Setting up lanes for the simulation
    

    # Creating an instance of the Simulation class
    simulation = Simulation()

    # Initiating the simulation with the prepared lanes
    simulation.initiate_simulation()

    # Displaying detailed information about all customers after the simulation
    
