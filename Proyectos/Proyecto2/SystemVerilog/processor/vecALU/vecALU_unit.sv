module vecALU_unit(input logic VCSub,
							input logic [2:0] ALUop,
							input logic [31:0] inputA, inputB,
							input logic [15:0] Vx,
							input logic [7:0] c7,
							output logic [31:0] out);
							

logic [31:0] Vopg, Vopa;
logic [7:0] r11, r12, r13;
logic signed [7:0] minus;

assign r13 = c7;
assign r12 = Vx[15:8];
assign r11 = Vx[7:0];

assign minus = r12 - r11;


assign Vopg = r11 + (inputA*(minus)) / inputB;
assign Vopa = (inputA*(100-r13) + inputB*r13) / 100; 

always_comb
	if(VCSub) out <= inputA;
	else
		case (ALUop)
			3'b000: out <= inputA;
			3'b001: out <= Vopg;
			3'b010 : out <= Vopa;
			default: out <= 32'b0;
		endcase
endmodule