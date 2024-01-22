import random
from models import Regular_Lane, Self_service_lane, Customer
import datetime
class Lane_Management:
    def __init__(self):
        self.all_customers = [] #the all customers are saved here 
  
    def set_up_lanes(self):
        # Create regular lanes (1 to 5) and a self-service lane (6)
        lanes = [Regular_Lane(i) for i in range(1, 6)] + [Self_service_lane.Self_Service_Lane(6)]
        lanes[0].open_lane()  # Open the first regular lane
        lanes[5].open_lane()  # Open the self-service lane
        return lanes

    
    def generate_random_customers(self,lanes):
        flag = [lane.status for lane in lanes]
        if flag.count("full") == 6:
            # sets falg if all the lanes are full no customer is generated
            pass
        else:
        # Generate a random number of customers (1 to 5)
            num_customers = random.randint(1, 5)
            print(f"Arriving {num_customers} customers to the supermarket...")
            self.assign_customers_to_lanes(lanes, num_customers)
            

   
    def assign_customers_to_lanes(self,lanes, num_customers):
        # Assign each generated customer to a lane
        for i in range(num_customers):
            customer = Customer(self.get_total_customers(lanes) + 1)
            lane = self.move_lane(lanes, customer)
            if lane:
                #adding customers to the lane and the all_customers lists
                self.all_customers.append(customer)
                lane.add_customer(customer)
                # Print information about the assigned customer
                checkout_time = customer.get_checkout_time(lane.lane_type)
                print(f"C{customer.identifier} estimated checkout time: {checkout_time} Secs")

    
    def get_total_customers(self,lanes):
        # Calculate the total number of customers in all lanes
        return len(self.all_customers)

    
    def move_lane(self,lanes, customer):
        # Decide whether to assign the customer to a self-service or regular lane
        if customer.get_basket_size() < 10:
            return self.get_self_service_lane(lanes)
        else:
            return self.get_regular_lane(lanes)

   
    def manage_lanes(self,lanes):
        # Manage the status of lanes (open or close based on the number of customers)
        for lane in lanes:
            if lane.status == 'opened':
                if len(lane.customers) == 0:
                    lane.close_lane()
            elif lane.status == 'closed':
                if len(lane.customers) > 0:
                    lane.open_lane()

    @staticmethod
    def display_lane_statuses(lanes):
        # Display the status of each lane
        for lane in lanes:
            lane.display_lane_status()

   
    def get_self_service_lane(self,lanes):
        # Find an open self-service lane with available capacity
        for lane in lanes:
            if lane.lane_type == 'Slf' and lane.status == 'opened' and len(lane.customers) < lane.get_lane_capacity():
                return lane
            else:
                self.get_regular_lane(lanes)
        return None

   
    def get_regular_lane(self,lanes):
        # Find an open regular lane with available capacity
        for lane in lanes:
            if lane.lane_type == 'Reg' and lane.status == 'opened' and len(lane.customers) < lane.get_lane_capacity():
                return lane
        # If all regular lanes are full, find a closed one to open
        for lane in lanes:
            if lane.lane_type == 'Reg' and lane.status == 'closed':
                lane.open_lane()
                return lane
        return None
    
    def move_lanes(self,lanes):

        #Thsi method moves customer from one lane to another 
        lan = [len(lane.customers) for lane in lanes]
        lan_max = lan.index(max(lan))
        lan_min = lan.index(min(lan))
        for i in range(random.randint(0,max(lan))):
            lanes[lan_min].add_customer(lanes[lan_max].customers.pop(-1))
        
            
   
    def award_lottery_ticket_if_eligible(self,customer):
        # Award a lottery ticket to the customer if eligible
        if customer.award_lottery_ticket():
            print(f"Customer {customer.identifier} won a lottery ticket!")

   
    def process_customers_in_lanes(self,lanes):
        # Process customers in each lane and award lottery tickets if eligible
        for lane in lanes:
            lane.process_checkout()
            
    

  
    def display_all_customer_details(self):
        print("\n----------------All Customer details after simulation ----------------")
        # Sort customers based on their identifiers
        self.all_customers.sort(key=lambda customer: customer.identifier)

        # Display customer details
        for customer in self.all_customers:
            customer.display_customer_details()
