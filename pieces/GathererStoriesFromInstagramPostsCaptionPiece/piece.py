from domino.base_piece import BasePiece
from .models import InputModel, OutputModel

class GathererStoriesFromInstagramPostsCaptionPiece(BasePiece):
    def piece_function(self, input_model: InputModel):
        sorted_media_list = sorted(input_model.instagram_media_list, key=lambda x: x['timestamp'])
        all_stories = ""
        for i in sorted_media_list:
            all_stories += f"Begin of a story\n{i.get('caption')}End of a story\n"
        
        self.format_display_result(all_stories)

        if input_model.output_type == "string":
            return OutputModel(
                all_stories_string=all_stories
            )
        
        output_file_path = f"{self.results_path}/{input_model.output_file_name}"
        with open(output_file_path, "w") as f:
            f.write(all_stories)
        
        if input_model.output_type == "file":
            self.logger.info(f"Result returned as file in {output_file_path}")
            return OutputModel(
                all_stories_file_path=output_file_path
            )

        self.logger.info(f"Result returned as string and file in {output_file_path}")
        return OutputModel(
            all_stories_string=all_stories,
            all_stories_file_path=output_file_path,
        )
    
    def format_display_result(self, all_stories: str):
        md_text = f"""
## All Stories  \n
{all_stories}

"""
        file_path = f"{self.results_path}/display_result.md"
        with open(file_path, "w") as f:
            f.write(md_text)
        self.display_result = {
            "file_type": "md",
            "file_path": file_path
        }