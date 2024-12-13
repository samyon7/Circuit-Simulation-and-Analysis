# Circuit Simulation 
=====================================

## Introduction
---------------

This code simulates an RLC circuit and calculates the energy efficiency of the circuit. The circuit consists of a resistor, an inductor, and a capacitor. The simulation is based on a custom formula that computes the output voltage of the circuit.

## Circuit Components
---------------------

The circuit consists of three components:

*   **Resistor**: Represented by the `Resistor` class, which inherits from the `CircuitComponent` class. The resistor has a resistance value and can calculate the current flowing through it based on the voltage applied.
*   **Inductor**: Represented by the `Inductor` class, which also inherits from the `CircuitComponent` class. The inductor has an inductance value and can calculate the current flowing through it based on the voltage applied and the previous current.
*   **Capacitor**: Represented by the `Capacitor` class, which inherits from the `CircuitComponent` class. The capacitor has a capacitance value and can calculate the current flowing through it based on the voltage applied and the previous voltage.

## Circuit Simulation
---------------------

The `Circuit` class represents the RLC circuit and has methods to simulate the circuit and calculate the energy efficiency. The simulation is based on the following formula:

"f(x, y, z) = x \* exp(-y) \* cos(2 \* π \* z) + 0.1 \* x \* y + (x^2) \* sin(z) / (1 + y)"

Where:

*   x is the energy input
*   y is the decay factor
*   z is the frequency of the periodic signal

The simulation calculates the output voltage of the circuit at each time step based on this formula.

## Energy Calculation
---------------------

The energy consumed by the circuit is calculated at each time step based on the following formulas:

*   **Capacitor Energy**: "0.5 \* C \* V^2"
*   **Inductor Energy**: "0.5 \* L \* I^2"
*   **Resistor Energy**: "V \* I \* dt"

Where:

*   C is the capacitance
*   V is the voltage across the capacitor
*   L is the inductance
*   I is the current flowing through the inductor
*   dt is the time step

The total energy consumed by the circuit is the sum of the energies consumed by each component.

## Landauer's Limit
-------------------

The code also calculates Landauer's limit, which is the minimum energy required to erase one bit of information. The formula for Landauer's limit is:

"E = k \* T \* ln(2)"

Where:

*   E is the energy required to erase one bit
*   k is the Boltzmann constant
*   T is the temperature in Kelvin

## Example Usage
-----------------

The code includes an example usage of the `Circuit` class, where an RLC circuit is simulated with the following parameters:

*   R = 100 Ohms
*   L = 1e-3 Henry
*   C = 1e-6 Farad
*   x = 1.0 Joules (energy input)
*   y_start = 5 (initial decay factor)
*   z_freq = 1 Hz (frequency of the periodic signal)
*   t_end = 1 second (simulation time)
*   dt = 0.001 seconds (time step)

The code calculates the total energy output, total energy input, energy efficiency, and Landauer's limit for the circuit.

## Plots
---------

The code generates three plots:

*   **Target Output Voltage vs. Time**: A plot of the target output voltage of the circuit over time.
*   **Circuit Output Voltage vs. Time**: A plot of the actual output voltage of the circuit over time.
*   **Circuit Output Current vs. Time**: A plot of the output current of the circuit over time.
*   **Energy Consumed vs. Time**: A plot of the energy consumed by the circuit over time.

These plots help visualize the behavior of the circuit and the energy consumption over time.
