from moviepy.editor import VideoFileClip, ImageClip, CompositeVideoClip, AudioFileClip, CompositeAudioClip

from moviepy.editor import VideoFileClip, AudioFileClip, ImageClip, CompositeAudioClip, CompositeVideoClip

def create_video():
    delay = float(input("How long dealy between comments(0.0-1.5): "))
    voices = []
    video_and_photos = []

    video = VideoFileClip("movies/resources/minecraft_1_no_audio.mp4")
    video_and_photos.append(video)

    title_voice = AudioFileClip("voices/post.mp3").set_start(0)
    voices.append(title_voice)

    last_voice_end = title_voice.end + delay

    title = (
        ImageClip("ss/question_screenshot.png")
        .set_start(0)
        .set_duration(last_voice_end)
        .set_pos(("center", "center"))
        .resize(width=600)
    )
    video_and_photos.append(title)

    for index in range(1, 6):
        comment_voice = AudioFileClip(f"voices/comments/comment_{index}.mp3").set_start(last_voice_end)
        comment_duration = comment_voice.duration + delay
        voices.append(comment_voice)

        comment = (
            ImageClip(f"ss/comments/comment_{index}.png")
            .set_start(last_voice_end)
            .set_duration(comment_duration)
            .set_pos(("center", "center"))
            .resize(width=600)
        )
        video_and_photos.append(comment)
        last_voice_end += comment_duration

    mixed_audio = CompositeAudioClip(voices)
    final_video = (
        CompositeVideoClip(video_and_photos)
        .set_duration(last_voice_end)
        .set_audio(mixed_audio)
    )

    final_video.write_videofile("movies/output.mp4")
