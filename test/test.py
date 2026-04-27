# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles, Timer


@cocotb.test()
async def test_project(dut):
    dut._log.info("Start Full Adder Test")

    # Clock (not required, but kept for format)
    clock = Clock(dut.clk, 10, unit="us")
    cocotb.start_soon(clock.start())

    # Reset
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 5)
    dut.rst_n.value = 1

    # Test function
    async def apply_test(a, b, cin):

        # Apply inputs
        dut.ui_in.value = (cin << 2) | (b << 1) | a

        # Wait for combinational logic
        await Timer(1, unit="ns")

        # Expected outputs
        expected_sum = a ^ b ^ cin
        expected_cout = (a & b) | (b & cin) | (a & cin)

        # Read output
        val = int(dut.uo_out.value)
        sum_out = val & 0x1
        cout_out = (val >> 1) & 0x1

        dut._log.info(
            f"A={a} B={b} Cin={cin} -> "
            f"SUM={sum_out} COUT={cout_out}"
        )

        assert sum_out == expected_sum, "Sum mismatch"
        assert cout_out == expected_cout, "Carry mismatch"

    # All combinations
    await apply_test(0, 0, 0)
    await apply_test(1, 0, 0)
    await apply_test(0, 1, 0)
    await apply_test(1, 1, 0)
    await apply_test(0, 0, 1)
    await apply_test(1, 0, 1)
    await apply_test(0, 1, 1)
    await apply_test(1, 1, 1)

    dut._log.info("All tests passed ✅")
