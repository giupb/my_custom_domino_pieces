from pydantic import BaseModel, Field


class InputModel(BaseModel):
    """
    Piece Inputs
    """
    instagram_media_list: list = Field(
        ...,
        description = "list of Instagram media posts"
    )

class OutputModel(BaseModel):
    """
    Piece Outputs
    """
    all_captions: str = Field(
        description="all captions from Instagram media posts"
    )


# class SecretsModel(BaseModel):
#     """
#     Piece Secrets
#     """
#     pass