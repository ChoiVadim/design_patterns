"""
State Pattern - Traffic Light Example
Real-world usage: Embedded systems, IoT devices, automation, workflow management
"""

from abc import ABC, abstractmethod
import time


class TrafficLightState(ABC):
    """State interface for traffic light"""
    
    @abstractmethod
    def handle(self, traffic_light):
        """Handle state behavior"""
        pass
    
    @abstractmethod
    def get_duration(self) -> int:
        """Get state duration in seconds"""
        pass
    
    @abstractmethod
    def get_color(self) -> str:
        """Get light color"""
        pass


class RedState(TrafficLightState):
    """Red light state"""
    
    def handle(self, traffic_light):
        print("🔴 RED LIGHT - STOP")
        print("   All vehicles must stop")
        time.sleep(1)  # Simulate duration
        # Transition to next state
        traffic_light.set_state(GreenState())
    
    def get_duration(self) -> int:
        return 30  # Red light lasts 30 seconds
    
    def get_color(self) -> str:
        return "RED"


class YellowState(TrafficLightState):
    """Yellow light state"""
    
    def handle(self, traffic_light):
        print("🟡 YELLOW LIGHT - CAUTION")
        print("   Prepare to stop")
        time.sleep(1)  # Simulate duration
        # Transition to next state
        traffic_light.set_state(RedState())
    
    def get_duration(self) -> int:
        return 5  # Yellow light lasts 5 seconds
    
    def get_color(self) -> str:
        return "YELLOW"


class GreenState(TrafficLightState):
    """Green light state"""
    
    def handle(self, traffic_light):
        print("🟢 GREEN LIGHT - GO")
        print("   Vehicles may proceed")
        time.sleep(1)  # Simulate duration
        # Transition to next state
        traffic_light.set_state(YellowState())
    
    def get_duration(self) -> int:
        return 25  # Green light lasts 25 seconds
    
    def get_color(self) -> str:
        return "GREEN"


class TrafficLight:
    """Context class that uses traffic light states"""
    
    def __init__(self):
        self._state = RedState()
        self._cycle_count = 0
    
    def set_state(self, state: TrafficLightState):
        """Change state"""
        self._state = state
    
    def get_state(self) -> TrafficLightState:
        """Get current state"""
        return self._state
    
    def change_state(self):
        """Change to next state"""
        self._state.handle(self)
    
    def start(self, cycles: int = 3):
        """Start traffic light cycle"""
        print("=" * 60)
        print("Traffic Light System Starting")
        print("=" * 60)
        print()
        
        for cycle in range(cycles):
            self._cycle_count = cycle + 1
            print(f"--- Cycle {self._cycle_count} ---")
            
            # Run through all states
            for _ in range(3):  # Red -> Green -> Yellow -> Red
                color = self._state.get_color()
                duration = self._state.get_duration()
                print(f"\n[{color}] Duration: {duration}s")
                self.change_state()
                print()
            
            if cycle < cycles - 1:
                print("-" * 60)
                print()
        
        print("=" * 60)
        print("Traffic Light System Stopped")
        print("=" * 60)


# Example usage
if __name__ == "__main__":
    print("=" * 60)
    print("State Pattern - Traffic Light Example")
    print("=" * 60)
    print()
    
    traffic_light = TrafficLight()
    
    # Run traffic light for 2 cycles
    traffic_light.start(cycles=2)
    
    print()
    print("=" * 60)
    print("Key Benefit: Each state knows its own behavior and")
    print("next state, making state transitions clear and maintainable!")
    print("=" * 60)

