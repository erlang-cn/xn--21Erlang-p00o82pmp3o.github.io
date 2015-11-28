========================
核对Erlang Shell会话的记录
========================

:date: 2015-10-11
:slug: how-to-verify-log-of-erlang-shell-session
:lang: zh-cn


和其他脚本语言的入门教程一样，21天学通Erlang里也会有很多Shell会话的记录。每次生成PDF时，都去人工检查一遍，不仅费时费力，还很容易出错。

为了方便检查这些记录，定义ErlangShellSession这个environment，把LaTeX文档中所有Erlang Shell会话记录输出到单独的文件，这样接下来就只要分别检查这些文件就可以了。


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


很糟糕的是，OTP并没有包含类似Python里的doctest的功能。Erlang作者之一，Joe Armstrong不久前也在Erlang Questions邮件列表上问如何实现类似的功能\ [#interface]_\ 。

Erlang Shell\ `和一般的REPL在功能上有些出入`__\ ，而且文档也不全。启动Shell的process，得先把自己设置成\ `group leader`__\ ，这样才能以\ `I/O protocol`__\ 与Shell通信。收到\ :code:`get_until`\ 消息，那么就向Shell发送他想要的内容。收到\ :code:`put_chars`\ 消息，就把这些字符和记录去比较。假如所有记录内容都已经比较完了，也没有出现不同，那么就向Shell发送\ :code:`eof`\ 消息，等Shell退出。


.. [#interface] `Programmatic interface to the shell <http://erlang.org/pipermail/erlang-questions/2015-August/085420.html>`_

.. __: http://ferd.ca/repl-a-bit-more-and-less-than-that.html
.. __: http://www.erlang.org/doc/man/erlang.html#group_leader-0
.. __: http://www.erlang.org/doc/apps/stdlib/io_protocol.html
