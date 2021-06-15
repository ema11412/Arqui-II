
module alfa_top (HEX0, HEX1, HEX2, HEX3, HEX4, HEX5, KEY, LEDR, SW);

	output logic [6:0] HEX0, HEX1, HEX2, HEX3, HEX4, HEX5;
	output logic [9:0] LEDR;
	input logic [3:0] KEY;
	input logic [9:0] SW;
	
	fullAdder FA (.A(SW[2]), .B(SW[1]), .cin(SW[0]), .sum(LEDR[0]), .cout(LEDR[1]));
	
	assign HEX0 = 7'b1111111;
	assign HEX1 = 7'b1111111;
	assign HEX2 = 7'b1111111;
	assign HEX3 = 7'b1111111;
	assign HEX4 = 7'b1111111;
	assign HEX5 = 7'b1111111;
	
endmodule

module alfa_top_testbench();
	logic [6:0] HEX0, HEX1, HEX2, HEX3, HEX4, HEX5;
   logic [9:0] LEDR;
	logic [3:0] KEY;
	logic [9:0] SW;
	
	alfa_top dut (.HEX0, .HEX1, .HEX2, .HEX3, .HEX4, .HEX5, .KEY, .LEDR, .SW);
	
	integer i;
	initial begin
		SW[0] = 1'b0;
		SW[1] = 1'b0;
		
		for (i=0; i< 2**8; i++) begin
			SW[7:0] = i; #10;
		end // for loop
	
	end
	
endmodule
