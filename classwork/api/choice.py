import inquirer
from inquirer.themes import GreenPassion

question = [
    inquirer.List("color", message="What is your favorite color?", choices=["Green", "Blue", "Red", "Purple", "None"], default="None"),
    inquirer.Text("name", message="Whats your name?", default=""),
    inquirer.Checkbox(
        "kill_list", message="Who you want to kill?", choices=["Cersei", "Littlefinger", "The Mountain"]
    ),
]

selected = inquirer.prompt(question, theme=GreenPassion())
print(f"You've selected {selected}")