let mapleader =","
set clipboard=unnamedplus
noremap <Leader>y "*y
noremap <Leader>p "*p
noremap <Leader>Y "+y
noremap <Leader>P "+p


set title
set go=a
set mouse=a
set nohlsearch
set clipboard+=unnamedplus

filetype plugin on
set noshowmode
set noruler
set laststatus=0
set noshowcmd
set showmatch
set smartcase
set smartindent
set smarttab
set ts=4
vnoremap < <gv
vnoremap > >gv

set nocompatible
syntax on
set encoding=utf-8
set number relativenumber
set wildmode=longest,list,full
" Move down file lines
noremap J 5j
vnoremap J 5j
" Move up file lines
noremap K 5k
vnoremap K 5k
:inoremap jj <Esc>
