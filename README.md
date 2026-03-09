# 2D Gas Particle Simulation

A physics-based simulation of gas particles in a 2D container designed to explore models from kinetic theory and statistical mechanics.

The project models particle dynamics using progressively more realistic interaction models, starting from idealized elastic collisions and moving toward intermolecular forces and chemical reactions.

---

## Current Status

🚧 **Work in progress**

The **hard sphere model** is currently being implemented and is close to completion.

---

## Models in the Project

### 1. Hard Sphere Model (Current Implementation)

Particles are treated as perfectly rigid spheres that interact only through **elastic collisions** with each other and the container walls.

**Features:**

- Particle motion in a 2D box
- Elastic particle–particle collisions
- Elastic wall collisions
- Energy and momentum conservation

---

### 2. Soft Sphere Model (Planned)

Particles interact through **intermolecular forces** rather than instantaneous collisions.

**Planned features:**

- Continuous force-based interactions
- Potential models (e.g., Lennard-Jones–type interactions)
- Numerical integration for particle dynamics
- Emergent gas behavior

---

### 3. Chemical Reaction Simulation (Planned)

A specialized simulation where particles can **react upon interaction** under defined conditions.

**Possible features:**

- Reaction probability on collision
- Conversion of particle types
- Tracking concentration changes over time
- Reaction dynamics visualization

---

## Goals of the Project

- Explore computational models of gas behavior
- Implement progressively more realistic particle interactions
- Study emergent phenomena such as distributions and reaction dynamics
- Build a flexible simulation framework for experimenting with particle systems

---

## Future Work

- Velocity distribution analysis
- Temperature and pressure estimation
- Visualization improvements
- Performance optimization