# Circuit Simulation

This project implements a Python-based simulation of an RLC circuit (Resistor, Inductor, Capacitor) to study its behavior under varying input conditions. The simulation calculates voltages, currents, and energy consumption over time and compares them to a target output voltage derived from a custom formula. Additionally, it estimates the energy efficiency of the circuit and computes the theoretical Landauer's Limit for energy per bit.

---

## Features

1. **Component Modeling**: Classes for resistors, capacitors, and inductors with methods to calculate current and energy.
2. **RLC Circuit Simulation**: Models the behavior of an RLC circuit with a given resistor, inductor, and capacitor.
3. **Energy Efficiency Calculation**: Evaluates the efficiency of energy conversion in the circuit.
4. **Landauer's Limit Estimation**: Calculates the theoretical minimum energy required for a single bit of computation at a given temperature.

---

## Formulas and Methods

### Resistor:
- **Ohm's Law**:
  $$ I_R = \frac{V}{R} $$
  Where:
  - \( I_R \): Current through the resistor (A)
  - \( V \): Voltage across the resistor (V)
  - \( R \): Resistance (\(\Omega\))

### Capacitor:
- **Current Calculation**:
  $$ I_C = C \cdot \frac{(V_{\text{new}} - V_{\text{prev}})}{\Delta t} $$
  Where:
  - \( I_C \): Current through the capacitor (A)
  - \( C \): Capacitance (F)
  - \( V_{\text{new}}, V_{\text{prev}} \): Current and previous voltages (V)
  - \( \Delta t \): Time step (s)

- **Stored Energy**:
  $$ E_C = \frac{1}{2} C \cdot V^2 $$
  Where:
  - \( E_C \): Energy stored in the capacitor (J)

### Inductor:
- **Current Calculation**:
  $$ I_L = I_{\text{prev}} + \frac{V}{L} \cdot \Delta t $$
  Where:
  - \( I_L \): Current through the inductor (A)
  - \( L \): Inductance (H)
  - \( V \): Voltage across the inductor (V)

- **Stored Energy**:
  $$ E_L = \frac{1}{2} L \cdot I^2 $$
  Where:
  - \( E_L \): Energy stored in the inductor (J)

### Target Voltage Formula:
The target output voltage is derived using the formula:
$$ V_{\text{target}} = x \cdot e^{-y} \cdot \cos(2 \pi z) + 0.1 \cdot x \cdot y + \frac{x^2 \cdot \sin(z)}{1 + y} $$
Where:
- \( x \): Input energy factor
- \( y \): Decay factor
- \( z \): Periodic signal factor (\( z = z_{\text{freq}} \cdot t \))

### Energy Efficiency:
The energy efficiency of the circuit is calculated as:
$$ \eta = \frac{E_{\text{out}}}{E_{\text{in}}} $$
Where:
- \( E_{\text{out}} \): Total energy consumed by circuit components (J)
- \( E_{\text{in}} \): Total input energy (J)

### Landauer's Limit:
Landauer's limit provides the theoretical minimum energy for a single bit of computation:
$$ E_{\text{Landauer}} = k_B \cdot T \cdot \ln(2) $$
Where:
- \( k_B \): Boltzmann constant (\(1.38 \times 10^{-23}\, J/K\))
- \( T \): Temperature in Kelvin (K)

---

## Classes

### 1. `CircuitComponent` (Base Class)
Represents a general circuit component with a common `value` attribute (e.g., resistance, capacitance, or inductance).

### 2. `Resistor`
- **Methods**:
  - `get_current(voltage)`: Computes current using Ohm's law.

### 3. `Capacitor`
- **Methods**:
  - `get_current(voltage, prev_voltage, dt)`: Computes the current based on voltage changes.
  - `get_energy(voltage)`: Computes the energy stored in the capacitor.

### 4. `Inductor`
- **Methods**:
  - `get_current(prev_current, voltage, dt)`: Updates the current based on voltage and time.
  - `get_energy(current)`: Computes the energy stored in the inductor.

### 5. `Circuit`
- Simulates the RLC circuit and computes output voltage, current, and energy consumed over time.
- **Methods**:
  - `simulate(x, y_start, z_freq, t_end, dt)`: Simulates the circuit behavior.
  - `calculate_energy_efficiency()`: Computes the circuit's energy efficiency.
  - `landauer_limit(temperature, bits)`: Computes the Landauer's limit for energy per bit.

---

## Example Usage
```python
R = 100  # Ohms
L = 1e-3  # Henry
C = 1e-6  # Farad

my_circuit = Circuit(R, L, C)

x = 1.0    # Energy input (Joules), drives output voltage
y_start = 5  # Initial decay factor
z_freq = 1   # Frequency of the periodic signal (Hz)
t_end = 1    # Simulation time (s)
dt = 0.001   # Time step (s)

my_circuit.simulate(x, y_start, z_freq, t_end, dt)

print(f"Total Energy Output: {np.sum(my_circuit.energy_consumed_list)}")
print(f"Total Energy Input: {np.sum(my_circuit.output) * np.mean(np.diff(my_circuit.time))}")
print(f"Energy Efficiency: {my_circuit.calculate_energy_efficiency():.4f}")
landauer_energy = my_circuit.landauer_limit(300)
print(f"Landauer's Limit (at 300K): {landauer_energy:.2e} Joules/bit")
```

---

## Visualization
The script generates three plots to analyze the circuit's behavior:

1. **Target and Output Voltage**:
   - Shows the desired target voltage and the actual output voltage of the circuit over time.

2. **Output Current**:
   - Displays the circuit's output current over time.

3. **Energy Consumption**:
   - Depicts the energy consumed by the circuit over time.

---

## Dependencies
- `numpy`
- `matplotlib`
- `scipy`

Install the dependencies using:
```bash
pip install numpy matplotlib scipy
```

---

## License
This project is released under the MIT License.

