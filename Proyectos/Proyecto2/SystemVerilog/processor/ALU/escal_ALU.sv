module escal_ALU (input logic Cin,
					     input logic [2:0]ALUop,
						  input logic [31:0] OpA, OpB,
						  output logic Cout,
						  output logic [31:0] Result,
						  output logic Zero, Carry, OverFlow, Negative, eq, blt);
						  
						  logic [31:0]  result_add, result_sub, result_mul, result_div, result_or, result_and, result_sleft, result_sright; 
						  
						  add 	Add 		(OpA, OpB, Cin, Cout, result_add);
						  sub 	Sub 		(OpA, OpB, result_sub);
						  mul 	Mul 		(OpA, OpB, result_mul);
						  div	Div			(OpA, OpB, result_div);
						  or_ 	Or_		(OpA, OpB, result_or);
						  and_ 	And_		(OpA, OpB, result_and);
						  shift_left 	shift_Left 	(OpA, OpB, result_sleft);
						  shift_right shift_Right		(OpA, OpB, result_sright);

						  
						  mux_ALU main_mux (ALUop, result_add, result_sub, result_mul, result_div, result_or, result_and, result_sleft, result_sright, Result);
						  
						  assign Carry =  Cout & ~ALUop[1];
						  assign OverFlow = ~ALUop[1] & (result_add[31] ^ OpA[31]) & (OpA[31] ^ OpB[31] ^ ALUop[0]);
						  assign Negative = Result[31];
						  assign Zero = ~Result[31];
						  assign eq = (OpA == OpB);
						  assign blt = (OpA <= OpB);
endmodule
