# 此文件默认用于fixture公告方法,
# 所有同级和子级目录都可以调用

import pytest
import os.path
from typing import (
    Any,
    Callable,
    Dict,
    Generator,
    List,
    Literal,
    Optional,
    Protocol,
    Sequence,
    Union,
    Pattern,
    cast,
)
from playwright.sync_api import BrowserContext, Page

"""
@pytest.fixture()
# 在程序开始之前先调用fixture
def hello_world():
    print("hello world")
    yield
    print("say! 886")

@pytest.fixture
def page(context: BrowserContext) -> Page:
    print("this is  my page")
    return context.new_page()"""

@pytest.fixture(scope="session")
# 用于设置 自动化屏幕大小和录像大小
def browser_context_args(browser_context_args,pytestconfig: Any):
    # 改造成pytest.ini的可配置项
    width,height= pytestconfig.getoption("--viewport")
    return {
            **browser_context_args,
            # 自动化屏幕大小
            "viewport":{
                "width":width,
                "height":height
            },
            # 录像的大小
            "record_video_size": {
                "width": width,
                "height": height
            }
        }
def pytest_addoption(parser: Any) -> None:
    group = parser.getgroup("playwright", "Playwright")
    group.addoption(
        "--viewport",
        action="store",
        default=[1200,900],
        help="viewport size set",
        type = int,
        # nargs 接受参数为2
        nargs = 2,
    )
