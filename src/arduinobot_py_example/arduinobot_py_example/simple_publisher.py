import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class Simple_publisher(Node):

    def __init__(self):
        super().__init__("simple_publisher")
        self.pub_ = self.create_publisher(String, "chatter", 10)
        self.counter = 0
        self.frequency_ = 1.0

        self.get_logger().info(f"Publishing at {self.frequency_} Hz")
        self.time_ = self.create_timer(self.frequency_, self.timerCallback)

    
    def timerCallback(self):
        msg = String()
        msg.data = f"Hello ros2 - counter {self.counter}"
        self.pub_.publish(msg)
        self.counter += 1



def main():
    rclpy.init()
    simple_publisher = Simple_publisher()
    rclpy.spin(simple_publisher)
    simple_publisher.destroy_node
    rclpy.shutdown()

    
if __name__ == '__main__':
    main()