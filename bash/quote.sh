#!/bin/bash

# shell meta

# IFS: <space>(more often), <tab> or <enter> constructing 
# CR : <enter>
# =  : equal sign
# $  : for variables or expression replace
# >  : redirect to stdout
# <  : redirect to stdin
# |  : command pipeline
# &  : redirect file descriptor, or set command background running
# () : inner commands running in nested subshell, or for replacing calculation/commands
# {} : inner commands running under non-named function, or indicating span
#      in variables replacing
# ;  : ignore former command's return value and continually perform next command 
# && : perform next command only if former one return true
# || : perform next command only if former one return false
# !  : perform history's commands

# three quoting using:
# * hard quote : '', ignore all META
# * soft quote : "", reserve part of META, like $
# * escape     : \ , igoore META after \

# example-1:
# <enter> using : CR/IFS/NL(New Line)/FF(Form Feed)/NULL...

# under hard quote
# <enter> inner '', just new-line not as <CR>
A='B
C
'

echo "$A"

# under soft quote
A="B
C
"

# A is not in soft quote, so <enter> as IFS , not new-line
echo $A

# after \ <enter> is ignored, but the last one
A=B\
C\

echo $A

# example-2:
# soft quote vs. hard quote

A=B\ C

echo "$A"
# $ is ignored
echo '$A'
