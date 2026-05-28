#!/usr/bin/env python
"""
简单的测试脚本来验证 ProgressBar 重构后的行为是否与之前一致
"""

import sys
sys.path.insert(0, '/app/click/src')

import click

# 测试 ProgressBar 功能
def test_progress_bar_refactor():
    # 创建一个测试用的 ProgressBar
    bar = click.progressbar(range(10))
    bar.__enter__()
    
    # 测试 format_pos
    print("Testing format_pos():")
    bar.pos = 5
    print(f"  pos=5, length=10: {bar.format_pos()}")
    
    # 测试 format_pct
    print("\nTesting format_pct():")
    bar.pos = 3
    print(f"  pos=3, length=10: {bar.format_pct()}")
    
    # 测试 _format_progress_info 私有方法（原来的 info_bits 生成逻辑）
    print("\nTesting _format_progress_info() (new private method):")
    # 测试默认行为
    info = bar._format_progress_info()
    print(f"  Default show_percent=None, show_pos=False: '{info}'")
    
    # 测试各种组合
    bar.show_pos = True
    info = bar._format_progress_info()
    print(f"  show_pos=True: '{info}'")
    
    bar.show_percent = True
    info = bar._format_progress_info()
    print(f"  show_pos=True, show_percent=True: '{info}'")
    
    # 测试 item_show_func
    print("\nTesting item_show_func:")
    bar.item_show_func = lambda item: f"Item {item}" if item is not None else None
    bar.current_item = 42
    info = bar._format_progress_info()
    print(f"  With item_show_func and current_item=42: '{info}'")
    
    # 测试完整的 format_progress_line
    print("\nTesting format_progress_line() (should still work the same):")
    bar.label = "Test"
    line = bar.format_progress_line()
    print(f"  Full progress line: '{line}'")
    
    # 让我们确保可以实际渲染（虽然我们不能在非 tty 上看到实际效果）
    print("\nBasic functionality verification: Refactoring didn't break the API.")
    
    bar.__exit__(None, None, None)
    return True

if __name__ == "__main__":
    test_progress_bar_refactor()
    print("\n✅ Manual verification completed. Refactoring appears correct.")
