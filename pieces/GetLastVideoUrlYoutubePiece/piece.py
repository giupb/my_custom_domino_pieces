from domino.base_piece import BasePiece
from .models import InputModel, OutputModel

class GetLastVideoUrlYoutubePiece(BasePiece):
    def piece_function(self, input_model: InputModel):
        youtube_videos = input_model.youtube_videos_list
        sorted_youtube_videos = sorted(youtube_videos, key=lambda k: k['publishedAt'])
        last_video_url = sorted_youtube_videos[0]['url']

        self.format_display_result(last_video_url)

        return OutputModel(
            last_video_url=last_video_url
        )
    
    def format_display_result(self, last_video_url: str):
        md_text = f"""
## Last Video URL
[{last_video_url}]({last_video_url})

"""
        file_path = f"{self.results_path}/display_result.md"
        with open(file_path, "w") as f:
            f.write(md_text)
        self.display_result = {
            "file_type": "md",
            "file_path": file_path
        }