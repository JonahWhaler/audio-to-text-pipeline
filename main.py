# Dependencies
import os
from dotenv import load_dotenv
from llm_agent_toolkit.transcriber import TranscriptionConfig
from llm_agent_toolkit.transcriber.open_ai import OpenAITranscriber


if __name__ == "__main__":
    load_dotenv()
    # Input-Output
    AUDIO_FILES = [
        # "./audio/part_0.mp3",
        # "./audio/part_1.mp3",
        "./audio/part_2.mp3",
    ]
    OUTPUT_DIRECTORY = "./output"

    # Execution
    whisper_config = TranscriptionConfig(
        name="whisper-1", temperature=0.3, response_format="text"
    )
    agent = OpenAITranscriber(config=whisper_config)

    for audio_file in AUDIO_FILES:
        basename = os.path.basename(audio_file)
        name_wo_ext = os.path.splitext(basename)[0]
        export_directory = os.path.join(OUTPUT_DIRECTORY, name_wo_ext)
        os.makedirs(export_directory, exist_ok=True)

        agent.transcribe(
            prompt="This is a sermon in Mandarin.",
            filepath=audio_file,
            tmp_directory=export_directory,
        )

    # View Output
    folders = os.listdir(OUTPUT_DIRECTORY)
    for folder in folders:
        files = os.listdir(os.path.join(OUTPUT_DIRECTORY, folder))
        for file in files:
            ext = os.path.splitext(file)[1]
            if ext != ".md":
                continue

            filepath = os.path.join(OUTPUT_DIRECTORY, folder, file)
            print(f"Filepath: {filepath}")
            with open(filepath, "r", encoding="utf-8") as f:
                line = f.read()
                print(f">>>> {line[:80]}")
            print("\n")
