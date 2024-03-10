# PDB — Python Debugger - это встроенный продвинутый модуль, который позволяет запустить командно отладчик для поиска ошибок в процессе самой программы.
# Запускается он путем указания команды: 
import pdb
pdb.set_trace()
# или
breakpoint()
# Команда continue продолжит работу программы после бейкпоинта
# Также можно вызвать python debugger напрямую из консоли, для отладки других скриптов по команде:
# python -m pdb myscript.py
# Если это было запущено после работы или краша программы, она будет запущена повторно для отладки.

# Модули команды pdb. :
    # pdb.run(statement, globals=None, locals=None)
    # Запускает указанный по имени скрипт или класс в режиме отладки. Позволяет указать использование глобальных или локальных переменных.

    # pdb.runeval(expression, globals=None, locals=None)
    # Схоже с .run, но также возвращает значение скрипта 

    # pdb.runcall(function, *args, **kwds)
    # Вызывает функцию, но возвращает все указанные в нее данные

    # pdb.set_trace(*, header=None)
    # Запускает режим отладки сразу после указания команды.

    # pdb.post_mortem(traceback=None)
    # Запускает режим отладки "пост-мортем", то есть после появления ошибки.

    # pdb.pm()
    # Запускае последний завершенный скрипт из sys.last_traceback в режиме отладки

# Debugger Commands - команды режима отладки:
    # h(elp) [command] - Распечатка 
    # w(here)
    # d(own) [count]
    # u(p) [count]
    # b(reak) [([filename:]lineno | function) [, condition]]
    # tbreak [([filename:]lineno | function) [, condition]]
    # cl(ear) [filename:lineno | bpnumber ...]
    # disable bpnumber [bpnumber ...]
    # enable bpnumber [bpnumber ...]
    # ignore bpnumber [count]
    # condition bpnumber [condition]
    # commands [bpnumber]
    # s(tep)
    # n(ext)
    # unt(il) [lineno]
    # r(eturn)
    # c(ont(inue))
    # j(ump) lineno
    # l(ist) [first[, last]]
    # a(rgs)
    # p expression
    # pp expression
    # whatis expression
    # source expression
    # display [expression]
    # undisplay [expression]
    # interact
    # alias [name [command]]
    # unalias name
    # ! statement
    # run [args ...]
    # restart [args ...]
    # debug code
    # retval
    # q(uit)
