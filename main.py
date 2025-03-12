import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import trimesh
import numpy as np
import cv2
import mediapipe as mp
import random

# Initialize Pygame
pygame.init()
pygame.mixer.init()  # Initialize audio

# Load Sound Effects
greeting_sound = pygame.mixer.Sound("greeting.mp3")  # Greeting audio
assemble_sound = pygame.mixer.Sound("nano_assemble.mp3")  # Nanoparticle assembly audio

# Play Greeting Sound at Startup
pygame.mixer.Sound.play(greeting_sound)

# Window Settings
WINDOW_WIDTH, WINDOW_HEIGHT = 1600, 1000
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), DOUBLEBUF | OPENGL)
pygame.display.set_caption("Iron Man Hologram Projection")

# OpenGL Settings
glEnable(GL_BLEND)
glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
glEnable(GL_DEPTH_TEST)
glEnable(GL_LINE_SMOOTH)
glHint(GL_LINE_SMOOTH_HINT, GL_NICEST)

# Load Iron Man Model
model_path = "IronMan.obj"
mesh = trimesh.load(model_path, force='mesh')
mesh.apply_scale(0.07)
mesh.apply_translation(-mesh.centroid)

vertices = np.array(mesh.vertices, dtype=np.float32)
faces = np.array(mesh.faces, dtype=np.uint32)

# Generate Nanobot Particles
nanobot_particles = np.random.uniform(-10, 10, (len(vertices), 3))
assembly_progress = 0.0

# Hand Tracking Setup
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5)
cap = cv2.VideoCapture(0)

# Perspective & View
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
gluPerspective(60, (WINDOW_WIDTH / WINDOW_HEIGHT), 0.1, 2000.0)
glMatrixMode(GL_MODELVIEW)
glLoadIdentity()
glTranslatef(0.0, -2.5, -40)

# Camera Controls
angle_x, angle_y = 0, 0
zoom = -18
assembly = False


def draw_nanobot_assembly():
    global assembly_progress, assembly
    if assembly:
        assembly_progress = min(assembly_progress + 0.02, 1.0)
    else:
        assembly_progress = max(assembly_progress - 0.02, 0.0)

    positions = (1 - assembly_progress) * nanobot_particles + assembly_progress * vertices
    glBegin(GL_POINTS)
    glColor4f(0.0, 1.0, 1.0, 0.5)
    for pos in positions:
        glVertex3f(*pos)
    glEnd()


# Hand Gesture Rotation
def hand_gesture_control():
    global angle_y
    ret, frame = cap.read()
    if not ret:
        return

    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            angle_y = (index_tip.x - 0.5) * 180


# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_a:
                if not assembly:  # Play only if it was not already assembling
                    pygame.mixer.Sound.play(assemble_sound)
                assembly = True
            elif event.key == K_d:
                if assembly:  # Play only if it was already assembling
                    pygame.mixer.Sound.play(assemble_sound)
                assembly = False

    hand_gesture_control()

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glTranslatef(0.0, -1.5, zoom)
    glRotatef(angle_x, 1, 0, 0)
    glRotatef(angle_y, 0, 1, 0)

    draw_nanobot_assembly()

    pygame.display.flip()
    pygame.time.wait(5)  # Optimized for high FPS

cap.release()
pygame.quit()
