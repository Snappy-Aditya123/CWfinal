# Lane class represents a checkout lane in a supermarket.
# It manages customer flow, lane status, and capacity.
from datetime import timedelta, datetime

class Lane:
    # Define constants for regular and self-service lane capacities.
    
    def __init__(self, lane_type, lane_id, lane_capacity):
        # Initialize lane with the provided type and ID.
        self.lane_type = lane_type
        self.lane_id = lane_id
        self.lane_capacity = lane_capacity
        # Set the initial status of the lane to 'closed'.
        self.status = 'closed'
        # Maintain a list to store customers currently in the lane.
        self.customers = []

    def add_customer(self, customer):
        # Add a customer to the lane if there is capacity.
        if len(self.customers) < self.get_lane_capacity():
            self.customers.append(customer)
        else:
            print(f"Cannot add customer {customer.identifier} to Lane {self.lane_id}. Lane is full.")

    def remove_customer(self, customer):
        # Remove a customer from the lane.
        if customer in self.customers:
            self.customers.remove(customer)

    def open_lane(self):
        # Open the lane for customer service.
        self.status = 'opened'
        # Display a message indicating that the lane is open.
     

    def close_lane(self):
        # Close the lane.
        self.status = 'closed'
        # Display a message indicating that the lane is closed.
        print(f"L{self.lane_id} ({self.lane_type}) is now closed.")
    
    def full_lane(self):
        self.status = 'full'
        print(f"L{self.lane_id} ({self.lane_type}) is now full.")

    def display_lane_status(self):
        # Display the current status of the lane, including the number of customers.
        lane_info = f"L{self.lane_id} ({self.lane_type})"

        if self.status == 'opened' or "full":
            # Display asterisks representing customers in the lane, or indicate 'closed' if no customers.
            customer_display = ' '.join('*' for i in range(len(self.customers))) if self.customers else 'closed'
        else:
            # If the lane is closed, display 'closed'.
            customer_display = 'closed'

        print(f"{lane_info} -> {customer_display}")

    def get_lane_capacity(self):
        # Get the capacity of the lane based on its type.
        if self.lane_type == 'Reg':
            return 5 
        else:
            return 15
        

    def process_checkout(self):
        
        # Simulate the checkout process by ckecking the customer checkout time through loop irreation
        if self.customers:
            for customer in self.customers:
                checkout_time = customer.get_checkout_time(self.lane_type)
                x = int(checkout_time)
                if customer.timecreated + timedelta(seconds=x) < datetime.now():
                    self.customers.remove(customer)
                else:
                    pass
        
            
            

    