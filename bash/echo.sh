#!/bin/bash

# echo options

# -e: enable back slash converting special char
# -E: disable back slash control (default)
# -n: cancel end of line's changing line identifier (same effect with \c)

# echo backslash control character

# \a: ALERT/BELL
# \b: BACKSPACE
# \c: cancel return
# \E: ESCAPE
# \f: FORMFEED
# \n: NEWLINE
# \r: RETURN
# \t: TAB
# \v: VERTICAL TAB
# \n: ASCII (xn hex)
# \\: backslash itself

# # example-1
# option: -e 
# enable back slash control character 

echo -e "a\tb\tc\nd\te\tf"

# using ascii instead
# FIXME: not working

echo -e "\141\011\142\011\143\012\144\011\145\011\146"

# using hex ascii 

echo -e "\x61\x09\x62\x09\x63\x0a\x64\x09\x65\x09\x66"

# \b: backspace
# \a: alert, FIXME: not working under virtual machine
echo -ne "a\tb\tc\nd\te\bf\a"
