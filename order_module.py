import time

class OrderManagement:
    """
    Manages customer orders for Takeaway and Dine-in services.
    """
    def __init__(self):
        self.takeaway_queue = []
        self.orders = {} # Stores active orders

    def create_takeaway_order(self, order_id, items):
        """Creates an order and distributes it to the queue in < 1 second."""
        start_time = time.time()
        
        # Order details
        new_order = {
            "id": order_id,
            "items": items,
            "status": "In Preparation",
            "timestamp": time.ctime()
        }
        
        # Queue-based load-balancing distribution
        self.takeaway_queue.append(new_order)
        self.orders[order_id] = new_order
        
        execution_time = time.time() - start_time
        print(f"Takeaway Order {order_id} distributed in {execution_time:.4f} seconds.")

    def update_order_status(self, order_id, new_status):
        """Updates the status (In Preparation, Ready, Delivered)."""
        if order_id in self.orders:
            self.orders[order_id]["status"] = new_status
            print(f"Order {order_id} status updated to: {new_status}")