# audio-to-text-pipeline
This project showcases steps to transform audio file to transcript.

# Dependencies
* **ffmpeg**: v4.4.2 # Ubuntu
* **llm-agent-toolkit[transcriber]**: 0.0.24

# Why use llm-agent-toolkit?
OpenAI's `whisper-1` API accepts file uploads up to 25MB. `OpenAITranscriber` streamline the transcribing experience by integrating the ability to split large audio file into acceptable chunks.
User may utilize `AudioHelper` to generate audio chunks.

