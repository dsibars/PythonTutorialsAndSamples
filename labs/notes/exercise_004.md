## Goals for exercise 004

- #### Modifications in friend class
Now, there are 3 levels for salutation: Hate, standard and Love.<br>
Add another additional standard sentence for each say method.<br>
If the levels are between 3 and 7, instead of saying the standard sentence,
the Friend will salutate randomly between the two standard sentences. <br>
The exception is level 5: With this specific level, you will say always the first standard sentence. This will make also that the Test 001 will work.

For example: <br>
<ul>
<li>the friend level is 4</li>
<li>we added the additional standard sentence: "Whats Up {FriendName}!" </li>
<li>Friend name is Paco, and friend of is Meralgo</li>
<li>we say salutate 4 times,it could say: 
<ul>
<li> Hello my Friend Meralgo. How are you?</li>
<li> Hello my Friend Meralgo. How are you?</li>
<li> Whats Up Meralgo!</li>
<li> Hello my Friend Meralgo. How are you?</li>
</ul>
</ul>
<br>


HOWEVER, YOU WILL DO THIS PART LAST, FIRST DO THE NEXT POINT! :)


- #### Create test file test_004
In this exercise, you will create your own test, and the purpose is to do it
before modifying the class.<br>
There will be, at least (additional tests will give you more points) the next tests:
<ul>
<li>With a friend level 7, call 10 times the method salutate and check the result: assert that both standard sentences are present (it does not 
matter how many times 
apperars each one, we only validate that in 10 executions both apperars).<br>
Do the same with friend level 3, 4 and 6. Try to not repeat the code, and think about a way to execute the same test with different friend levels.
</li>
<li>
With a friend level 7, call 10 times the method present_yourself and check the result, assert that both standard sentences are present (it does not 
matter how many times 
apperars each one, we only validate that in 10 executions both apperars).<br>
Do the same with friend level 3, 4 and 6. Try to not repeat the code, and think about a way to execute the same test with different friend levels.
</li>
<li>
With a friend level 7, call 40 times the method say_all and check the result, assert that all 4 standard combinations are present  (it 
does not 
matter how many times 
apperars each one, we only validate that in 10 executions both apperars).<br>
Do the same with friend level 3, 4 and 6. Try to not repeat the code, and think about a way to execute the same test with different friend levels.
</li>
</ul>
