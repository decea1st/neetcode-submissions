class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for i, n in enumerate(temperatures):
            while stack and n > temperatures[stack[-1]]:
                index = stack.pop()
                res[index] = i - index
            stack.append(i)
        return res








        # [1, 4, ]
        # I think 38 can be removed from the stack because I reached its index
        # At 38, I find 30 which isn't the answer, then 36, then 35, then finally 40
        # I think I should be adding the indices not the elemnts
        # So I guess I add all those indices in the monotonic stack which ends up looking like:
        # [2, 4, 3, ] - At 2 it's 30, then 35, then 36, then I find 40 which is my answer 
        # Now, should I be adding the 40 index? I think the issue is that I don't fully understand
        # the use of this stack. I'm at index 2 right now. How can I use this stack? I know the
        # temperature here is 30, if I have to scan this stack then that defeats the purpose. 
        # The stack is sorted. How can I use that? What if the stack was sorted in the opposite
        # direction? Right now highest goes on top. What if lowest was on top? No that doesn't make
        # because I want to be able to peek / pop and it should return the highest. If I DO search this
        # stack now and pop as I go through it, does it help in future searches? So I'd be starting my 
        # search with checking 40 but that would be wrong since it's higher but not the next higher. 
        # Maybe that supports sorting it the opposite way. Let's see what that looks like. 
        # I'd start at 30, I'd check that 38 is the next one so I add 1 to result and index 1 
        # [1, 4, 1, 2, 1]
        # [5]
        # Then I go to the next element which is 38 so I need to search for something higher
        # I see 30, add to stack, then 36 at the bottom, 35 in the middle. 40 at bottom. 
        # I append difference between self and index of 40. Then the next temperature is 30 at index 2
        # The first thing in the stack is 2 which is self so pop, the one higher than that is 4
        # This now actually helps me find my answer. Maybe I'm on the right track. Let's keep going.
        # Next is 36 at index 3. I look at my stack and first one is 4 but the temperature is 35 there.
        # So I guess I keep going? Then it's self and then finally it's 40 so I append the difference to res
        # Then the next element is 35 at index 4 so I search my stack and see the first one is self so pop
        # Next element is less so pop. Then it's 40 which is correct. Append the difference. I'm approaching
        # the correct output that the input would expect but this doesn't feel like monotonic stacks still.
        # The stack is my only source of answers, I never search the input. Wow what a great and intuitive solution that I would totally think of. 
        # I append 30 to stack. I go next because fuck me I guess? I leave the problem for a different day. 
        # Next element is 38. I check the stack and see if it solves anything. The first is 30 and it's solved. 
        # So pop because it won't be needed anymore because it's in the past. Append current index to res and stack both
        # Next is 30. Check stack to see if it solves anything. No it doesn't. Append it and fuck off I guess. 
        # Next element is 36. Does it solve anything? Yes it solves 30. Append current index for 30. Idk how to append in the right position but that is trivial compared to everything else. 