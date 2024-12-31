import os
from dotenv import load_dotenv
from llm_agent_toolkit import TranscriptionConfig, transcriber


if __name__ == "__main__":
    load_dotenv()

    AUDIO_FILES = [
        # "./audio/part_0.mp3",
        # "./audio/part_1.mp3",
        "./audio/part_2.mp3",
    ]
    OUTPUT_DIRECTORY = "./output"

    whisper_config = TranscriptionConfig(
        name="whisper-1", temperature=0.3, response_format="text"
    )
    agent = transcriber.open_ai.OpenAITranscriber(config=whisper_config)

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
