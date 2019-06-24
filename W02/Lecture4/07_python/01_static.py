import re


class Utilities:
    @staticmethod
    def isRegoValid(rego):
        return re.compile("^[A-Z]{3}\\d{3}$").match(rego)


while True:
    print("Enter rego: ", end="")
    rego = input()
    if not Utilities.isRegoValid(rego):
        print("This rego is not valid, please try again.")
        continue
    print("Thanks for the valid rego: " + rego)
    break
