from pydantic import BaseModel

# You’ll use target_url to 
# store the URL that your shortened URL forwards to
class URLBase(BaseModel):
    target_url: str

# inherits the target_url field from URLBase
class URL(URLBase):
    # is_active field allows you to deactivate shortened URLs
    is_active: bool
    # count how many times a shortened URL has been visited
    clicks: int


    # tell pydantic with orm_mode = True 
    # work with a database model
    class Config:
        orm_mode = True


# use the data in your API without
#  storing it in your database.
class URLInfo(URL):
    url: str
    admin_url: str