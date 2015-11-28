================
如何同步代码片段
================

:date: 2015-10-18
:slug: how-to-keep-code-snippet-stay-in-sync
:lang: zh-cn


因为21天学通Erlang是面向零基础的初学者的，长一点的代码肯定不会是一次写成的，是要分成很多步的。为了方便读者参考，同时也是为了能检验这中间每一步是不是真的没问题，所以每一步都会有一个单独文件，这个文件也要以和最终结果一样的方式检查。假如一个代码片段同时出现在很多个文件里，为了改这个片段，得同时编辑这些文件。这样真是非常非常麻烦，更大的麻烦是没办法检查同一个代码片段在多个文件里是否一致。

于是，我们用\ :code:`snip.py`\ 来应付这些问题。给代码片段起个名字，比如下面这个例子中叫my-first-snippet，把代码片段写在\ :code:`% SNIP BEGIN`\ 和 \ :code:`% SNIP END`\ 之间，这样就可以根据名字来判断是不是同一个片段了。

.. code::

    % SNIP BEGIN my-first-snippet
    hello() ->
        world.
    % SNIP END

运行\ :code:`snip.py build`\ 之后，这些注释都会被删掉，就变成下面这样。

.. code::

    hello() ->
        world.


Erlang中还有一种特殊的情况，clause之间是用\ :code:`;`\ 分开的，但是最后一个clause结尾处用的是\ :code:`.`\ 。此时可以用\ :code:`%- SNIP END`\ 。这样build后，会把注释前后两行接成一行，不会出现\ :code:`;`\ 和\ :code:`.`\ 分别单独占一行的情况。比如下面这个例子中，在第一个文件里，只有一个clause。

.. code::

    % SNIP BEGIN my-second-snippet
    hello(1) ->
        world
    %- SNIP END
    .

运行\ :code:`snip.py build`\ 之后，就变成下面这样。

.. code::

    hello(1) ->
        world.


在第二个文件里，有两个clause。

.. code::

    % SNIP BEGIN my-second-snippet
    hello(1) ->
        world
    %- SNIP END
    ;
    hello(2) ->
        big_world.

运行\ :code:`snip.py build`\ 之后，就变成下面这样。

.. code::

    hello(1) ->
        world;
    hello(2) ->
        big_world.


因为恰好LaTeX和Erlang注释用的都是\ :code:`%`\ 。可以在LaTeX文档里也可以用同样的记号。为了能在PDF里看到代码片段所在的文件名和行号，需要使用\ :code:`% SNIP REFERENCE`\ 。

.. code::

    % SNIP REFERENCE hello.erl my-first-snippet
    \begin{SourceCode}
    % SNIP BEGIN my-first-snippet
    hello(1) ->
        world.
    % SNIP END
    \end{SourceCode}


修改过代码后，运行\ :code:`snip.py status`\ 会列出所有不同步的代码片段的名字，接着就可以用\ :code:`snip.py sync`\ 来选择某个文件里的片段，把所有文件里的同名代码片段都修改成一样的。
