"""
In Python, default argument values are evaluated only once
at the function definition time--not each time the function is called.
"""

def add_color(color, colors=[]):
    colors.append(color)
    return colors

rgb = add_color("red")
print(rgb)  # Output: ['red']

hsl = add_color("hue")
print(hsl)  # Output: ['red', 'hue']

"""
for 'hsl' new list should be created but,
that doesn't really happens.
Instead it uses already existing default value.
"""

# Alternate Approach
def mod_add_color(color, colors = None):
    if colors is None:
        colors = []
    colors.append(color)
    return colors

rgb = mod_add_color("red")
print(rgb)  # Output: ['red']

hsl = mod_add_color("hue")
print(hsl)  # Output: ['hue']