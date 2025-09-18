import pygame
from pygame import Vector2 as V2
from math import radians, sin, cos, sqrt, pow
import numpy as np
import cupy as cp

RES = W,H = 800,600
HW, HH = W/2, H/2

FPS = 60

pygame.init()
