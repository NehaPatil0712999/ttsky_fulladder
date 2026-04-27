# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles, Timer


@cocotb.test()
async def test_project(dut):
    dut._log.info("Start Full Adder Test")

    # Clock (kept for format consistency)
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

    # Function to test one case
    async def apply_test(a, b, cin):

        # Apply inputs (A=bit0, B=bit1, Cin=bit2)
        dut.ui_in.value = (cin << 2) | (b << 1) | a

        # Wait for combinational logic to settle
        await Timer(1, unit="ns")

        # Expected values
        expected_sum = a ^ b ^ cin
        expected_cout = (a & b) | (b & cin) | (a & cin)

        # Extract outputs correctly
        uo_val = int(dut.uo_out.value)
        sum_out = uo_val & 0x1
        cout_out = (uo_val >> 1) & 0x1

        # Debug print
        dut._log.info(
            f"A={a} B={b} Cin={cin} -> "
            f"SUM={sum_out} COUT={cout_out} | "
            f"Expected SUM={expected_sum} COUT={expected_cout}"
        )

        # Assertions
        assert sum_out == expected_sum, "Sum mismatch"
        assert cout_out == expected_cout, "Carry mismatch"

    # Test all 8 combinations
    await apply_test(0, 0, 0)
    await apply_test(1, 0, 0)
    await apply_test(0, 1, 0)
    await apply_test(1, 1, 0)
    await apply_test(0, 0, 1)
    await apply_test(1, 0, 1)
    await apply_test(0, 1, 1)
    await apply_test(1, 1, 1)

    dut._log.info("All test cases passed ✅")
