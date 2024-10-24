Construir y ejecutar el contenedor Docker

    Coloca el archivo MP4 en la misma carpeta que el Dockerfile, con el nombre input.mp4 (puedes cambiar este nombre, pero asegúrate de cambiar también en el script transcribe.py).

    Abre un terminal en esa carpeta y construye la imagen Docker:

    bash

docker build -t whisper-transcriber .

Una vez construida la imagen, ejecuta el contenedor. El comando montará tu carpeta local en el contenedor para que Docker pueda acceder a los archivos MP4 y escribir la transcripción:

bash

    docker run --rm -v ${PWD}:/app whisper-transcriber

Este comando creará un archivo transcription.txt con el texto transcrito en la misma carpeta donde está el Dockerfile.
Notas adicionales

    Si deseas usar el archivo MP4 desde otra ubicación (como C:\Users\hecto\Downloads\), puedes modificar el script o montar esa carpeta en el contenedor utilizando -v "C:\Users\hecto\Downloads":/app/ en lugar de ${PWD}.
