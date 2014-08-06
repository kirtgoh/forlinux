Get processor's core dump
-------------------------

Enable core dump

    $ ulimit -c [ulimit|1024]

and ,use it

    $ gdb -c core ./name
