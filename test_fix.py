import click
from click.shell_completion import CompletionItem

def test_unicode_choice_completion():
    # 创建包含 unicode 字符的 Choice 类型
    choice_type = click.Choice(["straße", "Straße", "hello"], case_sensitive=False)
    
    # 模拟一个 ctx
    ctx = None
    param = None
    
    # 测试不同的 incomplete 值
    test_cases = [
        "s",
        "st",
        "str",
        "stra",
        "stras",
        "strass",
        "Stra",
        "h",
    ]
    
    print("Testing unicode choice completion (case_sensitive=False)...")
    print("Choices:", choice_type.choices)
    print()
    
    for incomplete in test_cases:
        completions = choice_type.shell_complete(ctx, param, incomplete)
        print(f"Incomplete: '{incomplete}'")
        print(f"Completions: {[c.value for c in completions]}")
        print()

def test_case_sensitive_completion():
    # 测试 case_sensitive=True 的情况
    choice_type = click.Choice(["Hello", "hello", "World"], case_sensitive=True)
    
    ctx = None
    param = None
    
    print("Testing case-sensitive completion...")
    print("Choices:", choice_type.choices)
    print()
    
    test_cases = [
        "h",
        "H",
        "W",
    ]
    
    for incomplete in test_cases:
        completions = choice_type.shell_complete(ctx, param, incomplete)
        print(f"Incomplete: '{incomplete}'")
        print(f"Completions: {[c.value for c in completions]}")
        print()

if __name__ == "__main__":
    test_unicode_choice_completion()
    print("=" * 50)
    test_case_sensitive_completion()
