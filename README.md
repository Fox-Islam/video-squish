# video-squish
Takes every frame in an mp4 video, reduces them to 1x200px images and then combines them all into a single image.

Before running the script, uncomment "imageio.plugins.ffmpeg.download()" if ffmpeg is not installed (Python will throw up an error if you try to run the script without it) and then comment it out again/remove the line for subsequent uses of the script since you only need to install it once.
