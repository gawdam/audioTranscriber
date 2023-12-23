import argparse, sys
import whisper

parser=argparse.ArgumentParser()

parser.add_argument("--audio_file", help="Add the audio file to be transcribed here. Eg.'lecture.mp3'")
parser.add_argument("--save_to", help="Save to this location. Eg.'transcript.txt'")

args=parser.parse_args()


if __name__ == '__main__':
    model = whisper.load_model('base')
    if args.audio_file:
        result = model.transcribe(args.audio_file)
    else:
        result = model.transcribe('sample_audio/harvard.mp3')
    print(result['text']);
    if args.save_to:
        with open('transcript2.txt', "w") as transcript:
            transcript.write(result['text'])


