module vec_ALU_test();

logic [2:0] ALUop;
logic [127:0] inputA, inputB, out;
logic VCSub;
logic [55:0] Vx;


vec_ALU DUT(VCSub, ALUop, inputA, inputB, Vx, out);

initial begin
	VCSub = 0;
	Vx[55:48] = 8'd25;
	Vx[47:24] = 24'hff00ff;
	Vx[23:0] = 24'h00ffff;


	inputA[31:0] = 32'd100;
	inputA[63:32] = 32'd101;
	inputA[95:64] = 32'd102;
	inputA[127:96] = 32'd103;
	
	inputB[31:0] = 32'd103;
	inputB[63:32] = 32'd103;
	inputB[95:64] = 32'd103;
	inputB[127:96] = 32'd103;

	
	ALUop = 3'b001; #10;
	assert(out[31:0] === 32'd255) else $error(" vopg 1 failed");
	assert(out[63:32] === 32'd250) else $error(" vopg 2 failed");
	assert(out[95:64] === 32'd2) else $error(" vopg 3 failed");
	assert(out[127:96] === 32'd0) else $error("vopg 4 failed");

	
	ALUop = 3'b010; #10;
	assert(out[31:0] === 32'd100) else $error("vopa 1 failed");
	assert(out[63:32] === 32'd101) else $error("vopa 2 failed");
	assert(out[95:64] === 32'd102) else $error("vopa 3 failed");
	assert(out[127:96] === 32'd0) else $error("vopa 4 failed");


end
endmodule