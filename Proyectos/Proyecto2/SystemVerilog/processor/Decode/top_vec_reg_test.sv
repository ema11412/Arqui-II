`timescale 1 ps / 1 ps

module top_vec_reg_test;

logic WriteEn,clk;
logic [4:0] Rs1, Rs2,rd;
logic [255:0]InputData;
logic [255:0]Rout1, Rout2;

	top_vec_reg DUT (WriteEn,clk,Rs1,Rs2,rd,InputData,Rout1,Rout2);
	
	initial begin
		WriteEn = 0;
		clk = 0;
		Rs1 = 5'd16;
		Rs2 = 5'd18;
		rd = 5'd16;	 
		#5 InputData = 256'd100;
		
		
		#7 WriteEn = 1;
		#7 WriteEn = 0;
		
		#5 rd = 5'd18;
		
		#7 WriteEn = 1;
		#7 WriteEn = 0;
	
	end
	
	always
		#5 clk <= !clk;

endmodule
