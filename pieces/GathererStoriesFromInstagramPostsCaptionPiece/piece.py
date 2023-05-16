from domino.base_piece import BasePiece
from .models import InputModel, OutputModel

class GathererStoriesFromInstagramPostsCaptionPiece(BasePiece):
    def piece_function(self, input_model: InputModel):
        sorted_media_list = sorted(input_model.instagram_media_list, key=lambda x: x['timestamp'])
        all_captions = ""
        for i in sorted_media_list:
            all_captions += f"Begin of a story\n{i.get('caption')}End of a story\n"
        return OutputModel(
            all_captions=all_captions
        )