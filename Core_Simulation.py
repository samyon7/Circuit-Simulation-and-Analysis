import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

class CircuitComponent:
    """Base class for circuit components"""
    def __init__(self, value):
        self.value = value

class Resistor(CircuitComponent):
    """Represents a resistor"""
    def __init__(self, resistance):
      super().__init__(resistance)
    def get_current(self,voltage):
      return voltage/self.value
      
class Capacitor(CircuitComponent):
    """Represents a capacitor"""
    def __init__(self, capacitance):
       super().__init__(capacitance)
    
    def get_current(self,voltage, prev_voltage, dt):
      return self.value *(voltage-prev_voltage)/dt
      
    def get_energy(self,voltage):
      return 0.5*self.value*voltage**2


class Inductor(CircuitComponent):
  """Represents an inductor"""
  def __init__(self, inductance):
    super().__init__(inductance)
  
  def get_current(self,prev_current, voltage, dt):
      return prev_current + (voltage/self.value)*dt

  def get_energy(self,current):
     return 0.5*self.value*current**2

class Circuit:
    """Represents an RLC circuit to compute f(x, y, z)"""
    def __init__(self, R, L, C):
        self.resistor = Resistor(R)
        self.inductor = Inductor(L)
        self.capacitor = Capacitor(C)
        self.current_prev = 0.0 #used for inductor
        self.voltage_prev = 0.0 #used for capacitor

        self.time = []
        self.output = []
        self.output_voltage = []
        self.output_current = []
        self.energy_consumed_list = []


    def simulate(self, x, y_start, z_freq, t_end, dt=0.001):
      
      self.time=np.arange(0,t_end,dt)
      self.output=np.zeros_like(self.time)
      self.output_voltage = np.zeros_like(self.time)
      self.output_current = np.zeros_like(self.time)
      self.energy_consumed_list = np.zeros_like(self.time)

      for i,t in enumerate(self.time):
        y= y_start*np.exp(-t)
        z = z_freq*t
        
        #Compute f(x, y, z) based on the custom formula
        target_voltage = x * np.exp(-y) * np.cos(2*np.pi*z)  +  0.1*x*y +  (x**2)*np.sin(z)/(1+y)
        self.output[i]=target_voltage

        if i>0:
          #Update the system
          voltage_change= target_voltage-self.voltage_prev
          #capacitor current based on voltage change and capacitance
          capacitor_current= self.capacitor.get_current(target_voltage, self.voltage_prev, dt)
          #inductor current
          inductor_current = self.inductor.get_current(self.current_prev,voltage_change, dt)
          #resistor current based on resistor voltage
          resistor_current= self.resistor.get_current(target_voltage)
          
          total_current = capacitor_current + inductor_current+ resistor_current
          self.output_voltage[i]=target_voltage
          self.output_current[i]=total_current
          
          self.current_prev = inductor_current
          self.voltage_prev=target_voltage
          #calculate energy
          cap_energy= self.capacitor.get_energy(target_voltage)
          inductor_energy= self.inductor.get_energy(inductor_current)
          #energy lost in resistor
          resistor_energy= target_voltage* resistor_current*dt
          self.energy_consumed_list[i]= cap_energy+ inductor_energy+ resistor_energy
        else:
          self.output_voltage[i]=target_voltage
    
    def calculate_energy_efficiency(self):
      total_energy_in = np.sum(self.output)*np.mean(np.diff(self.time))
      total_energy_out = np.sum(self.energy_consumed_list)
      if total_energy_in>0:
        return total_energy_out / total_energy_in
      else:
        return 0
    
    def landauer_limit(self, temperature, bits=1):
        k_b = 1.38e-23  # Boltzmann constant
        return bits * k_b * temperature * np.log(2)
      

# Example Usage
R = 100  # Ohms
L = 1e-3  # Henry
C = 1e-6  # Farad

my_circuit = Circuit(R, L, C)

x = 1.0    # Energy input (Joules), this drives the output voltage
y_start= 5 # Initial decay factor
z_freq = 1   # Frequency of the periodic signal (Hz)
t_end = 1    # Simulation time
dt = 0.001  #time step

my_circuit.simulate(x, y_start, z_freq, t_end, dt)

print(f"Total Energy Output: {np.sum(my_circuit.energy_consumed_list)}")
print(f"Total energy Input:{np.sum(my_circuit.output)*np.mean(np.diff(my_circuit.time))}")
print(f"Energy Efficiency: {my_circuit.calculate_energy_efficiency():.4f}")
landauer_energy=my_circuit.landauer_limit(300)
print(f"Landauer's Limit (at 300K): {landauer_energy:.2e} Joules/bit")

plt.figure(figsize=(10, 6))
plt.plot(my_circuit.time, my_circuit.output, label="Target Output Voltage")
plt.plot(my_circuit.time, my_circuit.output_voltage, label="Circuit Output Voltage")
plt.xlabel("Time (s)")
plt.ylabel("Voltage")
plt.title("Circuit Simulation")
plt.legend()
plt.show()


plt.figure(figsize=(10, 6))
plt.plot(my_circuit.time, my_circuit.output_current, label="Circuit Output Current")
plt.xlabel("Time (s)")
plt.ylabel("Current")
plt.title("Circuit Simulation")
plt.legend()
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(my_circuit.time, my_circuit.energy_consumed_list, label="Energy Consumed")
plt.xlabel("Time (s)")
plt.ylabel("Energy")
plt.title("Circuit Energy Consumption")
plt.legend()
plt.show()
