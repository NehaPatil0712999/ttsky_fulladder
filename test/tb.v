`default_nettype none
`timescale 1ns / 1ps

module tb ();

  // Dump waveform
  initial begin
    $dumpfile("tb.fst");
    $dumpvars(0, tb);
    #1;
  end

  // Inputs
  reg clk;
  reg rst_n;
  reg ena;
  reg [7:0] ui_in;
  reg [7:0] uio_in;

  // Outputs
  wire [7:0] uo_out;
  wire [7:0] uio_out;
  wire [7:0] uio_oe;

`ifdef GL_TEST
  wire VPWR = 1'b1;
  wire VGND = 1'b0;
`endif

  // Instantiate your Full Adder module
  tt_um_full_adder user_project (

`ifdef GL_TEST
      .VPWR(VPWR),
      .VGND(VGND),
`endif

      .ui_in  (ui_in),
      .uo_out (uo_out),
      .uio_in (uio_in),
      .uio_out(uio_out),
      .uio_oe (uio_oe),
      .ena    (ena),
      .clk    (clk),
      .rst_n  (rst_n)
  );

  // Test stimulus
  initial begin
    // Initialize
    clk   = 0;
    rst_n = 0;
    ena   = 1;
    ui_in = 0;
    uio_in = 0;

    #10 rst_n = 1;

    // Apply all Full Adder combinations (A=ui_in[0], B=ui_in[1], Cin=ui_in[2])

    ui_in = 8'b00000000; #10; // A=0 B=0 Cin=0
    ui_in = 8'b00000001; #10; // A=1 B=0 Cin=0
    ui_in = 8'b00000010; #10; // A=0 B=1 Cin=0
    ui_in = 8'b00000011; #10; // A=1 B=1 Cin=0
    ui_in = 8'b00000100; #10; // A=0 B=0 Cin=1
    ui_in = 8'b00000101; #10; // A=1 B=0 Cin=1
    ui_in = 8'b00000110; #10; // A=0 B=1 Cin=1
    ui_in = 8'b00000111; #10; // A=1 B=1 Cin=1

    #20 $finish;
  end

endmodule
