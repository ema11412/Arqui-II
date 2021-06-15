module instr_fetch(input logic clk, rst, stall,
					    input logic [1:0]NextInstr,
						 input logic [31:0] address, Rs, Branch,
						 
						 output logic [31:0] PC);

						 
	
	logic[31:0] pcPlus4, nextPC;
	
	mux_Ifetch mux_fetch (NextInstr, pcPlus4, address, Rs, Branch, nextPC);
	
	syncRegister PC_REG (clk, rst, stall, nextPC, PC);
	
	add4 pcP4 (PC, pcPlus4);
	
endmodule