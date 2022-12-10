from rich.console import Console
from rich.theme import Theme


iTheme = Theme({
    "good" : "green",
    "bad": "bold red"
})
console = Console(theme=iTheme)

# console.print(":smiley: :vampire: :pile_of_poo: :thumbs_up: :raccoon:")

def print(s):
    console.print(s)

def print_good(s):
    console.print(s, style="good")

def print_bad(s):
    console.print(s, style="bad")

def log(s):
    console.log(s)


