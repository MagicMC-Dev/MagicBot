from typing import Any

from pydantic import validator

from magic.log import logger
from magic.config import BaseConfig


class LevelConfig(BaseConfig):
    base_exp: int = 150
    """初始经验阈值"""
    max_level: int = 70
    """最大等级"""
    cardinality: float = 1.1
    """经验系数"""


class SignConfig(BaseConfig):
    """签到配置"""

    rewards: dict[str, Any] = {"coin": [10, 20], "exp": 320, "favor": 0}

    @validator("rewards", pre=True)
    def replenish(cls, v):
        logger.info("运行 replenish")
        if missing_keys := {"coin", "exp", "favor"} - v.keys():
            logger.info(f"Missing reward key: {missing_keys}")
            for key in missing_keys:
                v[key] = 0
            return v
        return v

    # @validator("rewards")
    # def check_rewards(cls, v):
    #     logger.info("运行 check_rewards")
    #     if extra_key := v.keys() - {"coin", "exp", "favor"}:
    #         raise ValueError(f"Invalid reward key: {extra_key}")
    #     return v


class GameConfig(BaseConfig):
    level: LevelConfig = LevelConfig()
    sign: SignConfig = SignConfig()
