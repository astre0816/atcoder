#!/bin/bash

d=$(cd $(dirname $(readlink -f $BASH_SOURCE)); pwd)

Deactivate() {
    unalias deactivate
    unalias acc
    unalias vim
    cd $d
    deactivate
}

Acc() {
    if [ "$1" = "t" -o "$1" = "test" ]
    then
        if [ "$2" = ""  ]
        then
            oj t -c "python main.py"
        else
            oj "${@}"
        fi
    else
        npx acc "${@}"
    fi
}

cd $d/contests
source ../venv/bin/activate
alias deactivate="Deactivate"
alias acc="Acc"
alias vim="vim -S $d/.vim/atcoder.vim"
