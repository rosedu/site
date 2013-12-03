from fabric.api import local, lcd
from os import walk
from os.path import isdir

skip = 5

def generate_file(page_no, template, pages):
    pskip = skip * page_no
    prev = page_no - 1 if page_no > 0 else -1
    npage = page_no + 1 if page_no < pages - 1 else -1
    with open('ro/news_%d.markdown' % page_no, 'w') as f:
        f.write(template.format(ppp=skip, ps=pskip, prev_page=prev, next_page=npage))

def read_template():
    with open('ro/_news_template', 'r') as f:
        template = f.read()
    return template

def get_num_pages():
    count = 0
    for root, dirs, files in walk('ro/_posts'):
        count += len(files)
    count += skip if count % skip else 0
    return count / skip

def create_paginations():
    template = read_template()
    pages = get_num_pages()
    for i in range(pages):
        generate_file(i, template, pages)


def devel():
    create_paginations()
    local('jekyll --auto --serve 8000')


def build():
    create_paginations()
    local('jekyll')


def deploy_old():
    build()
    local('rsync -rtv _site/ site@rosedu.org:public_html')
    local('rsync -rtv files/ site@rosedu.org:public_html/files/')

def deploy():
    git = lambda x: local('git --git-dir=../.git_deploy --work-tree=./ '+x)
    if not isdir('.git_deploy'):
        print 'Trying to clone the deploy repo on my own.'
        local('rm -rf _site')
        local("git clone -b gh-pages --separate-git-dir=.git_deploy `git remote -v|grep 'origin.*push'| tr ' ' '\t'|cut -f2`  _site")
    
    with lcd('_site'):
        git('status')
        git('pull')
    build()
    with lcd('_site'):
        git('status')
        git('add -f *')
        git('status')
        git('commit -a -m "`git log -n1 --oneline`" ')
        git('push')
