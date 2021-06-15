`timescale 1 ps / 1 ps
module control_unit_test();
	
	logic [4:0] OPcode;
	logic [2:0] ALUop;
	logic [1:0] JMPSel;
	logic WriteRegister, MemWrite, RegWrite, vcsub, SelectorRs2, SelWriteData, WriteRegisterVec, SelectorRs1;
	logic [2:0] ALUOp;
	logic [1:0] SelectorOpB, BranchSel, SelectorOpA;

	
	control_unit DUT(OPcode, ALUop, JMPSel, WriteRegister, MemWrite, RegWrite, vcsub, ALUOp, 
							SelectorOpB, SelectorRs2, BranchSel, SelectorOpA, SelWriteData, WriteRegisterVec, SelectorRs1);

	initial begin
		
		OPcode = 5'b00000;
		ALUop = 3'b010;
		
		// R type
		#10 OPcode = 5'b00000; // ADD
		#10 ALUop = 3'b000;
		#10 ALUop = 3'b001;
		#10 ALUop = 3'b010;
		#10 OPcode = 5'b00101; // mov

		// I type
		#10 OPcode = 5'b01000; // addi
		#10 OPcode = 5'b01001; // subi
		#10 OPcode = 5'b01010; // muli
		#10 OPcode = 5'b01011; // divi
		#10 OPcode = 5'b01100; // ble
		#10 OPcode = 5'b01101; // movi

		// J type
		#10 OPcode = 5'b1000; // jmp

		// V type
		#10 OPcode = 5'b11101; // vst
		#10 OPcode = 5'b11011; // vld
		#10 OPcode = 5'b11000; // 
		ALUop = 3'b001; //vopg
		#10 ALUop = 3'b010; // vopa
		


		
	end
	
	
endmodule 