# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles


@cocotb.test()
async def test_project(dut):
    dut._log.info("Start Full Adder Test")

    # Clock (not required for combinational logic, but kept for format)
    clock = Clock(dut.clk, 10, unit="us")
    cocotb.start_soon(clock.start())

    # Reset
    dut._log.info("Reset")
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 5)
    dut.rst_n.value = 1

    dut._log.info("Applying test cases")

    # Function to apply inputs and check outputs
    async def apply_test(a, b, cin):
        # Pack inputs into ui_in
        dut.ui_in.value = (cin << 2) | (b << 1) | a
        await ClockCycles(dut.clk, 1)

        # Expected values
        expected_sum = a ^ b ^ cin
        expected_cout = (a & b) | (b & cin) | (a & cin)

        dut._log.info(f"A={a} B={b} Cin={cin} -> Sum={expected_sum} Cout={expected_cout}")

        assert dut.uo_out.value[0] == expected_sum, "Sum mismatch"
        assert dut.uo_out.value[1] == expected_cout, "Carry mismatch"

    # All combinations
    await apply_test(0, 0, 0)
    await apply_test(1, 0, 0)
    await apply_test(0, 1, 0)
    await apply_test(1, 1, 0)
    await apply_test(0, 0, 1)
    await apply_test(1, 0, 1)
    await apply_test(0, 1, 1)
    await apply_test(1, 1, 1)

    dut._log.info("All test cases passed ✅")
