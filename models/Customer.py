# Importing necessary module for basket creation and randomization
from .Basket import Basket
import random
import datetime
# Definition of the Customer class, representing a shopper in the supermarket


class Customer:
    # Constants for processing times and lottery threshold
    CASHIER_PROCESSING_TIME = 4
    SELF_SERVICE_PROCESSING_TIME = 6
    LOTTERY_THRESHOLD = 10
    
    # Constructor to initialize a customer with a unique identifier
    def __init__(self, identifier):
        # Unique identifier for the customer
        self.identifier = identifier
        # Creating a basket with a random size between 1 and 30
        self.basket = Basket(random.randint(1, 31))
    
        self.timecreated = datetime.datetime.now()
        # Determining if the customer has a lottery ticket based on basket size and random choice
        self.lottery_ticket = self.lottery_ticket()

    def lottery_ticket(self):
        #sets lotterey winner based on two conditions 
        if self.basket.get_size() > 10 and random.randint(0,100) > 0:
            return True
        else:
            return False

    # Method to get the size of the customer's basket
    def get_basket_size(self):
        return self.basket.get_size()

    # Method to calculate the checkout time based on whether it's a self-service lane or cashier lane
    def get_checkout_time(self, lane_type):
        # Processing time is determined by the size of the basket and the appropriate constant
        if lane_type == None:
            return [self.basket.get_size() * self.CASHIER_PROCESSING_TIME,self.basket.get_size() * self.SELF_SERVICE_PROCESSING_TIME]
        if lane_type == "Slf": 
            processing_time =   self.basket.get_size() * self.SELF_SERVICE_PROCESSING_TIME
        else: 
            processing_time  =  self.basket.get_size() * self.CASHIER_PROCESSING_TIME
        return processing_time

    # Method to check if the customer is eligible for a lottery ticket
    def award_lottery_ticket(self):
        return self.lottery_ticket

    # Method to display customer details, including basket size, lottery outcome, and checkout time
    def display_customer_details(self, lane_type=None):
        print("--------------------Customer details--------------------")
        # Displaying customer identifier and basket size
        basket_info = f"{self.identifier} -> items in basket: {self.basket.get_size()}, "
        # Displaying lottery outcome
        if self.lottery_ticket:
            lottery_info = 'wins a lottery ticket!' 
        else:
            lottery_info = 'Better luck with lotter ticket next time'
        # Displaying checkout time based on the type of lane
        processing_time_info = f"""time to process basket at {lane_type if lane_type != None else "Reg" } till: {self.get_checkout_time(lane_type)[0]} Secs
                                   time to process basket at {lane_type if lane_type != None else "Self"} till: {self.get_checkout_time(lane_type)[1]} Secs
                                """

        print(basket_info + lottery_info)
        print(processing_time_info)

    # Method to initiate the checkout process and return the checkout time

