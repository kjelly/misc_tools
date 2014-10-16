import os.path
import os
import tempfile


home_dir = os.path.expanduser('~')


def cd_to_tmp_dir():
    tmp_dir = tempfile.gettempdir()
    if not tmp_dir:
        print 'No temp dir'
        return False
    os.chdir(tmp_dir)
    return True


def init_vim_dir():
    os.chdir(home_dir)
    os.system("mkdir -p .vim/bundle")


def init_vimrc():
    if not cd_to_tmp_dir():
        return
    os.system('wget http://amix.dk/vim/vimrc.txt')
    if not os.path.exists('vimrc.txt'):
        print 'download failed'
        return
    vimrc_path = os.path.join(home_dir, '.vimrc')
    os.system('cp -f vimrc.txt {vimrc}'.format(vimrc=vimrc_path))


def install_to_bundle(git_path):
    bundle_dir = os.path.join(home_dir, '.vim', 'bundle')
    if not os.path.exists(bundle_dir):
        os.system("mkdir -p {dir}".format(dir=bundle_dir))
    os.chdir(bundle_dir)
    os.system('git clone ' + git_path)


def install_syntastic():
    install_to_bundle("https://github.com/scrooloose/syntastic.git")


def install_nerdtree():
    install_to_bundle("https://github.com/scrooloose/nerdtree.git")


vundle_settings = '''
set nocompatible              " be iMproved
filetype off                  " required!

set rtp+=~/.vim/bundle/vundle/
call vundle#rc()

" let Vundle manage Vundle
" required!
Bundle 'gmarik/vundle'
filetype plugin indent on     " required!

let g:jedi#completions_command = "<C-n>"
let popup_select_first = 0
let @/ = ""
set nu
'''


def vundle_install_tip():
    print '''
Please run below command in vim.
:BundleInstall
    '''



def install_vundle():
    install_to_bundle("https://github.com/gmarik/vundle.git")
    write_to_vimrc(vundle_settings)


def install_jedi_vim():
    write_to_vimrc("Bundle 'git://github.com/davidhalter/jedi-vim'\n")
    vundle_install_tip()


def install_golang_plugin():
    write_to_vimrc("Bundle 'https://github.com/jnwhiteh/vim-golang'\n")
    vundle_install_tip()


def install_scala_plugin():
    write_to_vimrc("Bundle 'derekwyatt/vim-scala'\n")
    vundle_install_tip()


def install_javascript_plugin():
    write_to_vimrc("Bundle 'pangloss/vim-javascript'\n")
    vundle_install_tip()


def install_d_plugin():
    write_to_vimrc("Bundle 'JesseKPhillips/d.vim'\n")
    vundle_install_tip()


def install_prolog_plugin():
    write_to_vimrc("Bundle 'adimit/prolog.vim'\n")
    vundle_install_tip()


def write_to_vimrc(content):
    vimrc_path = os.path.join(home_dir, '.vimrc')
    with open(vimrc_path, 'a') as ftr:
        ftr.write(content)


def install():
    init_vim_dir()
    init_vimrc()
    # install_pathogen()
    # install_syntastic()
    # install_nerdtree()
    install_vundle()
    install_jedi_vim()
    install_golang_plugin()
    install_scala_plugin()
    install_d_plugin()
    install_javascript_plugin()


if __name__ == '__main__':
    install()
