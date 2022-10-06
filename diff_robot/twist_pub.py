import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from geometry_msgs.msg import Twist
import yaml


class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('twist_pub')
        self.publisher_ = self.create_publisher(Twist, 'model/vehicle_blue/cmd_vel', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0
        with open("/home/maverick/upwork/diff_sim_ws/src/diff_robot/config/commands.yaml", "r") as stream:
            try:
                self.commands = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)

    def timer_callback(self):
        
        msg = Twist()
        msg.linear.x = 0.5
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg)
        self.i += 1


def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()