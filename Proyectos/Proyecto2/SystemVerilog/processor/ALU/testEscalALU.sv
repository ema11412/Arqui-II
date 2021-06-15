module testEscalALU;

logic Cin;
logic [2:0] ALUop;
logic [31:0] OpA, OpB;
logic Cout;
logic [31:0] Result;
logic Zero, Carry, OverFlow, Negative, eq, blt;

escal_ALU DUT (Cin, ALUop, OpA, OpB, Cout, Result, Zero, Carry, OverFlow, Negative, eq, blt);

	initial begin

		//Addition OpA > OpB:

		OpA = 6;
		OpB = 2;
		Cin = 0;
		ALUop = 3'b000;
		#10;
		
		//Addition OpA < OpB:
		
		OpA = 2;
		OpB = 7;
		Cin = 0;
		ALUop = 3'b000;
		#10;
		
		//Subtraction OpA > OpB:
		
		OpA = 10;
		OpB = 5;
		ALUop = 3'b001;
		#10;
		
		//Subtraction OpA < OpB:
		
		OpA = 5;
		OpB = 10;
		ALUop = 3'b001;
		#10;
		
		
		//Multiplication
		
		OpA = 10;
		OpB = 30;
		ALUop = 3'b010;
		#10;
		
		
		//Division
		
		OpA = 300;
		OpB = 30;
		ALUop = 3'b011;
		#10;


		//Or
		
		OpA = 10;
		OpB = 1;
		ALUop = 3'b100;
		#10;


		//And
		
		OpA = 10;
		OpB = 6;
		ALUop = 3'b101;
		#10;


		// Logical Shift Left
		
		OpA = 10;
		OpB = 2;
		ALUop = 3'b110;
		#10;
		

		
		//Logical Shift Right
		
		OpA = 10;
		OpB = 1;
		ALUop = 3'b111;
		#10;
		
		

	end


endmodule
