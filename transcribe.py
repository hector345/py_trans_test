import whisper
import ffmpeg
import os

def convert_mp4_to_mp3(input_file, output_file):
    # Usa ffmpeg para convertir el archivo MP4 a MP3
    ffmpeg.input(input_file).output(output_file).run()

def transcribe_audio(audio_file, language="es"):
    # Cargar el modelo de Whisper
    model = whisper.load_model("base")
    # Transcribir el audio
    result = model.transcribe(audio_file, language=language)
    return result['text']

if __name__ == "__main__":
    input_file = "/app/input.mp4"
    output_file = "/app/output.mp3"

    # Verificar si el archivo MP3 ya existe
    if not os.path.exists(output_file):
        # Convertir MP4 a MP3
        convert_mp4_to_mp3(input_file, output_file)
    else:
        print(f"El archivo {output_file} ya existe. Saltando la conversión.")

    # Transcribir el MP3 en español de México
    transcript = transcribe_audio(output_file, language="es")
    
    # Guardar la transcripción en un archivo de texto
    with open("/app/transcription.txt", "w") as f:
        f.write(transcript)
    
    print("Transcripción completada. Ver archivo transcription.txt")
