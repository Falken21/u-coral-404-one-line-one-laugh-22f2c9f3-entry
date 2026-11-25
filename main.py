"""One Line, One Laugh -- entry for the make.fun one-liner contest.

The joke: a smart fridge with access to its owner's late-night snack
history takes matters into its own hands.
"""

TEXT = (
    "My smart fridge just ordered milk, eggs, and a gym membership. "
    "It has seen my 2 a.m. snack history and staged an intervention."
)


def main():
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
