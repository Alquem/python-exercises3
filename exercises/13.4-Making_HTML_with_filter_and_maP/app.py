all_colors = [
	{"label": 'Red', "sexy": True},
	{"label": 'Pink', "sexy": False},
	{"label": 'Orange', "sexy": True},
	{"label": 'Brown', "sexy": False},
	{"label": 'Pink', "sexy": True},
	{"label": 'Violet', "sexy": True},
	{"label": 'Purple', "sexy": False},
]

#Your code go here:
##filter_colors = list(filter(lambda color: color["sexy"]==True, all_colors))
##generate_li = "".join(map(lambda color: f"<li>{color['label']}</li>", filter_colors))
##print(generate_li)
def filter_colors(colors):
	return list(filter(lambda color: color["sexy"]==True, colors))

def generate_li(sexy_colors):
	return "".join(map(lambda color: f"<li>{color['label']}</li>", sexy_colors))

print(generate_li(filter_colors(all_colors)))