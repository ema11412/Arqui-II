`timescale 1 ps / 1 ps
module deco_PC_test();
	
	logic [1:0] BranchSel, JMPSel, NextInstrSel;
	logic eq, blt;
	
	deco_PC DUT (BranchSel, eq, blt, JMPSel, NextInstrSel);
	
	initial begin
		
		BranchSel = 2'b0;
		JMPSel = 2'b0;
		blt = 1'b1;
		
		
		#10 JMPSel = 2'b01;

		
		
		#10 BranchSel = 2'b10;
		
		#10 blt = 1'b0;
	
	end
	

endmodule 