# Audio Transcriber App

Welcome to the Audio Transcriber app, a simple tool that uses the Whisper neural network-based speech recognition model to transcribe audio files. This repository provides the necessary code to transcribe audio files and save the results to a text file.

## Dependencies

This app relies on the following dependency:

- **Whisper**: A neural net-based speech recognition model.

Do not worry about the details of downloading this model. It is included in the requirements.txt

## How to Run

To transcribe audio files using this app, follow these steps:

1. **Clone this repository to your local machine:**

    ```bash
    git clone https://github.com/gawdam/audio-transcriber.git
    cd audio-transcriber
    ```

2. **Install the required dependencies. You can use the following command to install them:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Run the transcribe script, providing the path to your audio file and the location where you want to save the transcription:**

    ```bash
    python transcribe.py --audio_file="<audio_file_location>" --save_to="<save_to_txt_location>"
    ```

    Replace `<audio_file_location>` with the path to your audio file and `<save_to_txt_location>` with the desired location to save the transcription results.

## Troubleshooting Audio File Reading Errors

If you encounter errors related to reading audio files, it may be due to missing dependencies. Follow these instructions to resolve the issue:

1. Download the appropriate FFmpeg installation zip from [https://github.com/BtbN/FFmpeg-Builds/releases](https://github.com/BtbN/FFmpeg-Builds/releases).**

2. Unzip the downloaded file and navigate to the `ffmpeg-master-folder\bin` directory.

3. Copy all contents of the `bin` directory.

4. Paste the copied contents into the same directory as the transcribe script in this repository.

After completing these steps, you should be able to run the transcribe script without any issues.

Happy transcribing!
