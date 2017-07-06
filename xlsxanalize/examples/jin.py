




from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('../templates'))
template = env.get_template('mess.html')

def z_report():
    return 5000

not_mess = ""
dop_doh_mess = "доп доход"
print(template.render(z=5000, dop_doh_mess=None))