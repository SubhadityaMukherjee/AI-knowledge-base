---
title: Instruction Pipelining
tags: parallel 
date modified: Thursday, August 11th 2022, 12:32:52 am
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Instruction Pipelining
- used in the design of modern microprocessors, microcontrollers and CPUs to increase their [[Instruction Throughput]] for the entire workload
- divide the processing of a CPU instruction into a series of independent steps o microinstructions with storage at the end of each step.
- This allows the CPUs control logic to handle instructions at the processing rate of the slowest step, which is much faster than the time needed to process the instruction as a single step
- IF: Instruction Fetch
- ID: Instruction Decode, register fetch
- EX: Execution
- MEM: Memory Access
- WB: Register write Back

## Backlinks

> - [Instruction Level Programming](Instruction level programming.md)
>   - [[Instruction Pipelining]]

_Backlinks last generated 2022-10-04 13:01:19_
