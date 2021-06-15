module vec_registers (input logic WriteEn,clk,
					          input logic [4:0] Rs1, Rs2,rd,
								 input logic [127:0]InputData,
								 output logic [127:0]Rout1, Rout2);
								 
								 logic [127:0] vec_reg[7:0];



								 always_ff @(posedge clk) 
										if (WriteEn) vec_reg[rd] <= InputData;

								assign Rout1 = vec_reg[Rs1];
								assign Rout2 = vec_reg[Rs2];

									
									
endmodule
