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
    input_dir = "/app/input"
    output_dir = "/app/output"

    # Crear la carpeta de salida si no existe
    os.makedirs(output_dir, exist_ok=True)

    # Procesar todos los archivos en la carpeta de entrada
    for file_name in os.listdir(input_dir):
        input_path = os.path.join(input_dir, file_name)

        # Si el archivo es MP4, convertirlo a MP3
        if file_name.endswith(".mp4"):
            mp3_file_name = file_name.replace(".mp4", ".mp3")
            mp3_path = os.path.join(input_dir, mp3_file_name)

            if not os.path.exists(mp3_path):
                print(f"Convirtiendo {file_name} a {mp3_file_name}...")
                convert_mp4_to_mp3(input_path, mp3_path)
            else:
                print(f"El archivo {mp3_file_name} ya existe. Saltando la conversión.")

    # Transcribir todos los archivos MP3
    for file_name in os.listdir(input_dir):
        if file_name.endswith(".mp3"):
            mp3_path = os.path.join(input_dir, file_name)
            transcription_file = os.path.join(output_dir, file_name.replace(".mp3", ".txt"))

            print(f"Transcribiendo {file_name}...")
            transcript = transcribe_audio(mp3_path, language="es")

            # Guardar la transcripción en la carpeta de salida
            with open(transcription_file, "w") as f:
                f.write(transcript)

            print(f"Transcripción de {file_name} completada. Guardada en {transcription_file}")

    print("Proceso completado.")