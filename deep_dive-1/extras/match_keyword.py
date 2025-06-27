def respond(language):
    match language:
        case "Java" | "Javascript":  # can use multiple options
            return "Hmm, coffee!"
        case "Python":
            return "I'm not scared of snakes!"
        case "Rust":
            return "don't drink too much water!"
        case "Go":
            return "Collect $200"
        case _:
            return "I'm sorry....."


# print(respond("Python"))
# print(respond("Javascript"))
# print(respond("Go"))
# print(respond("C"))

symbols = {
    "R": "\u2192",
    "L": "\u2190",
    "up": "\u2191",
    "down": "\u2193",
    "pick": "\u2923",
    "drop": "\u2925"
}


# print(symbols)


def op(command):
    match command:
        case ["move", ("up" | "down" | "L" | "R") as direction]:
            return symbols[direction]
        case "pick":
            return symbols["pick"]
        case "drop":
            return symbols["drop"]
        case _:
            raise ValueError(f"{command} does not compute!")


print(op(["move", "up"]))
print(op(["move", "down"]))
print(op(["move", "R"]))
print(op(["move", "L"]))
print(op("pick"))
