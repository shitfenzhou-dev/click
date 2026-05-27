import click
from click.core import Command, Option
from click.types import Choice
from click.shell_completion import ShellComplete

def _get_words(cli, args, incomplete):
    comp = ShellComplete(cli, {}, cli.name, '_CLICK_COMPLETE')
    completions = comp.get_completions(args, incomplete)
    return [c.value for c in completions]

# Test 1: existing test
cli = Command('cli', params=[Option(['-a'], type=Choice(['Au', 'al', 'Bc'], case_sensitive=False))])
result = _get_words(cli, ['-a'], 'a')
print(f'Test 1 (case_sensitive=False, input=a): {result}')
assert result == ['au', 'al'], f'Expected ["au", "al"], got {result}'

# Test 2: Unicode casefold
cli = Command('cli', params=[Option(['-a'], type=Choice(['Straße', 'Strasse', 'Other'], case_sensitive=False))])
result = _get_words(cli, ['-a'], 'strasse')
print(f'Test 2 (Unicode, input=strasse): {result}')
assert result == ['strasse', 'strasse'], f'Expected ["strasse", "strasse"], got {result}'

result = _get_words(cli, ['-a'], 'straße')
print(f'Test 3 (Unicode, input=straße): {result}')
assert result == ['strasse', 'strasse'], f'Expected ["strasse", "strasse"], got {result}'

print('All tests passed!')
