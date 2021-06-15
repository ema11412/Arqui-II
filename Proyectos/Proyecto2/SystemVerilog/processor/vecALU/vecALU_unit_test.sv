module vecALU_unit_test();

logic [2:0] ALUop;
logic [31:0] inputA, inputB, out;
logic [15:0] Vx;
logic [7:0] c7;
logic VCSub;

vecALU_unit DUT(VCSub, ALUop, inputA, inputB, Vx, c7, out);

initial begin
	VCSub = 0;
	c7 = 8'd25;

	inputA = 32'd100;
	inputB = 32'd103;

	Vx[7:0] = 8'd255;
	Vx[15:8] = 8'd255;

	ALUop = 3'b001; #10; //vopg
	assert(out === 32'd255) else $error("Failed"); // ESTE

	
	ALUop = 3'b010; #10; //vopa
	assert(out === 32'd100) else $error("Failed");
	
	inputA = 32'd101;
	Vx[7:0] = 8'd0;
	Vx[15:8] = 8'd255; #10;
	assert(out === 32'd101) else $error("Failed");

	ALUop = 3'b001; #10;
	assert(out === 32'd250) else $error("Failed"); // ESTE
	
	
	inputA = 32'd102;
	Vx[7:0] = 8'd255;
	Vx[15:8] = 8'd0; 
	#10;
	assert(out === 32'd2) else $error("failed"); // ESTE

	
	ALUop = 3'b010; #10;
	assert(out === 32'd102) else $error("Failed");
	


	#10;
end
endmodule