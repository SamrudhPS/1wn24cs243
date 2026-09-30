def simple_reflex_agent(location, status):

    if status == "Dirty":
        return "Suck"

    elif location == "A":
        return "Move Right"

    elif location == "B":
        return "Move Left"


# Test the agent
print("Output:")

print(simple_reflex_agent("A", "Dirty"))
print(simple_reflex_agent("A", "Clean"))
print(simple_reflex_agent("B", "Dirty"))
print(simple_reflex_agent("B", "Clean"))
