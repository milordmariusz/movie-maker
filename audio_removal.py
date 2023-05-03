from moviepy.editor import VideoFileClip

videoclip = VideoFileClip("movies/resources/minecraft_1.mp4")
new_clip = videoclip.without_audio()
new_clip.write_videofile("movies/resources/minecraft_1_no_audio.mp4")