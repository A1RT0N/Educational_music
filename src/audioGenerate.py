from pydub import AudioSegment
from elevenlabs import Voice, VoiceSettings, generate, play
import elevenlabs
import os
def generate_voice(text):

    elevenlabs.set_api_key("2ea493ac23d40e0c936fce64d0b313c5")
    
    audio = generate(
        text=text,
        voice=Voice(
            voice_id='ZQe5CZNOzWyzPSCn5a3c', # James
            settings=VoiceSettings(stability=0.4, similarity_boost=0.3, style=0.0, use_speaker_boost=True)
        )
    )

    elevenlabs.save(audio, "audio.mp3")

    return AudioSegment.from_mp3("audio.mp3")

def gerar_audio(text):

    background_music = AudioSegment.from_mp3("./src/samples_vozes/sample0.mp3")

    # Generate voice (replace with your voice generation method)
    voice = generate_voice(text)

    # Volume adjustment
    voice = voice + 9
    background_music = background_music

    # Combine background music and voice
    combined = background_music.overlay(voice)

    # # Export the final audio
    output_path = "./src/output_audio.mp3"
    combined.export(output_path, format="mp3")
