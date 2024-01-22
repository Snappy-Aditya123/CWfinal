import unittest
from unittest.mock import patch
from io import StringIO
from datetime import datetime, timedelta
from models import Regular_Lane, Self_Service_Lane, Customer
from Lane_Management import Lane_Management
from Simulation import Simulation

class TestIntegrationCases(unittest.TestCase):

    def test_customer_assignment_and_processing(self):
        # Test if customers are assigned to lanes and processed correctly
        lane_manager = Lane_Management()
        lanes = lane_manager.set_up_lanes()
        customers = [Customer(identifier=f"Cust{i}") for i in range(1, 6)]
        lane_manager.all_customers = customers
        lane_manager.assign_customers_to_lanes(lanes, len(customers))
        lane_manager.process_customers_in_lanes(lanes)
      

    def test_lanes_open_close_management(self):
        # Test if lanes are opened and closed based on the number of customers
        lane_manager = Lane_Management()
        lanes = lane_manager.set_up_lanes()
        customers = [Customer(identifier=f"Cust{i}") for i in range(1, 6)]
        lane_manager.all_customers = customers
        lane_manager.assign_customers_to_lanes(lanes, len(customers))
        lane_manager.manage_lanes(lanes)
      
        

    def test_award_lottery_tickets(self):
        # Test if lottery tickets are awarded to eligible customers
        lane_manager = Lane_Management()
        lanes = lane_manager.set_up_lanes()
        customers = [Customer(identifier=f"Cust{i}") for i in range(1, 6)]
        lane_manager.all_customers = customers
        lane_manager.assign_customers_to_lanes(lanes, len(customers))
        lane_manager.process_customers_in_lanes(lanes)
        self.assertTrue(any(customer.award_lottery_ticket() for customer in lane_manager.all_customers))

    # Add more integration test cases based on specific interactions in your system.

if __name__ == '__main__':
    unittest.main()
