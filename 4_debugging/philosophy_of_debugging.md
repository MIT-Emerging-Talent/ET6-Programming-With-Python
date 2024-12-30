# Philosophy of Debugging

> Adapted from Nick Parlante:
> [Debugging](https://web.stanford.edu/class/archive/cs/cs106a/cs106a.1184//handouts/9%20-%20Debugging.pdf)
> and [Debugging](https://cs.stanford.edu/people/nick/compdocs/Debugging.pdf)

Much of your time as a computer programmer will likely be spent debugging. This
phenomenon is best described by a quotation from one of the first computer
pioneers, Maurice Wilkes:

> As soon as we started programming, we found to our surprise that it wasn’t as
> easy to get programs right as we had thought. We had to discover debugging. I
> can remember the exact instant when I realized that a large part of my life
> from then on was going to be spent in finding mistakes in my own programs.
>
> — Maurice Wilkes, 1949

In order to be better prepared to undertake the more complex future debugging
that you will be doing, we aim to give you here both a sense of the philosophy
of debugging as well as to teach you how to use some of the practical tips that
make testing and debugging easier. The Philosophy of Debugging

Debugging is one of the most creative and intellectually challenging aspects of
programming. It can also be one of the most frustrating. To a large extent, the
problems that people face debugging programs are not so much technical as they
are psychological. To become successful debuggers, you must learn to think in a
different way. There is no cookbook approach to debugging, although Nick
Parlante’s 11 Truths of Debugging (given below) will probably help. What you
need is insight, creativity, logic, and determination. As computer scientists,
it is important to remember that the programming process leads you through a
series of tasks and roles:

| Task      | Role      |
| --------- | --------- |
| Design    | Architect |
| Coding    | Engineer  |
| Testing   | Vandal    |
| Debugging | Detective |

These roles require you to adopt distinct strategies and goals, and it is often
difficult to shift your perspective from one to another. Although debugging can
often be very difficult, it can be done. It will at times take all of the skill
and creativity at your disposal, but you can succeed if you are methodical and
do not give up on the task.

Debugging is an important skill that you will use every day if you continue in
Computer Science or any related field. Even though it is the final task of those
listed above, it is certainly not the least important. You should always plan
ahead and allow sufficient time for testing and debugging, as it is required if
you expect to produce quality software. In addition, you should make a
concentrated effort to develop these skills now, as they will be even more
important as programs become more complicated later in the quarter.

## 11 Truths of Debugging

1. Intuition and hunches are great—you just have to test them out. When a hunch
   and a fact collide, the fact wins. That's life in the city.
2. Don’t look for complex explanations. Even the simplest omission or typo can
   lead to very weird behavior. Everyone is capable producing extremely simple
   and obvious errors from time to time. Look at code critically—don’t just
   sweep your eye over that series of simple statements assuming that they are
   too simple to be wrong.
3. The clue to what is wrong in your code is in the values of your variables and
   the flow of control. Try to see what the facts are pointing to. The computer
   is not trying to mislead you. Work from the facts.
4. Be systematic and persistent. Don’t panic. The bug is not moving around in
   your code, trying to trick or evade you. It is just sitting in one place,
   doing the wrong thing in the same way every time.
5. If you code was working a minute ago, but now it doesn’t—what was the last
   thing you changed? This incredibly reliable rule of thumb is the reason your
   section leader told you to test your code as you go rather than all at once.
6. Do not change your code haphazardly trying to track down a bug. This is sort
   of like a scientist who changes more than one variable in an experiment at a
   time. It makes the observed behavior much more difficult to interpret, and
   you tend to introduce new bugs.
7. If you find some wrong code that does not seem to be related to the bug you
   were tracking, fix the wrong code anyway. Many times the wrong code was
   related to or obscured the bug in a way you had not imagined.
8. You should be able to explain in Sherlock Holmes style the series of facts,
   tests, and deductions that led you to find a bug. Alternately, if you have a
   bug but can’t pinpoint it, then you should be able to give an argument to a
   critical third party detailing why each one of your functions cannot contain
   the bug. One of these arguments will contain a flaw since one of your
   functions does in fact contain a bug. Trying to construct the arguments may
   help you to see the flaw.
9. Be critical of your beliefs about your code. It’s almost impossible to see a
   bug in a function when your instinct is that the function is innocent. Only
   when the facts have proven without question that the function is not the
   source of the problem should you assume it to be correct.
10. Although you need to be systematic, there is still an enormous amount of
    room for beliefs, hunches, guesses, etc. Use your intuition about where the
    bug probably is to direct the order that you check things in your systematic
    search. Check the functions you suspect the most first. Good instincts will
    come with experience.
11. Debugging depends on an objective and reasoned approach. It depends on
    overall perspective and understanding of the workings of your code.
    Debugging code is more mentally demanding than writing code. The longer you
    try to track down a bug without success, the less perspective you tend to
    have. Realize when you have lost the perspective on your code to debug. Take
    a break. Get some sleep. You cannot debug when you are not seeing things
    clearly. Many times a programmer can spend hours late at night hunting for a
    bug only to finally give up at 4:00A.M. The next day, they find the bug in
    10 minutes. What allowed them to find the bug the next day so quickly? Maybe
    they just needed some sleep and time for perspective. Or maybe their
    subconscious figured it out while they were asleep. In any case, the “go do
    something else for a while, come back, and find the bug immediately”
    scenario happens too often to be an accident.

## Show me where your code hurts

When you write a program, you have a mental plan in mind of what you are trying
to compute. The program itself is an extremely unambiguous plan of some
computation. A bug is when these two plans diverge. Unfortunately, you do not
observe the bug directly. Instead you see a symptom produced by the underlying
bug. Your job is to work backward from the symptom to find the bug which
produced it. The line in your code which contains the bug will have the
following property. Before that line, the values of your variables were ok.
After that line executes, some of the values are wrong.

There are three basic themes in trying track down the bug. You can work backward
linearly from the symptom trying to find the line which took in good values but
produced bad values. You can trace forward from the beginning of your program,
looking for the values to go bad. Or you can do a sort of "binary search" in
your code with break points, narrowing in on the bug by seeing if it lays before
or after each trial breakpoint. People develop a personal craft for how they
like to debug— the key is to be methodical.

What you want to avoid is the worst case: you've probed around in your code for
a few hours without success. You've looked at a lot of your functions but can
find nothing wrong. You begin to change around the code in functions in an
effort to fix the elusive bug. The problem here is that you are not really
getting any closer to finding the bug. It's sort of like looking for a diamond
ring on a football field. If you just stroll around at random you may find it.
But if after a couple hours you haven't found it-- then are not much better off
than when you started since you don't know where you've looked and where you
haven't. The most important quality about the following strategy is that by
being systematic, you always know which part of the field you've checked.

## The Solution

Identify the line which corresponds to the symptom. This is typically is very
simple. For the above example the symptom corresponds to the line where the
variable went out of bounds or to the `print`s which produced the garbage output.
The incorrect behavior will correspond to a variable with a bad value. Identify
the variable(s) with bad values. For this example, suppose that the program
crashes on line 112 because i is -1 and tries to index an list.

The critical question is: where did i get its value? There are basically three
ways a variable can get a value: the variable appears on the left hand side of a
`=`, a reference to the variable is passed to somebody who changes it, or there is
a bad pointer reference somewhere which is accidentally scribbling on the
variable. Arguably a fourth way is if the variable is never initialized and so
gets a random value. Writing your code with good style: sensibly used
parameters, no global variables should make it easier to identify what bit of
code could be changing your variable.

In this example, i is wrong on line 112. Look above line 112 searching for the
most recent line which changes i. Suppose line 108 passes i as a reference and
so is suspect. Put a breakpoint or printf just before line 108 to examine i. If
i is correct before 108 but wrong after, then 108 is the problem. If i was
already wrong, then you must probe further backward. If working backwards
doesn't reveal the good values/bad values transition, it can be easier to
sprinkle prints or asserts at the very beginning of a few functions just to find
the general area where things are going wrong.

One starting strategy which doesn't require any breakpoints is to step over the
functions in main() without stepping into any one. Keep an eye on your data
state after each step to see which function messes things up. Of course, if you
didn't decompose out the basic phases of your program, then this won't work.

## Deer in the Headlights

The key is not to lock up in deer-in-the-headlights mode when overwhelmed with
the enormity of the problem. You are never more than a couple well-placed break
point examinations away from seeing the problem. Try think about which
breakpoint will implicate/exonerate the largest amount of code with the least
work.
