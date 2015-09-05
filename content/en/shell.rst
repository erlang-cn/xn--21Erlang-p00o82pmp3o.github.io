==================================
How to verify Erlang shell session
==================================

:date: 2015-10-11
:slug: how-to-verify-erlang-shell-session
:lang: en


There are quite a few Erlang shell session, in the book Teach Yourself
Erlang In 21 Days, since this book is targeted to absolute
beginners. It is tedious and error-prone to verify them manually every
time the PDF is generated.

To help finding out all the sessions in the LaTeX source, we first
define a new environment ErlangShellSession. It will write each
session out to a separate file.

.. code:: latex

    \newcounter{erlangshellsession}[section]
    \newoutputstream{erlangshellsession}
    \newenvironment{ErlangShellSession}{
    \stepcounter{erlangshellsession}
    \openoutputfile{\currfiledir\theerlangshellsession.session}{erlangshellsession}
    \writeverbatim{erlangshellsession}
    }{
    \endwriteverbatim
    \closeoutputstream{erlangshellsession}
    \begin{SingleSpacing}
    \lstinputlisting[title={Erlang Shell}]{\currfiledir\theerlangshellsession.session}
    \end{SingleSpacing}}

We then verify these files. Unfortunately, OTP does not include
anything close to Python's doctest. Joe Armstrong, creator of Erlang,
also asked for this on the Erlang-Questions mailing list recently\
[#interface]_\ .

Erlang Shell is `a bit more (and less) than REPL`__\ , and not well
documented. The process, which starts the shell, should set itself as
the `group leader`__ of the shell, and communicate with it via `I/O
protocol`__\ . When a :code:`get_until` message is received, just send
the shell what it wants. When a :code:`put_chars` message is received,
we compare the characters with those read from the session file. When
all have been sent or compared and nothing has gone wrong, the file is
verified, we then send :code:`eof` to the shell, and wait until it
terminates.


.. [#interface] `Programmatic interface to the shell <http://erlang.org/pipermail/erlang-questions/2015-August/085420.html>`_

.. __: http://ferd.ca/repl-a-bit-more-and-less-than-that.html
.. __: http://www.erlang.org/doc/man/erlang.html#group_leader-0
.. __: http://www.erlang.org/doc/apps/stdlib/io_protocol.html
