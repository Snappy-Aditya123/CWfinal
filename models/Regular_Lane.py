from .Lane import Lane



# Regular_Lane class represents a regular checkout lane.
# It inherits from the Lane class and sets its lane_type to 'Reg'.
class Regular_Lane(Lane):
    def __init__(self, lane_id, lane_capacity=5):
        # Call the constructor of the parent class (Lane) with 'Reg' lane_type and the provided lane_id.
        super().__init__('Reg', lane_id, lane_capacity)

    
