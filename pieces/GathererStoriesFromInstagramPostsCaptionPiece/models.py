from pydantic import BaseModel, Field
from enum import Enum

class OutputTypeType(str, Enum):
    """
    Output type for the result text
    """
    file = "file"
    string = "string"
    file_and_string = "file_and_string"


class InputModel(BaseModel):
    """
    Piece Inputs
    """
    instagram_media_list: list = Field(
        ...,
        description = "list of Instagram media posts"
    )
    output_type: OutputTypeType = Field(
        default=OutputTypeType.string,
        description='The type of the output.'
    )
    output_file_name: str = Field(
        default="all_stories.txt",
        description="The name of the file to save all the stories. It works only with Output Type equals to file or file_and_string"
    )


class OutputModel(BaseModel):
    """
    Piece Outputs
    """
    all_stories_string: str = Field(
        default=None,
        description="all captions from Instagram media posts in string format"
    )
    all_stories_file_path: str = Field(
        default=None,
        description="all captions from Instagram media posts in txt file format"
    )


# class SecretsModel(BaseModel):
#     """
#     Piece Secrets
#     """
#     pass