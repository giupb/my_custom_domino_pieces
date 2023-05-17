from domino.base_piece import BasePiece
from .models import InputModel, OutputModel

class GetLastVideoUrlYoutubePiece(BasePiece):
    def piece_function(self, input_model: InputModel):
        youtube_videos = input_model.youtube_videos_list
        sorted_youtube_videos = sorted(youtube_videos, key=lambda k: k['publishedAt'])
        last_video_url = sorted_youtube_videos[0]['url']
        return OutputModel(
            last_video_url=last_video_url
        )