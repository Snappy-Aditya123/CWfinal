from .Lane import Lane


class Self_Service_Lane(Lane):
    def __init__(self, lane_id,lane_capacity=15):
        # Call the constructor of the parent class (Lane) with lane_type 'Slf' and the provided lane_id
        super().__init__('Slf', lane_id,lane_capacity=15)

  
