import glob

from fabric.api import local, task
from jinja2 import Environment, PrefixLoader, FileSystemLoader


# Init env
loader = PrefixLoader({
    "theme": FileSystemLoader('theme'),
    "pages": FileSystemLoader('pages'),
    # blog": FileSystemLoader("blog")
})

jinja_env = Environment(loader=loader)


@task
def copy_static_to_build():
    ''' Copies all the static files(like css/js) to build dir.'''
    local('rm -rf ./build')
    local('mkdir ./build')
    local('cp -R static/* ./build/')


@task
def render_pages():
    for page in glob.glob('pages/*.html'):
        print("Rendering {}".format(page))
        template = jinja_env.get_template(page)
        fout = open('build/' + page.replace('pages/', ''), 'w')
        fout.write(template.render())
        fout.close()


@task
def render_blog():
    pass


@task
def build():
    copy_static_to_build()
    render_pages()
    render_blog()


@task
def deploy():
    build()
    local('./google_appengine/appcfg.py update build/')
    # local('appcfg.py --oauth2 update build/')


@task
def serve():
    build()
    local('./google_appengine/dev_appserver.py build/')
    # local('dev_appserver.py build/')
