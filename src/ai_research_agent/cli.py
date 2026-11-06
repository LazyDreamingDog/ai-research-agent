"""Command-line entry point for the project scaffold."""

import argparse
from importlib.metadata import version


def main() -> int:
    """Display project help until the research workflow is implemented."""
    parser = argparse.ArgumentParser(
        prog="ai-research-agent",
        description="AI 资料调研助手：项目初始化版本，调研功能尚未实现。",
        epilog="后续将实现搜索资料、阅读网页、核对来源和生成中文报告。",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {version('ai-research-agent')}",
    )
    parser.parse_args()
    parser.print_help()
    return 0
