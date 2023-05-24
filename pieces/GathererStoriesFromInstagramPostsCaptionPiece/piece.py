from domino.base_piece import BasePiece
from .models import InputModel, OutputModel

class GathererStoriesFromInstagramPostsCaptionPiece(BasePiece):
    def piece_function(self, input_model: InputModel):
        sorted_media_list = sorted(input_model.instagram_media_list, key=lambda x: x['timestamp'])
        all_captions = ""
        for i in sorted_media_list:
            all_captions += f"Begin of a story\n{i.get('caption')}End of a story\n"
        
        self.format_display_result(all_captions)
        
        return OutputModel(
            all_captions=all_captions
        )
    
    def format_display_result(self, all_captions: str):
        md_text = f"""
## All Captions
{all_captions}

"""
        file_path = f"{self.results_path}/display_result.md"
        with open(file_path, "w") as f:
            f.write(md_text)
        self.display_result = {
            "file_type": "md",
            "file_path": file_path
        }