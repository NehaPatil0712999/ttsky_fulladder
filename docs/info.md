<!---

This file is used to generate your project datasheet. Please fill in the information below and delete any unused
sections.

You can also include images in this folder and reference them in the markdown. Each image must be less than
512 kb in size, and the combined size of all images must be less than 1 MB.
-->

## How it works

This project implements a 1-bit Full Adder using combinational logic.

A full adder adds three binary inputs:

A
B
Cin (Carry-in)

The design produces two outputs:

Sum
Cout (Carry-out)
Logic used:
Sum = A ⊕ B ⊕ Cin
Cout = (A & B) | (B & Cin) | (A & Cin)
Input Mapping:
ui_in[0] → A
ui_in[1] → B
ui_in[2] → Cin
Output Mapping:
uo_out[0] → Sum
uo_out[1] → Carry (Cout)

All remaining input and output bits are unused and set to 0.

This is a pure combinational circuit, meaning:

No clock dependency
No memory elements (flip-flops)
Output changes immediately with input

## How to test

Step 1: Take input values

Choose values for:

A = 0 or 1
B = 0 or 1
Cin = 0 or 1
Step 2: Substitute in formulas

Example:

👉 A = 1, B = 0, Cin = 1

Sum calculation:

S=1⊕0⊕1=0

Carry calculation:

C
out
	​

=(1⋅0)+(0⋅1)+(1⋅1)=1
Step 3: Compare with output
Check if your circuit gives:
Sum = 0
Cout = 1

If yes ✅ → correct
If no ❌ → error in design

## External hardware

no hardware is required
