import click
from click.shell_completion import CompletionItem

def test_choice_completion():
    choice = click.Choice(["straße"], case_sensitive=False)
    ctx = click.Context(click.Command("test"))
    param = click.Parameter(["--foo"])
    
    # User types "straß"
    comps = choice.shell_complete(ctx, param, "straß")
    print("Completion for 'straß':", comps)

    # User types "strass"
    comps2 = choice.shell_complete(ctx, param, "strass")
    print("Completion for 'strass':", comps2)

test_choice_completion()
