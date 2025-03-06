import os
from pytubefix import YouTube
from fake_useragent import UserAgent
import requests

# Configure User Agent
agent = UserAgent()


def downloadsAudio(link, outputPath='.'):
    """Download audio from YouTube video to local file."""
    try:
        # Get metadata
        meta = YouTube(link).metadata
        
        # Create a filename based on the video's title and upload date
        fileName = "youtube_audio.mp3"
        
        # Try to download the first audio stream
        
        video = YouTube(link)
        audio_stream = video.streams.filter(only_audio=True).first()
        
        if audio_stream:
            audio_stream.download(
                output_path=outputPath,
                filename=fileName
            )
             
    except Exception as e:
        print(f"Error downloading audio: {e}")
        # Add retry logic here to attempt download again

def main():
    """Main function to process YouTube video URLs."""
    # List of YouTube video links (replace with actual URLs)

    
    print(f"Attempting to download audio")
    downloadsAudio('https://www.youtube.com/watch?v=CXUIvNi7hQ4', outputPath='extracted')
        
if __name__ == "__main__":
    main()