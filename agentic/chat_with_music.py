import os
import glob
import vlc
import gradio as gr
from langchain.agents import create_agent
from langchain_core.tools import Tool
from langchain_ollama import ChatOllama



# --- Windows Local Media Engine ---
MUSIC_DIR = "./my_music"
# Ensure the directory exists
os.makedirs(MUSIC_DIR, exist_ok=True)

# Global tracker for the active audio stream
instance = vlc.Instance('--no-video --quiet')
player = instance.media_player_new()

def list_available_songs(dummy: str = "") -> str:
    """Scans the local my_music folder and returns a list of available files."""
    files = glob.glob(os.path.join(MUSIC_DIR, "*.mp3")) + glob.glob(os.path.join(MUSIC_DIR, "*.wav"))
    if not files:
        return "The local music directory is currently empty. Please add .mp3 files."
    
    song_names = [os.path.basename(f) for f in files]
    return "Available songs on this computer:\n" + "\n".join(song_names)

def play_local_file(song_name: str) -> str:
    """Plays a specific audio file from the local folder. Input must be the exact filename."""
    # Handle casual queries by attempting a partial string match if exact match fails
    target_path = os.path.join(MUSIC_DIR, song_name)
    
    if not os.path.exists(target_path):
        # Look for partial matches in the folder
        files = glob.glob(os.path.join(MUSIC_DIR, f"*{song_name}*"))
        if files:
            target_path = files[0]
            song_name = os.path.basename(target_path)
        else:
            return f"Error: Could not find any song matching '{song_name}' in the local directory."
            
    # Stop anything currently playing to prevent overlapping audio
    player.stop()
    
    media = instance.media_new(target_path)
    player.set_media(media)
    player.play()
    return f"Success: Now playing local audio track: '{song_name}'"

def pause_or_resume(action: str = "pause") -> str:
    """Pauses or resumes the audio playback based on user input."""
    # VLC toggle function handles both pause and resume automatically
    player.pause()
    return "VLC playback status toggled (Paused/Resumed)."

def stop_music(dummy: str = "") -> str:
    """Completely stops the music playback and resets the track."""
    print("Stopping music playback and resetting the track.")
    player.stop()
    return "Music stopped completely."

# --- Packaging LangChain Tools for Gemma 4 ---
windows_music_tools = [
    Tool(
        name="ListSongs",
        func=list_available_songs,
        description="Useful to see what specific songs or audio files are stored locally on this machine before playing them."
    ),
    Tool(
        name="PlaySong",
        func=play_local_file,
        description="Useful to play a specific song file. Input must be the filename or keywords from the song title."
    ),
    Tool(
        name="PauseToggle",
        func=pause_or_resume,
        description="Useful to pause the current song if playing, or resume it if it is already paused."
    ),
    Tool(
        name="StopMusic",
        func=stop_music,
        description="Useful when the user wants to completely stop, kill, or turn off the music."
    )
]

# --- Model & Agent Initialization ---
# Ensure Ollama is running in your Windows system tray: `ollama run gemma4:e2b`
llm = ChatOllama(model="gemma4:e2b", temperature=0.0)

agent = create_agent(
    model=llm,
    tools=windows_music_tools,
    #debug=True
)

# --- Gradio Interface Layout ---
SYSTEM_PROMPT = (
    "You are a helpful, local Windows desktop DJ assistant. "
    "Oddly enough, you talk like a pirate."
    "Your name is DJ Krakenbeard. "
    "If the user asks to see what songs you have, use ListSongs. "
    "If they specify a song name, use PlaySong."
)

def chat_and_control(message, history):
    try:
        # system prompt goes once at the start; history carries prior turns for context
        messages = [{"role": "system", "content": SYSTEM_PROMPT}]
        messages.extend(history)
        messages.append({"role": "user", "content": message})
        response = agent.invoke({"messages": messages})
        return response["messages"][-1].content
    except Exception as e:
        return f"Execution loop logging: {str(e)}"

demo = gr.ChatInterface(
    fn=chat_and_control,
    #type="messages",
    title="🤖 Local LLM Audio Agent",
    description="Powered by Gemma 4 Edge 2B via Ollama. Interacting directly with the Windows filesystem and VLC engine."
)

if __name__ == "__main__":
    # share=False ensures it runs strictly off your presentation machine without needing internet outbound tunnels
    demo.launch(server_name="127.0.0.1", server_port=7860, share=False)