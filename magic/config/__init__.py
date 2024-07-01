from .utils import load_config
from .config import MagicConfig
from .path import BOT_DIR as BOT_DIR
from .path import LOG_DIR as LOG_DIR
from .path import RES_DIR as RES_DIR
from .path import DATA_DIR as DATA_DIR
from .path import FONT_DIR as FONT_DIR
from .path import PAGE_DIR as PAGE_DIR
from .path import AUDIO_DIR as AUDIO_DIR
from .path import IMAGE_DIR as IMAGE_DIR
from .path import VIDEO_DIR as VIDEO_DIR
from .config import BaseConfig as BaseConfig

magic_config = MagicConfig(**load_config())
"""MagicBot 配置"""

bot_config = magic_config.bot
"""本体主要配置"""

plugin_config = magic_config.plugin
"""插件加载相关配置"""

log_config = magic_config.log
"""日志相关配置"""

database_config = magic_config.database
"""数据库相关配置"""
