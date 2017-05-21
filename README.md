# video-squish
Takes every frame in an mp4 video, reduces them to 1x200px images and then combines them all into a single image.

Before running the script, uncomment line 44 "imageio.plugins.ffmpeg.download()" if ffmpeg is not installed (Python will throw up an error if you try to run the script without it) and then comment it out again/remove the line for subsequent uses of the script since you only need to install it once.

This script is adapted from the wonderful Alan Zucconi's tutorial for making 'game barcodes' which you can find here: https://www.patreon.com/posts/tutorial-game-of-3762003
The biggest change is that this takes local files and not Youtube videos (which requires a different library, and thus created a need for the bulk of the minor changes), but also that it doesn't do the colour sorting thing.
