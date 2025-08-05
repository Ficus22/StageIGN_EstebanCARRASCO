import subprocess
import os

INPUT_VIDEO = "Result/NByteTrack2.mp4"  # Exemple : "videos/mavideo.mp4"

# Le fichier converti portera le suffixe "_h264"
OUTPUT_VIDEO = INPUT_VIDEO.replace(".mp4", "_h264.mp4")

def convert_to_h264(input_path, output_path):
    command = [
        "ffmpeg",
        "-y",  # overwrite output
        "-i", input_path,
        "-vcodec", "libx264",
        "-crf", "23",
        "-preset", "fast",
        "-movflags", "+faststart",
        output_path
    ]

    print(f"Conversion : {input_path} -> {output_path}")
    try:
        subprocess.run(command, check=True)
        print("✅ Conversion terminée avec succès.")
    except subprocess.CalledProcessError as e:
        print(f"❌ Erreur lors de la conversion : {e}")

if __name__ == "__main__":
    if not os.path.isfile(INPUT_VIDEO):
        print(f"❌ Fichier introuvable : {INPUT_VIDEO}")
    else:
        convert_to_h264(INPUT_VIDEO, OUTPUT_VIDEO)
