# Fan Speed Controller with Emergency Shutdown

A Python script that simulates controlling the fan speed of a gaming computer based on the system's temperature. The fan adjusts dynamically as the temperature increases. If the temperature hits 100°C, the system will shut down, leaving only the fan running at MAX speed for 5 minutes to cool the system. During this time, the user is blocked from interacting with the system.

## Features

- Monitors system temperature.
- Controls fan speed with 4 levels: OFF, LOW, MEDIUM, HIGH, and MAX for critical temperatures.
- Emergency shutdown at 100°C with the fan running for 5 minutes before a complete system shutdown.

## Fan Speed Control

| Temperature Range  | Fan Speed  |
|--------------------|------------|
| Below 40°C         | OFF        |
| 40°C to 59°C       | LOW        |
| 60°C to 79°C       | MEDIUM     |
| 80°C to 99°C       | HIGH       |
| 100°C              | MAX (System shutdown, fan runs for 5 minutes) |

## Emergency Shutdown

If the temperature hits 100°C:
- The system halts all operations except for the fan.
- The fan will run at MAX speed for 5 minutes to cool the system.
- After cooling, the fan will shut down, and the system will require a restart.

## Prerequisites

- Python 3.x

## How to Run

1. Clone the repository.
   ```bash
   git clone https://github.com/yourusername/fan-speed-controller.git
   cd fan-speed-controller
