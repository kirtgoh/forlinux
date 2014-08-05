#!/bin/bash

# Read the name of user and print hello
echo "Hello! What's your name?"
read name
echo "Welcome, $name"

# Single quotes prevent expansion of the variable
echo 'Your name has been stored in $name'
