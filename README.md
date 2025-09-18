# DragonCurveUnfolding

Simulation of the Dragon Curve fractal unfolding step-by-step using matrix math and Pygame-CE.

## Description

Using simple 2D Matrix Transformations to make a Dragon Curve Unfolding Animation.

There are 2 Modes:
1: Automatic (uncomment line 17,18 in main.py)
2: Manual   (comment line 17,18 in main.py) (use mouse clicks to step the Unfolding)

## Installation

```bash
git clone https://github.com/FINN-2005/Dragon-Curve-Sim.git
```

Then download the ```nvidia cuda toolkit``` and change the ```12x``` to the version of cuda toolkit you download.
For example, I have the nvidia cuda 12 toolkit:

```bash
pip install numpy cupy-cuda12x python-ce 
```

## Usage

```bash
cd ./Dragon-Curve-Sim
python main.py
```