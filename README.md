# Iron Man Hologram Projection

## Description
This project is a **real-time 3D hologram projection** of an Iron Man suit, inspired by the movies. It features an interactive, animated model with nanoparticle assembly, gesture-based control, dynamic UI elements, and immersive audio effects.

## Features
- **Holographic Iron Man Model**: A realistic 3D rendering of Iron Man's suit.
- **Nanoparticle Assembly & Disassembly**: The suit assembles/disassembles in response to key commands (`A` and `D`).
- **Hand Gesture Rotation**: Rotate the model using webcam-based hand tracking.
- **Dynamic UI Elements**: Includes radar scans, HUD indicators, and power level displays.
- **Foggy Navy Blue Background**: Enhances the holographic effect.
- **Audio Integration**:
  - Greeting audio plays when the project starts.
  - Nanoparticle assembly and disassembly have dedicated sound effects.
- **Steel Frame Assembly**: The model first appears as a structured exoskeleton before forming completely.

## Installation
### Prerequisites
Ensure you have the following dependencies installed:

```sh
pip install pygame PyOpenGL trimesh numpy opencv-python mediapipe
```

### Running the Project
1. Download the project files, including the `IronMan.obj` model and required sound files.
2. Run the script:
   ```sh
   python main.py
   ```
3. Use the following controls:
   - **Press `A`** to start nanoparticle assembly.
   - **Press `D`** to disassemble the suit.
   - **Use hand gestures** to rotate the model.

## Future Enhancements
- **Advanced Gesture Controls**: Use hand tracking to trigger additional UI interactions.
- **Voice Commands**: Implement AI voice recognition for a more J.A.R.V.I.S.-like experience.
- **Augmented Reality Mode**: Enable projection on AR-compatible devices.

## Credits
- Developed by **AdityOo**
- Inspired by **Marvel's Iron Man**
- Built using **Python, OpenGL, and Pygame**

---
This is a **passion project**, designed to bring a cinematic experience to life through programming. 🚀

