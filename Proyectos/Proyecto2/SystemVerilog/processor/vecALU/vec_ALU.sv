module vec_ALU(input logic VCSub,
						input logic [2:0] ALUop,
						input logic [127:0] inputA, inputB,
						input logic [55:0] Vx,
						output logic [127:0] out);

logic [2:0] unitOp;
logic [31:0] out1, out2, out3, out4;
logic [7:0] c1, c2 ,c3 ,c4 ,c5 ,c6, temp1, temp2, temp3;



assign c1 = Vx[7:0];
assign c2 = Vx[15:8];
assign c3 = Vx[23:16];
assign c4 = Vx[31:24];
assign c5 = Vx[39:32];
assign c6 = Vx[47:40];


assign temp1 = Vx[55:49];
assign temp2 = Vx[55:49];
assign temp3 = Vx[55:49];


vecALU_unit unit1(VCSub, unitOp, inputA[31:0], inputB[31:0], {c1, c4} ,temp1 ,out1),
					unit2(VCSub, unitOp, inputA[63:32], inputB[63:32], {c2, c5}, temp2, out2),
					unit3(VCSub, unitOp, inputA[95:64], inputB[95:64], {c3, c6}, temp3, out3),
					unit4(VCSub, unitOp, inputA[127:96], inputB[127:96], 16'b0, 8'b0,out4);

always_comb
	case (ALUop)
		3'b001:
			begin
				unitOp <= 3'b001;
				out[31:0] <= out1;
				out[63:32] <= out2;
				out[95:64] <= out3;
				out[127:96] <= out4;
			end
		3'b010:
			begin
				unitOp <= 3'b010;
				out[31:0] <= out1;
				out[63:32] <= out2;
				out[95:64] <= out3;
				out[127:96] <= out4;
			end
		default:
			begin
				unitOp <= 3'b000;
				out[31:0] <= out1;
				out[63:32] <= out2;
				out[95:64] <= out3;
				out[127:96] <= out4;
			end
	endcase
endmodule
