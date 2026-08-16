# Hofstra Department of Computer Science Open House Demos

Welcome! 👋 This repository contains interactive Artificial Intelligence (AI) and Machine Learning demonstrations created for the **Hofstra University Department of Computer Science Open House**.

Even if you have never written a line of Python before, this guide will walk you step-by-step through setting up and running these demos on your computer!

---

## 🌟 What's in this Repository?

1. **🤖 Agentic AI Demos (`/agentic`)**
   - Run a 100% private, local Large Language Model (LLM) on your machine using **Ollama**.
   - Interact with chatbots via a web interface built with **Gradio**.
   - Meet **DJ Krakenbeard**, a pirate-themed AI agent that can control your local music playback using **VLC**!

2. **🎨 AI Image Generator (`/image_gen`)**
   - Generate high-resolution artwork from text descriptions using **Stable Diffusion XL**.

---

## 🛠️ Step 1: Install the Prerequisites

Before running the code, you'll need a few free tools installed on your computer:

### 1. Python (Programming Language)
- Download and install **Python 3.10, 3.11, or 3.12** from [python.org](https://www.python.org/downloads/).
- ⚠️ **IMPORTANT (Windows Users):** During installation, make sure to check the box that says **"Add python.exe to PATH"** before clicking Install.

### 2. Ollama (Runs Local AI Models)
- Download and install **Ollama** from [ollama.com](https://ollama.com/download).
- Once installed, open your computer's terminal (Command Prompt or PowerShell on Windows, Terminal on Mac/Linux) and download the lightweight AI model used in our demos:
  ```bash
  ollama run gemma4:e2b
  ```
  *(Once it finishes downloading, you can type `/bye` to exit the chat prompt. Ollama will keep running in the background).*

### 3. VLC Media Player (Required for the Music Agent)
- Download and install the standard 64-bit version of **VLC media player** from [videolan.org](https://www.videolan.org/vlc/).
- *Note:* The Python music script connects directly to VLC to play songs.

### 4. Download This Repository
- **Option A (With Git):** Open your terminal and run:
  ```bash
  git clone https://github.com/your-username/demos_august_2026.git
  cd demos_august_2026
  ```
- **Option B (Without Git):** Click the green **Code** button at the top of this GitHub page, select **Download ZIP**, extract the folder, and open a terminal inside that folder.

---

## 🚀 Step 2: Running the Agentic AI & DJ Demos (`/agentic`)

### 1. Open Terminal in the `agentic` folder
Navigate into the `agentic` folder:
```bash
cd agentic
```

### 2. (Recommended) Create a Python Virtual Environment
A virtual environment keeps project dependencies organized and isolated:
```bash
# Create the virtual environment
python -m venv venv

# Activate it:
# On Windows (PowerShell):
.\venv\Scripts\Activate.ps1
# On Windows (Command Prompt):
.\venv\Scripts\activate.bat
# On Mac/Linux:
source venv/bin/activate
```

### 3. Install the Dependencies
Install all required libraries using the provided requirements file:
```bash
pip install -r requirements.txt
```

### 4. Choose a Demo to Run!

#### Demo A: Simple Local Chatbot
```bash
python simplechat.py
```
- Open your web browser and go to `http://127.0.0.1:7860`.
- Chat with the local AI running directly on your laptop/desktop!

#### Demo B: Chat with DJ Krakenbeard (Pirate Persona)
```bash
python chat_with_personality.py
```
- Open `http://127.0.0.1:7860` to talk to DJ Krakenbeard.

#### Demo C: Interactive Music DJ Agent
1. Create a folder named `my_music` inside the `agentic` directory (or let the script create it for you).
2. Copy a few `.mp3` or `.wav` music files into `agentic/my_music/`.
3. Start the agent:
   ```bash
   python chat_with_music.py
   ```
4. Open `http://127.0.0.1:7860` and try asking:
   - *"What songs do you have in your library?"*
   - *"Play [song name]"*
   - *"Pause the music"*
   - *"Stop"*

---

## 🎨 Step 3: Running the AI Image Generator (`/image_gen`)

> 💡 **Note on Hardware:** Stable Diffusion XL works best on computers with a dedicated NVIDIA graphics card (GPU with 8GB–16GB+ VRAM).

### 1. Navigate to the `image_gen` folder
```bash
cd ../image_gen
```

### 2. Install Image Generation Dependencies
```bash
pip install -r requirements.txt
```
*(If using an NVIDIA GPU, make sure you have PyTorch with CUDA enabled by visiting [pytorch.org](https://pytorch.org/get-started/locally/)).*

### 3. Generate an Image
Run the script with a prompt describing what you want to generate:
```bash
python generate.py "a corgi wearing a graduation cap, oil painting style"
```
- The first time you run this, it will automatically download the Stable Diffusion model weights.
- When finished, the generated image will be saved as **`output.png`** in the `image_gen` folder!

---

## ❓ Frequently Asked Questions & Troubleshooting

- **`'python' is not recognized as an internal or external command`**:
  Re-run the Python installer and ensure **"Add Python to PATH"** is checked.
- **`Execution loop logging: ... Connection refused`**:
  Make sure Ollama is running in your system tray or run `ollama serve` in a separate terminal.
- **`FileNotFoundError` or VLC Error in the Music Demo**:
  Ensure VLC Media Player (64-bit) is installed on your machine and that you placed `.mp3` or `.wav` files inside the `agentic/my_music` folder.
- **To stop any running program**:
  Press `Ctrl + C` in your terminal window.

---

## 🎓 Learn More About Computer Science at Hofstra
Interested in studying Computer Science, Software Engineering, Cybersecurity, or Artificial Intelligence?
- Visit the [Hofstra Department of Computer Science](https://www.hofstra.edu/computer-science/) for degree programs, research opportunities, and student clubs!
