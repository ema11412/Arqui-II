module top_vec_reg(input logic WriteEn,clk,
					          input logic [4:0] Rs1, Rs2,rd,
								 input logic [127:0]InputData,
								 output logic [127:0]Rout1, Rout2);
								 
								 logic [4:0] rs1_dec, rs2_dec, rd_dec;
								 
								 vec_deco_reg_addr decoAddress (Rs1,Rs2,rd, rs1_dec, rs2_dec, rd_dec);
								 
								 vec_registers VReg (WriteEn,clk, rs1_dec, rs2_dec, rd_dec,InputData,Rout1, Rout2);
								 

endmodule
