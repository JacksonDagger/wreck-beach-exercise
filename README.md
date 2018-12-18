# wreck-beach-exercise
You are at Wreck Beach, and it's been a tiring day. You have a stamina level that is represented by an integer **stamina,** where 0 ≤ stamina ≤ 1000.

To get back home, you will need to make the climb back, and the stairs are behaving strangely today. There are **n** stairs to climb and each stepping on a stair drains some stamina. The amount of stamina that you lose when you step of the i-th stair is **stair[i]** where **stair is an array of length n,** with stair[0] corresponding to the first stair and stair[n-1] corresponding to the last stair.

You want to reach the top of the stairs with a positive stamina level (> 0). If you are at stair[j], 0 ≤ j ≤ n-2, or before you take the first step, you have a few choices: 

- **Normal Step:** You can take a normal step to reach the next immediate stair, and this does not require any extra stamina. By taking a normal step, you will lose stair[j+1] stamina;
- **Big Step:** You can take a big step, which allows you to skip one stair, and in this case you will reach the (j+2)-th stair and lose an additional 1 point stamina;
- **Jump:** You can jump and this allows you to skip two stairs and you will reach the (j+3)-th stair but will lose an additional 2 points of stamina.

**What is the maximum amount of stamina you can be left with when you complete the climb?** You can skip any of the stairs using a big step or a jump. A big step or a jump past the last stair will get you to the road, which is your destination.

To answer this question, implement the method **maxStamina** that takes as input the array **stair** and the initial stamina level **stamina**. If it is not possible to reach the top with positive stamina, throw an `InsufficientStaminaException`.
