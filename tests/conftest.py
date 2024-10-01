"""测试的一些初始化"""

import pytest
from dotenv import load_dotenv

from qihoo_360 import Qihoo360User, Qihoo360

load_dotenv()
import config  # noqa: E402


@pytest.fixture(scope='session')
def qihoo_client():
    """360用户信息"""

    user = Qihoo360User(username=config.USERNAME,
                        password=config.PASSWORD)
    client = Qihoo360(user=user)
    yield client