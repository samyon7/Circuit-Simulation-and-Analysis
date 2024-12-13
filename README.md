# Circuit Simulation Code Explanation
=====================================

## Introduction
---------------

This code simulates an RLC circuit and calculates the energy efficiency of the circuit. The circuit consists of a resistor, an inductor, and a capacitor. The simulation is based on a custom formula that computes the output voltage of the circuit.


## Circuit Components
---------------------

The circuit consists of three components:

*   **Resistor**: Represented by the `Resistor` class, which inherits from the `CircuitComponent` class. The resistor has a resistance value and can calculate the current flowing through it based on the voltage applied, using the formula: $I = \frac{V}{R}$.
*   **Inductor**: Represented by the `Inductor` class, which also inherits from the `CircuitComponent` class. The inductor has an inductance value and can calculate the current flowing through it based on the voltage applied and the previous current, using the formula: $I = I_{prev} + \frac{V}{L} \cdot dt$.
*   **Capacitor**: Represented by the `Capacitor` class, which inherits from the `CircuitComponent` class. The capacitor has a capacitance value and can calculate the current flowing through it based on the voltage applied and the previous voltage, using the formula: $I = C \cdot \frac{V - V_{prev}}{dt}$.


## Circuit Simulation
---------------------

The `Circuit` class represents the RLC circuit and has methods to simulate the circuit and calculate the energy efficiency. The simulation is based on the following formula: $f(x, y, z) = x \cdot e^{-y} \cdot \cos(2 \cdot \pi \cdot z) + 0.1 \cdot x \cdot y + \frac{x^2}{1 + y} \cdot \sin(z)$.


## Energy Calculation
---------------------

The energy consumed by the circuit is calculated at each time step based on the following formulas:

*   **Capacitor Energy**: $E_C = \frac{1}{2} \cdot C \cdot V^2$
*   **Inductor Energy**: $E_L = \frac{1}{2} \cdot L \cdot I^2$
*   **Resistor Energy**: $E_R = V \cdot I \cdot dt$


The total energy consumed by the circuit is the sum of the energies consumed by each component: $E_{total} = E_C + E_L + E_R$.


## Landauer's Limit
-------------------

The code also calculates Landauer's limit, which is the minimum energy required to erase one bit of information, using the formula: $E = k \cdot T \cdot \ln(2)$.


## Example Usage
-----------------

The code includes an example usage of the `Circuit` class, where an RLC circuit is simulated with the following parameters:

*   $R = 100 \, \Omega$
*   $L = 1 \cdot 10^{-3} \, H$
*   $C = 1 \cdot 10^{-6} \, F$
*   $x = 1.0 \, J$ (energy input)
*   $y_{start} = 5$ (initial decay factor)
*   $z_{freq} = 1 \, Hz$ (frequency of the periodic signal)
*   $t_{end} = 1 \, s$ (simulation time)
*   $dt = 0.001 \, s$ (time step)


The code calculates the total energy output, total energy input, energy efficiency, and Landauer's limit for the circuit.


## Plots
---------

The code generates three plots:

*   **Target Output Voltage vs. Time**: A plot of the target output voltage of the circuit over time.
*   **Circuit Output Voltage vs. Time**: A plot of the actual output voltage of the circuit over time.
*   **Circuit Output Current vs. Time**: A plot of the output current of the circuit over time.
*   **Energy Consumed vs. Time**: A plot of the energy consumed by the circuit over time.


These plots help visualize the behavior of the circuit and the energy consumption over time.


## RLC Circuit Simulation and Analysis Example

**Parameters:**
* Resistor ($R$): $100 \Omega$
* Inductor ($L$): $1 \times 10^{-3} \, H$
* Capacitor ($C$): $1 \times 10^{-6} \, F$
* Initial Input Energy ($x$): $1 \, J$
* Initial Decay Factor ($y_{start}$): $5$
* Frequency ($z_{freq}$): $1 \, Hz$
* Simulation Time ($t_{end}$): $1 \, s$
* Time Step ($dt$): $0.001 \, s$

**Target Output Voltage:**
$$V_{out}(t) = x \cdot e^{-y(t)} \cdot \cos(2 \pi z_{freq} \cdot t) + 0.1 \cdot x \cdot y(t) + \frac{x^2}{1+y(t)} \cdot \sin(z_{freq} \cdot t)$$
where
$$y(t) = y_{start}e^{-t}$$

**Component Currents:**
* **Resistor:** $I_R = \frac{V_{out}}{R}$
* **Inductor:** $I_L = I_{L,prev} + \frac{V_{out}}{L} \cdot dt$
* **Capacitor:** $I_C = C \cdot \frac{V_{out} - V_{C,prev}}{dt}$

**Component Energies:**
* **Capacitor:** $E_C = \frac{1}{2} C V_{out}^2$
* **Inductor:** $E_L = \frac{1}{2} L I_L^2$
* **Resistor:** $E_R = V_{out} \cdot I_R \cdot dt$

**Total Energy:**
$E_{total} = E_C + E_L + E_R$

**Energy Efficiency:**
$Efficiency = \frac{E_{out}}{E_{in}}$

**Landauer's Limit:**
$E_{Landauer} = k \cdot T \cdot \ln(2)$, where $k = 1.38 \times 10^{-23} \, J/K$ and $T = 298 \, K$

**Calculations:**

The provided code would compute the values at each time step and plot the results. Here's an example at specific time points for the target voltage:
*   At $t=0$: $V_{out}(0) = 0.5067 V$
*   At $t=0.1$: $V_{out}(0.1) = 0.4785V$
*   At $t=1$: $V_{out}(1) = 0.6375V$

Resistor Current at $t = 0$:
*   $I_R = 0.005067 A$
Inductor Current at $t = 0$:
*   $I_L = 0.5067 A$
Capacitor Current at $t=0$:
*   $I_C = 0.0005067 A$

Resistor Energy at $t = 0$:
*   $E_R = 0.00000000257 J$

Total Energy at $t=0$
* $E_{total} = 0.000000259 J$

**Example Efficiency**

Assuming $E_{out} = 0.5 \, J$
$Efficiency = 50\%$

**Landauer's Limit:**
$E_{Landauer} = 2.84 \times 10^{-21} \, J$

**Analysis:**

The simulation provides insights into the circuit's behavior over time. The current flowing through the different components, and the energy dissipated by each is simulated and the total efficiency of the circuit is computed. Finally the Landauer limit is computed to determine the efficiency of the circuit from an information perspective.



Just correct me if I'm wrong :')
