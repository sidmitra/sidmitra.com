from jinja2 import Environment, Template, FileSystemLoader
pages = ['index','books','research']
environment_name = 'sidm'

def render(page):
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template(page+".templ")
    context={}
    fout = open(page+'.html','w')
    fout.write(template.render())
    fout.close()
    
def main():
    for page in pages:
        render(page)
        
    
if __name__ == "__main__":
    main()