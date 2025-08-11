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

    def test_customer_uses_regular_lane_when_self_service_unavailable(self):
        lane_manager = Lane_Management()
        lanes = lane_manager.set_up_lanes()
        # close self-service lane to force fallback
        for lane in lanes:
            if lane.lane_type == 'Slf':
                lane.close_lane()
        customer = Customer(identifier="Test")
        customer.basket._size = 5
        selected_lane = lane_manager.move_lane(lanes, customer)
        self.assertIsNotNone(selected_lane)
        self.assertEqual(selected_lane.lane_type, 'Reg')

    def test_display_lane_status_closed(self):
        lane = Regular_Lane(1)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            lane.display_lane_status()
            self.assertIn('closed', fake_out.getvalue())

    def test_simulation_state_snapshot(self):
        sim = Simulation()
        lane = Regular_Lane(1)
        lane.open_lane()
        customer = Customer(identifier='X')
        lane.add_customer(customer)
        sim.lanes = [lane]
        state = sim.get_lane_states()
        self.assertEqual(state[0]['customers'], ['X'])

    # Add more integration test cases based on specific interactions in your system.

if __name__ == '__main__':
    unittest.main()
