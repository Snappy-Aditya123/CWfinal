**Checkout Simulation System Documentation**

---

**1. Introduction:**
   The Checkout Simulation System is a Python program that simulates the operation of multiple checkout lanes in a retail setting. It models the interaction between customers, their shopping baskets, and the checkout lanes. The system includes regular and self-service lanes, each with its specific capacity and processing times. The simulation aims to mimic a realistic shopping environment with customers joining lanes based on their basket sizes.

---

**2. Classes:**

**2.1 Basket:**
   - Represents a shopping basket with a randomly generated size.
   - Method:
     - `get_size()`: Returns the size of the basket.

**2.2 Customer:**
   - Represents a customer with a unique identifier, a shopping basket, and the possibility of winning a lottery ticket.
   - Methods:
     - `get_basket_size()`: Returns the size of the customer's basket.
     - `get_checkout_time(is_self_service)`: Calculates the estimated checkout time based on the type of lane.
     - `award_lottery_ticket()`: Returns whether the customer wins a lottery ticket.
     - `display_customer_details(is_self_service)`: Displays customer details.
     - `checkout()`: Simulates the customer checking out and returns the checkout time.

**2.3 CheckoutLane:**
   - Represents a general checkout lane with a specified capacity and list of customers.
   - Methods:
     - `add_customer(customer)`: Adds a customer to the lane if there is space.
     - `remove_customer(customer)`: Removes a customer from the lane.
     - `open_lane()`: Opens the lane for customer service.
     - `close_lane()`: Closes the lane.
     - `display_lane_status()`: Displays the lane status.
     - `get_lane_capacity()`: Returns the capacity of the lane.
     - `process_customers()`: Processes customers in the lane.

**2.4 RegularLane:**
   - Subclass of CheckoutLane representing a regular checkout lane.

**2.5 SelfServiceLane:**
   - Subclass of CheckoutLane representing a self-service checkout lane.

---

**3. Functions:**

**3.1 set_up_lanes():**
   - Initializes regular and self-service lanes, opens the first and last lanes, and returns a list of lanes.

**3.2 initiate_simulation(lanes):**
   - Initiates the simulation by taking user input for the simulation duration.
   - Calls functions to assign customers to lanes and run the simulation.

**3.3 generate_random_customers(lanes, max_customers):**
   - Generates a random number of customers and assigns them to lanes.

**3.4 assign_customers_to_lanes(lanes, num_customers):**
   - Assigns customers to lanes based on their basket sizes.

**3.5 move_lane(lanes, customer):**
   - Determines the appropriate lane for a customer based on their basket size.

**3.6 get_self_service_lane(lanes):**
   - Returns an open self-service lane if available.

**3.7 get_regular_lane(lanes):**
   - Returns an open regular lane or opens a closed one if all regular lanes are full.

**3.8 get_total_customers(lanes):**
   - Returns the total number of customers across all lanes.

**3.9 run_simulation(lanes, simulation_duration_seconds, time_interval_seconds, max_customers):**
   - Runs the simulation for the specified duration with a time interval.
   - Displays lane statuses, generates random customers, processes customers, and manages lanes.

**3.10 process_customers_in_lanes(lanes):**
    - Processes customers in each lane and awards lottery tickets if eligible.

**3.11 award_lottery_ticket_if_eligible(customer):**
    - Awards a lottery ticket to the customer if eligible.

**3.12 manage_lanes(lanes):**
    - Opens or closes lanes based on the current status and the presence of customers.

**3.13 display_lane_statuses(lanes):**
    - Displays the status of each lane.

**3.14 display_all_customer_details(lanes):**
    - Displays details of all customers after the simulation.

**3.15 end_simulation():**
    - Displays the end timestamp of the simulation.

---

**4. Execution:**
   - The main execution block sets up lanes, initiates the simulation, and displays customer details after the simulation. Every event is shown When there is a change in the state of the simulation.

---

**5. Conclusion:**
   The Checkout Simulation System provides a flexible and extensible framework for simulating customer interactions in a retail checkout environment. Users can adjust parameters such as simulation duration, time intervals, and lane capacities to observe different scenarios. The system aims to mimic real-world checkout operations, providing insights into lane efficiency and customer experiences.

---

**6. Web Interface:**
   - A simple Flask-based interface is included for visual control of the simulation.
   - Run `python web_app.py` and open `http://localhost:5000` in a browser.
   - The page allows setting the simulation duration and number of initial customers with buttons to start or stop the run.
