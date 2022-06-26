---
title: Out of Order Execution
tags: parallel 
---

# Out of Order Execution
- allow the processor to avoid a class of delays that occur when the data needed to perform an operation are unavailable
- Instruction fetch.
- Instruction dispatch to an instruction queue (also called instruction buffer)
- The instruction waits in the queue until its input operands are available.
- The instruction is issued to the appropriate functional unit and executed by that unit.
- The results are queued (Re-order Buffer).
- Only after all older instructions have their results written back to the register file, then this result is written back to the register.








































































