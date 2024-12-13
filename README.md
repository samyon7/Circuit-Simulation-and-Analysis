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
