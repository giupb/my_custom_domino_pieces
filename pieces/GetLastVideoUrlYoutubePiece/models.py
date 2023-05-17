from pydantic import BaseModel, Field


class InputModel(BaseModel):
    """
    Piece Inputs
    """
    youtube_videos_list: list = Field(
        ...,
        description = "list of Youtube videos"
    )

class OutputModel(BaseModel):
    """
    Piece Outputs
    """
    last_video_url: str = Field(
        description="last Youtube video url"
    )