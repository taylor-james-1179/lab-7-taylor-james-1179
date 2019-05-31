# CS162 Lab 7

1. Clone this repository to your development computer.

1. (optional) Open the file `.travis.yml` and enter your email address in place of "`user@example.com`". This will ensure that you are notified about the success or failure of the automated tests that are run against your code.

   ```yaml
   notifications:
     email:
       recipients:
         - user@example.com
       on_success: always
       on_failure: always
   ```

1. Don't forget that docstrings are a requirement for your code. Example module and function docstrings are provided below.

   ```python
   """
   Brief assignment description.

   Longer, more detailed explanation of your solution. This may be anywhere from
   a couple of sentences to several paragraphs depending on how complex the
   assignment is. It should be detailed enough that someone who has never seen the
   code can understand what it does just by reading this explanation. You may
   also want to include examples of using the program if it accepts command line
   arguments.

   Your name
   Your partner's/collaborator's name
   """
   ```

   ```python
    def random_number_generator(arg1, arg2):
    """
    Summary line.

    Extended description of function.

    Parameters
    ----------
    arg1 : int
        Description of arg1.
    arg2 : str
        Description of arg2.

    Returns
    -------
    int
        Description of return value. This may be omitted if the function does not explicitly return a value.

    """
   ```

## Exercises

This last lab of the term is meant to be fun! In it you'll work to create algorithmic solutions to a couple of engaging and entertaining problems. Yes, you can find solutions to them online if you look. I _strongly_ encourage you not to, however. Instead, concentrate on understanding the problem and finding _your own_ solution to it. And have fun along the way!

### You Will All Conform

> When people are free to do as they please, they usually imitate each other. – Eric Hoffer

**Programming constructs and algorithmic paradigms covered in this puzzle: Lists, tuples, functions, control flow including if statements and for loops, and print statements.**

Let’s say we have a whole bunch of people in line waiting to see a baseball game. They are all hometown fans and each person has a team cap and is wearing it. However, not all of them are wearing the caps in the same way – some are wearing their caps in the normal way, and some are wearing them backwards.

People have different definitions of normal and backwards but you, the gatekeeper thinks that the cap on the left below is being normally worn and the one on the right is being worn backwards.

![alt](/images/hats.png)

You are the gatekeeper and can only let them in to the stadium if the entire group has their caps on in the same way – either all forwards or all backwards. Because everyone has different definitions of forward and backward, you can’t tell them to wear their cap forwards or backwards. You can only tell them to flip their caps. The good news is that each person knows what position they are in the line, starting with the first person having position 0 and the last one position n – 1. You can say things like:

    "Person in position i please flip your cap."
    "People in positions i through j (inclusive) please flip your caps."

What you would like to do is to minimize the number of requests you have to shout out
to save your voice. Here is an example:

![alt](/images/example1.png)

We have 13 people standing in line in positions 0 through 12 inclusive. Since there are six people with caps on forwards, we could shriek out 6 commands, e.g.,

    Person in position 0 please flip your cap.

And repeat for person in positions 1, 5, 9, 10 and 12. A voice-saving measure would exploit the second type of command and only yell out four commands:

    People in positions 0 through 1 please flip your caps.
    Person in position 5 please flip your cap.
    People in positions 9 through 10 please flip your caps.
    Person in position 12 please flip your cap.

And this will get everyone to have caps on backwards.

However, in this example, we can do one better. If we scream out:

    People in positions 2 through 4 please flip your caps.
    People in positions 6 through 8 please flip your caps.
    Person in position 11 please flip your cap.

This will get everyone with caps on forwards.

#### Part 1

Write a function that given a list cap directions in the form `['F', 'F', 'B', 'B', 'B', 'F', 'B', 'B', 'B', 'F', 'F', 'B', 'F' ]` will generate the minimum number of commands to get all hats worn in the same way? Using the list above, the output should be:

        Person in position 2 through 4 please flip your cap!
        Person in position 6 through 8 please flip your cap!
        Person in position 11 through 11 please flip your cap!

**Bonus challenge:** Can you think of a way of generating all the commands as you walk down the line for the first time (i.e. in a single pass)?

#### Part 2

As you may have noticed, the output from `part_1` doesn't always read well. For example,

        Person in position 11 through 11 please flip your cap!

sounds awkward and would be better phrased as

        Person in position 11 please flip your cap!

Using your solution to `part_1` as a starting point, modify your code so that it generates output like the line above. With your new code and the input `['F', 'F', 'B', 'B', 'B', 'F', 'B', 'B', 'B', 'F', 'F', 'B', 'F' ]` your output should be:

        Person in position 2 through 4 please flip your cap!
        Person in position 6 through 8 please flip your cap!
        Person in position 11 please flip your cap!

Due 11:59:59PM, June 6.
