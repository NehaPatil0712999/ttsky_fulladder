/*
 * Full Adder - Tiny Tapeout Format
 */

`default_nettype none

module tt_um_full_adder (
    input  wire [7:0] ui_in,    // Inputs
    output wire [7:0] uo_out,   // Outputs
    input  wire [7:0] uio_in,   
    output wire [7:0] uio_out,  
    output wire [7:0] uio_oe,   
    input  wire       ena,      
    input  wire       clk,      
    input  wire       rst_n     
);

    // Assign inputs
    wire A   = ui_in[0];
    wire B   = ui_in[1];
    wire Cin = ui_in[2];

    // Full Adder Logic
    wire Sum  = A ^ B ^ Cin;
    wire Cout = (A & B) | (B & Cin) | (A & Cin);

    // Assign outputs
    assign uo_out[0] = Sum;
    assign uo_out[1] = Cout;

    // Unused outputs set to 0
    assign uo_out[7:2] = 0;
    assign uio_out = 0;
    assign uio_oe  = 0;

    // Prevent warnings for unused signals
    wire _unused = &{ena, clk, rst_n, uio_in, 1'b0};

endmodule
