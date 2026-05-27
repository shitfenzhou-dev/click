#!/usr/bin/env python
from click.types import Choice
import enum


class TestEnum(enum.Enum):
    OPTION1 = "option1"
    OPTION2 = "option2"
    Straße = "Straße"


def test_normalize_choice():
    print("Testing normalize_choice...")
    choice1 = Choice(["Straße", "Strasse", "Schule"], case_sensitive=False)
    ctx = None
    
    # Test German ß
    result1 = choice1.normalize_choice("Straße", ctx)
    print(f"normalize_choice('Straße') = {repr(result1)}")
    
    result2 = choice1.normalize_choice("strasse", ctx)
    print(f"normalize_choice('strasse') = {repr(result2)}")
    
    # Should be equal when case_sensitive=False
    print(f"Equal? {result1 == result2}")
    
    print("\nTesting Enum handling...")
    choice2 = Choice([TestEnum.OPTION1, TestEnum.OPTION2, TestEnum.Straße], case_sensitive=False)
    for opt in choice2.choices:
        normalized = choice2.normalize_choice(opt, ctx)
        print(f"normalize_choice({opt.name}) = {repr(normalized)}")


def test_shell_complete():
    print("\n\nTesting shell_complete...")
    choice = Choice(["Straße", "Strasse", "Schule"], case_sensitive=False)
    
    # Mock objects (just need to exist)
    class MockContext:
        pass
    
    class MockParam:
        pass
    
    ctx = MockContext()
    param = MockParam()
    
    completions = choice.shell_complete(ctx, param, "stra")
    print(f"Completions for 'stra': {[c.value for c in completions]}")
    
    completions = choice.shell_complete(ctx, param, "sch")
    print(f"Completions for 'sch': {[c.value for c in completions]}")


if __name__ == "__main__":
    test_normalize_choice()
    test_shell_complete()
