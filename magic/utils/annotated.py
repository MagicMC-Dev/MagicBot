from typing import Annotated

from nonebot.params import Depends

from magic.database import User as _User

UserInfo = Annotated[_User, Depends(_User.get_user_by_event)]
